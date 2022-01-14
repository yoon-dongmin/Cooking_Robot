#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import time
import copy
import yaml
import csv
import json
import logging
import os
import datetime
import rospy
from collections import defaultdict
from os.path import dirname
from task_planning.searcher import AStarSearcher
from task_planning.planner import ForwardPlanner
from task_planning.domain import *
from task_planning.problem import StripsProblem
from object_level_motion import ObjectLevelMotion
import sample.club_sandwich
import sample.tuna_sandwich
import sample.greek_salad
import sample.shrimp_salad

import sample.test_33_predict2_v2
import sample.test_49_predict2_v2
import sample.test_80_predict2_v2
import sample.test_15_predict3_v2

KB_PATH = dirname(__file__) + '/task_planning/knowledge_base.yaml'

def get_network_output(file_path):
    """
    input
    - file_path : file path of network output
    output
    - goals : list of subgoals
    - using_ings : list of core ingredients
    - new_objs<dict> : key=new object(salad, sandwich, ...etc) 
                        val=list of it's component objects
    - goal_diffs : list of goals[i]-goals[i-1]
    """
    goals = []
    goal_diffs = []
    using_ings = []
    new_objs = defaultdict(list)
    raw_data = None
    
    # read csv file
    with open(file_path) as csvfile:
        raw_data = list(csv.reader(csvfile))
    
    # info of file
    num_of_task = int(raw_data[0][0])
    num_of_obj = int(raw_data[0][1])
    ings_1 = raw_data[1] # ingredient
    ings_2 = raw_data[2] # bottled_ingredient
    new_i = 3
    while True:
        if raw_data[new_i][0] == 'Task':
            break
        else:
            new_objs[raw_data[new_i][0]] = raw_data[new_i][1:]
            new_i += 1

    # 
    sandwich_idx = -1
    passed_sandwich = False
    passed_salad = False
    for i in range(new_i+1, new_i+1+num_of_task*num_of_obj-1, num_of_obj):
        task = raw_data[i:i+num_of_obj]

        # subgoal
        subgoal = dict()
        for row in task:
            obj = row[1]
            state = row[2].split(',')
            rel_on = row[3]
            rel_in = row[4]
            rel_sp = row[5]
            if obj in ings_1:
                for st in state:
                    if 'exist' in st:
                        subgoal.update({'exist_'+obj: True})
                    elif 'chopped' in st:
                        subgoal.update({'chopped_'+obj: True})
                    elif 'cooked' in st:
                        subgoal.update({'cooked_'+obj: True})
                if rel_on != 'none':
                    subgoal.update({obj+'_is_on': rel_on})
                if rel_in != 'none':
                    subgoal.update({obj+'_is_in': rel_in})
                if rel_sp != 'none':
                    subgoal.update({'spread_on_'+obj: rel_sp})
        
        # delete subgoals for tuna_spread
        if ('exist_tuna_spread' in subgoal.keys()) and subgoal['exist_tuna_spread']:
            for ts_i in range(len(new_objs['tuna_spread'])):
                del subgoal[new_objs['tuna_spread'][ts_i]+'_is_in']
                del subgoal['exist_'+new_objs['tuna_spread'][ts_i]]

        # delete subgoals for sandwich
        ings = set()
        if not passed_sandwich:
            sandwich_idx += 1
        if ('exist_sandwich' in subgoal.keys()) and subgoal['exist_sandwich']:
            passed_sandwich = True
            del subgoal['exist_'+new_objs['sandwich'][0]]
            for sand_i in range(1, len(new_objs['sandwich'])):
                # print('del', new_objs['sandwich'][sand_i]+'_is_on')
                del subgoal[new_objs['sandwich'][sand_i]+'_is_on']
                del subgoal['exist_'+new_objs['sandwich'][sand_i]]
            # add last ingredient of sandwich
            ings |= using_ings[sandwich_idx-1][0]

        # delete subgoals for salad
        if ('exist_salad' in subgoal.keys()) and subgoal['exist_salad']:
            passed_salad = True
        if passed_salad:
            for sal_i in range(len(new_objs['salad'])):
                del subgoal[new_objs['salad'][sal_i]+'_is_in']
                del subgoal['exist_'+new_objs['salad'][sal_i]]
        
        # calculate difference between subgoals
        subgoal_diff = dict()
        if goals:
            subgoal_1 = copy.deepcopy(goals[-1])
            for key, val in subgoal.items():
                if key in subgoal_1.keys():
                    if subgoal_1[key] != val:
                        subgoal_diff[key] = val
                else:
                    subgoal_diff[key] = val
        
        # extract using_ings from subgoal_diff
        for key, val in subgoal_diff.items():
            if 'cooked' in key:
                ings.add(key[7:])
            if 'chopped' in key:
                ings.add(key[8:])
            if 'spread_on' in key:
                ings.add(key[10:])
            if 'is_on' in key:
                ings.add(key[:-6])
            if 'is_in' in key:
                ings.add(key[:-6])
            if 'exist' in key:
                ings.add(key[6:])
            if val not in [True, False]:
                if val != 'bowl':
                    ings.add(val)
            ings |= set(ings_2)
        
        # append to list
        goals.append(subgoal)
        using_ings.append([ings, {}])
        goal_diffs.append(subgoal_diff)
    
    # remove goal above exist sandwich
    if passed_sandwich:
        goals.pop(sandwich_idx-1)
        using_ings.pop(sandwich_idx-1)
        goal_diffs.pop(sandwich_idx-1)

    return goals, using_ings, new_objs, goal_diffs

def get_knowledge_base():
    with open(KB_PATH) as f:  # Path
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)
    return yaml_data

def get_default_initial(obj_state, kb):
    """
    input
    - obj_state : list of object instance, type and state
    - kb : knowledge base yaml data
    output
    - initial : set of initial state
    """
    ingredients = set()
    ing_bottles = set()
    tools = set()
    containers = set()
    exist_ings = set()
    objects = dict()

    for (oinstance, otype, ostate) in obj_state:
        rospy.loginfo("{}, {}, {}".format(oinstance, otype, ostate))
        objects[oinstance] = otype
        if 'ingredient' in kb[otype]['isA']:
            ingredients.add(oinstance)
            if 'exist' in ostate:
                exist_ings.add(oinstance)
        elif 'ing_bottle' in kb[otype]['isA']:
            ing_bottles.add(oinstance)
        elif 'tool' in kb[otype]['isA']:
            tools.add(oinstance)
        elif 'container' in kb[otype]['isA']:
            containers.add(oinstance)

    initial = {'holding': 'None'}
    initial.update({in_relation(x): 'None' for x in ingredients})
    initial.update({on_relation(x): 'table' for x in ingredients|tools|containers|ing_bottles})
    initial.update({spread(x): 'None' for x in ingredients})
    initial.update({cooked(x): False for x in ingredients})
    initial.update({chopped(x): False for x in ingredients})
    initial.update({is_exist(x): True for x in exist_ings})
    initial.update({is_exist(x): False for x in ingredients-exist_ings})
    
    return initial

def set_ingredients(obj_state, kb, ings):
    """
    input
    - obj_state : list of object instance, type and state
    - kb : knowledge base yaml data
    - ings : list of core ingredients
    output
    - using_objects<dict> : key=object instance, val=object type
    """
    using_objects = dict()
    ing_list = list(ings[0])+list(ings[1])
    for instance, otype, state in obj_state:
        if 'container' in kb[otype]['isA']:
            using_objects[instance] = otype
        elif 'tool' in kb[otype]['isA']:
            using_objects[instance] = otype
        elif 'place' in kb[otype]['isA']:
            using_objects[instance] = otype
        elif 'ingredient' in kb[otype]['isA']:
            if instance in ing_list:
                using_objects[instance] = otype
        elif 'ing_bottle' in kb[otype]['isA']:
            if kb[otype]['Contains'][0] in ing_list:
                using_objects[instance] = otype
    return using_objects

def make_task_planner(problem, objects, knowledge_base, new_objs):
    sandwich_problem = StripsProblem(problem)
    cooking_domain = CookingDomain(objects, knowledge_base, new_objs)
    planning_problem = ForwardPlanner(cooking_domain, sandwich_problem)
    searcher = AStarSearcher(planning_problem)

    return searcher

def make_obj_state(file_path):
    """
    input
    - file_path : file path of network output
    output
    - obj_state : list of object instance, type and state
    """
    ing_idx = dict()
    with open(file_path) as csvfile:
        raw_data = list(csv.reader(csvfile))

    # info of file
    num_of_task = int(raw_data[0][0])
    num_of_obj = int(raw_data[0][1])
    ings_1 = raw_data[1] # ingredient
    ings_2 = raw_data[2] # bottled_ingredient
    new_i = 3
    while True:
        if raw_data[new_i][0] == 'Task':
            break
        else:
            new_i += 1
    
    task0 = raw_data[new_i+1:new_i+1+num_of_obj]
    for t in range(len(task0)):
        if task0[t][1] in ings_1:
            ing_idx[task0[t][1]] = t

    # instance-type-state
    obj_state = []

    # container
    obj_state.append(['pan', 'pan', None])
    obj_state.append(['pot', 'pot', None])
    obj_state.append(['plate', 'plate', None])
    obj_state.append(['bowl', 'bowl', None])

    # tool
    obj_state.append(['spatula', 'spatula', None])
    obj_state.append(['spreader', 'spreader', None])
    obj_state.append(['scooper', 'scooper', None])
    obj_state.append(['knife', 'knife', None])

    # place
    obj_state.append(['table', 'table', None])
    obj_state.append(['stove', 'stove', None])
    obj_state.append(['cutting_board', 'cutting_board', None])
    obj_state.append(['near_cutting_board', 'near_cutting_board', None])

    # ingredient
    for obj in ings_1:
        obj_name = obj
        if obj_name[-1] in ['1', '2', '3']:
            obj_type = obj_name[:-1]
        else:
            obj_type = obj_name
        if 'exist' in task0[ing_idx[obj_name]][2]:
            obj_state.append([obj_name, obj_type, ['exist']])
        else:
            obj_state.append([obj_name, obj_type, []])

    # ingredient bottle
    for obj in ings_2:
        obj_name = obj+'_bottle'
        obj_type = obj+'_bottle'
        obj_state.append([obj_name, obj_type, None])
    
    return obj_state

def save_list_of_dict(file_path, column, dict_data):
    """
    save dict_data(list of dict) to csv file
    """
    with open(file_path, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column)
        writer.writeheader()
        for data in dict_data:
            # writer.writerow(data)
            writer.writerow(dict(zip(column, map(data.get, column))))

def run_test_set():
    # selected = 'predict_v2'
    selected = 'predict2_v2'
    test_set = range(0, 68)

    # csv
    test_dir = dirname(dirname(__file__)) + '/test_set/{}/'.format(selected)
    result_dir = dirname(dirname(__file__)) + '/result/{}/'.format(selected)
    for target_dir in [test_dir, result_dir]:
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

    total_result_file_name = 'total_result.csv'
    total_result_file_path = result_dir + total_result_file_name

    # initialize for task planning
    knowledge_base = get_knowledge_base()

    test_file_infos = []
    for r in test_set:
        # test file path
        test_file_name = 'test_{}_{}.csv'.format(r, selected)
        test_file_path = test_dir + test_file_name

        result_file_name = 'test_{}_{}.csv'.format(r, selected)
        result_file_path = result_dir + result_file_name

        rospy.loginfo('file_name = '+test_file_name)
        rospy.loginfo('-'*10)
        
        # get object state
        obj_state = make_obj_state(test_file_path)
        for objs in obj_state:
            rospy.loginfo(objs)
        rospy.loginfo('-'*10)
        
        # get network output
        (goals, using_ings, new_objs, goal_diffs) = get_network_output(test_file_path)
        default_initial = get_default_initial(obj_state, knowledge_base)

        path = None
        task_plan_infos = []
        success = False
        for t in range(1, len(goals)):
            # reduce object set
            using_objects = set_ingredients(obj_state, knowledge_base, using_ings[t])

            current = None
            rospy.loginfo('='*20)
            rospy.loginfo('[task={}]'.format(t))

            # generate problem
            initial = copy.deepcopy(default_initial)
            initial.update(goals[t-1])
            if path:
                initial.update(path.end())
            problem = [initial, goals[t]]
            
            # info
            rospy.loginfo('####### generate problem #######')
            rospy.loginfo('using_ings: {}'.format(using_ings[t]))
            rospy.loginfo('using_objects: {}'.format(using_objects))
            rospy.loginfo('goal: {}'.format(goals[t]))
            rospy.loginfo('goal_diff: {}'.format(goal_diffs[t]))
            rospy.loginfo('current: {}'.format(current))
            rospy.loginfo('initial: {}'.format(initial))

            # task plan
            task_planner = make_task_planner(problem, using_objects, knowledge_base, new_objs)
            start = time.time()
            success = task_planner.search()
            end = time.time()

            rospy.loginfo('####### task plan info #######')
            path = task_planner.solution
            rospy.loginfo('plan = {}'.format(task_planner.solution))
            rospy.loginfo('length = {}'.format(len(task_planner.solution)-1))
            rospy.loginfo('num_of_expand = {}'.format(task_planner.num_expanded))
            rospy.loginfo('time = {}'.format(end-start))
            rospy.loginfo('success = {}'.format(success))

            task_plan_info = dict()
            task_plan_info['task'] = t
            task_plan_info['subgoal'] = goal_diffs[t]
            task_plan_info['plan'] = task_planner.solution.to_str()
            task_plan_info['length'] = len(task_planner.solution)-1
            task_plan_info['num_of_expand'] = task_planner.num_expanded
            task_plan_info['time'] = end-start
            task_plan_info['success'] = success
            task_plan_infos.append(task_plan_info)
                
            if not success:
                break
        
        save_list_of_dict(result_file_path, ['task', 'subgoal', 'length', 'plan', 'success', 'time', 'num_of_expand'], task_plan_infos)

        test_file_info = dict()
        test_file_info['test_num'] = r
        test_file_info['total_subgoal'] = len(goals)-1
        test_file_info['solved_subgoal'] = [tpi['success'] for tpi in task_plan_infos].count(True)
        test_file_info['success'] = success
        test_file_info['total_time'] = sum(tpi['time'] for tpi in task_plan_infos)
        test_file_infos.append(test_file_info)
    
    save_list_of_dict(total_result_file_path, ['test_num', 'total_subgoal', 'solved_subgoal', 'success', 'total_time'], test_file_infos)

def main():
    use_moveit = True
    use_unity = True

    # sample
    # sandwich = sample.club_sandwich
    # sandwich = sample.tuna_sandwich
    sandwich = sample.greek_salad
    # sandwich = sample.shrimp_salad
    # sandwich = sample.test_15_predict3_v2
    # sandwich = sample.test_33_predict2_v2
    # sandwich = sample.test_49_predict2_v2
    # sandwich = sample.test_80_predict2_v2

    # csv
    test_dir = dirname(dirname(__file__)) + '/test_set/default_v2/'
    # test_dir = dirname(dirname(__file__)) + '/test_set/predict2_v2/'
    # test_dir = dirname(dirname(__file__)) + '/test_set/predict3_v2/'
    result_dir = dirname(dirname(__file__)) + '/result/default_v2/'
    # result_dir = dirname(dirname(__file__)) + '/result/predict2_v2/'
    # result_dir = dirname(dirname(__file__)) + '/result/predict3_v2/'
    for target_dir in [test_dir, result_dir]:
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

    test_path = test_dir + sandwich.test_file_name
    suffix = datetime.datetime.now().strftime("_%y%m%d_%H%M%S")
    tp_result_path = result_dir + sandwich.test_file_name[:-4] + suffix + '_tp.csv'
    ola_result_path = result_dir + sandwich.test_file_name[:-4] + suffix + '_ola.csv'
    mp_result_path = result_dir + sandwich.test_file_name[:-4] + suffix + '_mp.csv'

    # initialize for task planning
    knowledge_base = get_knowledge_base()
    (goals, using_ings, new_objs, goal_diffs) = get_network_output(test_path)
    default_initial = get_default_initial(sandwich.obj_state, knowledge_base)
    
    raw_input("Experiment Start!!")

    # initialize for motion planning
    if use_moveit:
        obj_test = ObjectLevelMotion(use_unity)
        obj_test.initialize(sandwich.obj_place)
    
        if use_unity:
            obj_test.init_sync()
            obj_test.scene_sync()
            

    path = None
    tp_infos = []
    ola_infos = []
    mp_infos = []
    finished = False
    for t in range(1, len(goals)):
        # reduce object set
        using_objects = set_ingredients(sandwich.obj_state, knowledge_base, using_ings[t])

        ola_success = False
        replan_num = 0
        while (not ola_success) and replan_num < 3:
            current = None
            rospy.loginfo('='*50)
            rospy.loginfo('[task={}]'.format(t))

            # generate problem
            initial = copy.deepcopy(default_initial)
            initial.update(goals[t-1])
            if use_moveit:
                current = obj_test.get_current_state()
                initial.update(current)
                problem = [initial, goals[t]]
            else:
                if path:
                    initial.update(path.end())
                problem = [initial, goals[t]]
            
            # rospy.loginfo details
            rospy.loginfo('####### generate problem #######')
            rospy.loginfo('using_ings: {}'.format(using_ings[t]))
            rospy.loginfo('using_objects: {}'.format(using_objects))
            rospy.loginfo('goal: {}'.format(goals[t]))
            rospy.loginfo('goal_diff: {}'.format(goal_diffs[t]))
            rospy.loginfo('current: {}'.format(current))
            rospy.loginfo('initial: {}'.format(initial))
            
            # task plan
            task_planner = make_task_planner(problem, using_objects, knowledge_base, new_objs)
            start = time.time()
            success = task_planner.search()
            end = time.time()

            rospy.loginfo('####### task plan info #######')
            path = task_planner.solution
            rospy.loginfo('plan = {}'.format(task_planner.solution))
            rospy.loginfo('length = {}'.format(len(task_planner.solution)-1))
            rospy.loginfo('num_of_expand = {}'.format(task_planner.num_expanded))
            rospy.loginfo('time = {}'.format(end-start))
            rospy.loginfo('success = {}'.format(success))

            tp_info = dict()
            tp_info['task'] = t ##
            tp_info['subgoal'] = goal_diffs[t]
            tp_info['plan'] = task_planner.solution.to_str()
            tp_info['length'] = len(task_planner.solution)-1
            tp_info['num_of_expand'] = task_planner.num_expanded
            tp_info['time'] = end-start
            tp_info['success'] = success
            tp_infos.append(tp_info)

            if not success:
                finished = True
                break

            # run action_sequences
            action_sequences = [action.split('/') for action in task_planner.solution.to_str().split(" -> ") if action]
            if use_moveit:
                # success = False
                for i, action in enumerate(action_sequences):
                    rospy.loginfo('='*50)
                    rospy.loginfo('[ola={}] {}'.format(i, action))
                    
                    start = time.time()
                    ola_success, ola_info = obj_test.run(action)
                    end = time.time()

                    mpi = ola_info.pop('mp_infos')
                    for j in range(len(mpi)):
                        rospy.loginfo('####### motion plan info #######')
                        rospy.loginfo('planning_time = {}'.format(mpi[j]['planning_time']))
                        rospy.loginfo('execution_time = {}'.format(mpi[j]['execution_time']))
                        rospy.loginfo('success = {}'.format(mpi[j]['success']))
                        mpi[j]['action'] = ola_info['action']
                        mpi[j]['action_length'] = ola_info['length']
                        mpi[j]['sequence'] = j
                        mpi[j]['task'] = t               
                    mp_infos.extend(mpi)

                    rospy.loginfo('####### object-level action info #######')
                    rospy.loginfo('time = {}'.format(end-start))                    
                    rospy.loginfo('action = {}'.format(ola_info['action']))
                    rospy.loginfo('length = {}'.format(ola_info['length']))
                    rospy.loginfo('success = {}'.format(ola_success))
                    ola_info['time'] = end-start
                    ola_info['task'] = t
                    ola_infos.append(ola_info)
                    
                    # if object-level action failed, break from for loop and replan
                    if not ola_success:
                        replan_num += 1
                        rospy.loginfo('!'*20 + 'replan {}'.format(replan_num))
                        break
            else:
                break
        
        if finished:
            break
    
    # save to csv
    save_list_of_dict(tp_result_path, ['task', 'subgoal', 'length', 'plan', 'success', 'time', 'num_of_expand'], tp_infos)
    if use_moveit: 
        save_list_of_dict(ola_result_path, ['task', 'action', 'length', 'time', 'success'], ola_infos) 
        save_list_of_dict(mp_result_path, ['task', 'action', 'action_length', 'sequence', 'planning_time', 'execution_time', 'success'], mp_infos) 

if __name__ == "__main__":
    rospy.init_node('PandaMove', anonymous=True)
    main()
    # run_test_set()