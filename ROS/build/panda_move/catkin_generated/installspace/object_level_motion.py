#!/usr/bin/env python2
from numpy.lib.function_base import place
from pose_level_motion import *
import tf
import sys
import os
import copy
import rospy
import yaml
import numpy as np
import math as m
import random
import pyautogui
from os.path import dirname
from collections import defaultdict
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from std_msgs.msg import String
from visualization_msgs.msg import Marker
from moveit_commander.conversions import pose_to_list, list_to_pose
from geometry_msgs.msg import Quaternion
import threading
import time

import utils
import sample.club_sandwich
import sample.tuna_sandwich
import sample.greek_salad
import sample.shrimp_salad

from panda_move.srv import Init, InitRequest, InitResponse
from panda_move.srv import Sync, SyncRequest, SyncResponse
from panda_move.srv import Plan, PlanRequest, PlanResponse
from panda_move.srv import Hand, HandRequest, HandResponse
from panda_move.srv import MotionCheck, MotionCheckRequest, MotionCheckResponse
from panda_move.msg import ExecutionCheck

# Set Path
YAML_PATH = dirname(dirname(__file__)) + '/config/'
POSE_INFO_PATH = YAML_PATH + 'object_pose_info.yaml'
STL_INFO_PATH = YAML_PATH + 'object_stl_info.yaml'
PLACEMENT_INFO_PATH = YAML_PATH + 'placement_pose_info.yaml'
STL_PATH = dirname(dirname(dirname(__file__))) + '/object_sample/'

SAUCES = ['mayonnaise', 'sugar', 'pepper', 'salt', 'black_pepper', 'lemon_juice', 'olive_oil']

def import_yaml(file_path):
    with open(file_path) as f:  # Path
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)
    return yaml_data

def pressEnter(msg):
    if msg.status:
        pyautogui.press('enter')

class ObjectLevelMotion(PoseLevelMotion):
    def __init__(self, use_unity, self_play=True):
        PoseLevelMotion.__init__(self, self_play)

        # True to use unity / False to not use unity
        self.unity = use_unity

        # yaml
        self.obj_pose_yaml = import_yaml(POSE_INFO_PATH)
        self.obj_stl_yaml = import_yaml(STL_INFO_PATH)
        self.placement_yaml = import_yaml(PLACEMENT_INFO_PATH)

        # publisher
        self.marker_pub = rospy.Publisher('action', Marker, queue_size=1)

        # key=object state, val=object list
        self.objects = defaultdict(list)
        # obj instance -> obj type
        self.instance_type = dict()
        # place area -> list of placement pose name
        self.place_area_poses = defaultdict(list)
        # key=container, val=(sorted)list of objects
        self.contain_objects = dict()
        # key=object, val=number of pour
        self.num_of_pour = defaultdict(int)
        # self.execution_check()
        # check_thread = threading.Thread(target=self.execution_check)
        # check_thread.start()

    ### Unity - ROS Communication Method Start ###
    def init_sync(self):
        if self.unity == True:
            try:
                rospy.wait_for_service("init_sync")
                init_sync_client = rospy.ServiceProxy("init_sync", Init)
                init_sync_req = InitRequest()

                joint_state = self.robot.get_current_state().joint_state.position
                init_sync_req.joint_state = joint_state

                for i in range(len(self.objects["activated"])):
                    temp_name = self.objects["activated"][i]
                    temp_type = self.instance_type[temp_name]
                    temp_position = self.get_object_pose(temp_name).position
                    temp_orientation = self.get_object_pose(
                        temp_name).orientation

                    init_sync_req.activated_object.append(temp_name)
                    # init_sync_req.object_name.append(temp_name)
                    init_sync_req.position.append(temp_position)
                    init_sync_req.orientation.append(temp_orientation)
                    temp_scale = geometry_msgs.msg.Vector3()
                    temp_scale.x = self.obj_stl_yaml[temp_type]["scale"][0]
                    temp_scale.y = self.obj_stl_yaml[temp_type]["scale"][1]
                    temp_scale.z = self.obj_stl_yaml[temp_type]["scale"][2]
                    init_sync_req.scale.append(temp_scale)
                
                init_sync_res = init_sync_client(init_sync_req)
                if init_sync_res.init_state == 1:
                    raw_input("Initialization Sync Completed")
                else:
                    rospy.loginfo("[Unity Error] Initialization Sync Failed")

            except Exception as e:
                rospy.logerr(e)
        elif self.unity == False:
            pass

    def scene_sync(self):
        if self.unity == True:
            try:
                rospy.wait_for_service("scene_sync")
                scene_sync_client = rospy.ServiceProxy("scene_sync", Sync)
                scene_sync_req = SyncRequest()
                scene_sync_req.activated_object = self.objects["activated"]

                scene_sync_res = scene_sync_client(scene_sync_req)

                for i in range(len(scene_sync_res.joint_state)):
                    if i == 0:
                        self.joint[i].move(scene_sync_res.joint_state[i])
                    elif i > 0 and i < 8:
                        self.joint[i].move(
                            scene_sync_res.joint_state[i] * m.pi / 180)
                    else:
                        self.joint[i].move(scene_sync_res.joint_state[i])

                for i in range(len(scene_sync_res.object_name)):
                    temp_name = scene_sync_res.object_name[i]
                    temp_pose = geometry_msgs.msg.Pose()
                    temp_pose.position = scene_sync_res.position[i]
                    temp_pose.orientation = scene_sync_res.orientation[i]
                    self.update_object_pose(temp_name, temp_pose)
                rospy.loginfo("Scene Sync Completed")

            except Exception as e:
                rospy.logerr(e)

        elif self.unity == False:
            pass

    def hand_sync(self, object_name, grasp_size):
        if self.unity == True:
            try:
                rospy.wait_for_service("hand_sync")
                hand_sync_client = rospy.ServiceProxy("hand_sync", Hand)
                hand_sync_req = HandRequest()
                hand_sync_req.grasp_state = self.grasp_state
                hand_sync_req.object_name = object_name
                hand_sync_req.grasp_size = grasp_size

                hand_sync_res = hand_sync_client(hand_sync_req)

                if hand_sync_res.execute_state == 1:
                    rospy.loginfo("Hand Sync Completed")
                else:
                    rospy.loginfo("[Unity Error] Hand Sync Failed")

            except Exception as e:
                rospy.logerr(e)

        elif self.unity == False:
            pass

    def panda_plan(self, plan_i):
        if self.unity == True:
            try:
                rospy.wait_for_service("panda_plan")
                panda_plan_client = rospy.ServiceProxy("panda_plan", Plan)
                panda_plan_req = PlanRequest()
                panda_plan_req.trajectories.append(plan_i)

                panda_plan_res = panda_plan_client(panda_plan_req)

                if panda_plan_res.execute_state == 1:
                    raw_input("Plan Execution Complelted")
                else:
                    rospy.loginfo("[Unity Error] Plan Execution Failed")

                # self.execution_check()

            except Exception as e:
                rospy.logerr(e)

        elif self.unity == False:
            pass
    
    def motion_check(self, motion_type, object_1, object_2):
        if self.unity == True:
            try:
                rospy.wait_for_service("motion_check")
                motion_check_client = rospy.ServiceProxy("motion_check", MotionCheck)
                motion_check_req = MotionCheckRequest()
                motion_check_req.motion_type = motion_type
                motion_check_req.object_1 = object_1
                motion_check_req.object_2 = object_2

                motion_check_res = motion_check_client(motion_check_req)

                if motion_check_res.execute_state == 1:
                    rospy.loginfo("Motion Type Interaction Completed")
                else:
                    rospy.loginfo("[Unity Error] Motion Type Interaction Failed")
            except Exception as e:
                rospy.logerr(e)
        
        elif self.unity == False:
            pass

    # def execution_check(self):
    #     if self.unity == True:
    #         try:
    #             rospy.Subscriber("execution_check", ExecutionCheck, pressEnter)
    #             rospy.spin()
    #         except Exception as e:
    #             rospy.logerr(e)
        
    #     elif self.unity == False:
    #         pass

    # def pressEnter(self, msg):
    #     if msg.status:
    #         pyautogui.press('enter')
    ## Unity - ROS Communication Method End ##

    def _arrange(self, obj_name, obj_type, placement):
        try:
            placement_pose = self.placement_yaml[placement]['pose']
            place_pose = self._make_place_pose(obj_type)
            place_pose_inv = utils.inv_trans_mat(place_pose)
            
            object_pose = utils.concatenate_to_pose_list(placement_pose, place_pose_inv)
            object_mesh = STL_PATH + self.obj_stl_yaml[obj_type]['file_name']
            object_size = self.obj_stl_yaml[obj_type]['scale']
            frame_id = self.placement_yaml[placement]['frame_id']

            # raw_input(obj_name)
            rospy.loginfo(obj_name)
            self.add_object(obj_name, object_pose,
                            object_mesh, object_size, frame_id)

        except Exception as e:
            rospy.logerr(e)

    def _update_place_pose_state(self):
        place_pose_state = {}
        place_thresh = 0.1
        
        rospy.loginfo('wait for update_place_pose_state')
        time.sleep(0.7)

        def distance(p1, p2):
            return m.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

        # get collision object poses from Planing Scene
        obj_poses = dict()
        for obj in self.objects['activated']:
            obj_pose = self.get_object_pose(obj)
            rospy.loginfo("obj={}, obj_pose={}".format(obj, obj_pose))
            if obj_pose:
                obj_poses[obj] = obj_pose
            else:
                rospy.logerr("self.objects", self.objects)
                exit()

        for key, val in self.placement_yaml.items():
            place_pose_state[key] = []
            
            # calculate xy_dist
            for obj, obj_pose in obj_poses.items():
                obj_type = self.instance_type[obj]
                place_pose = self._make_place_pose(obj_type)
                obj_place_pose = utils.concatenate_to_pose_list(obj_pose, place_pose)
                xy_dist = distance(val['pose'], obj_place_pose)
                if xy_dist < place_thresh:
                    # bottom = obj_place_pose[2] - self.obj_stl_yaml[obj_type]['thickness'][0]
                    bottom = obj_place_pose[2]
                    place_pose_state[key].append({'name': obj, 'z': bottom})
            
            # sort by z value
            rospy.loginfo("^"*30)
            if place_pose_state[key]:
                rospy.loginfo("key={}, val={}".format(key, place_pose_state[key]))
                sorted_obj = sorted(place_pose_state[key], key=lambda x: x.get('z'))
                place_pose_state[key] = [obj['name'] for obj in sorted_obj]       
        
        return place_pose_state, obj_poses.keys()
    
    def _match_place_to_area(self, place, obj_category):
        if place == 'table':
            if obj_category == 'ingredient':
                area = 'table1_ingredient_area'
            elif obj_category == 'ing_bottle':
                area = 'table1_ing_bottle_area'
            elif obj_category == 'cookware':
                area = 'table1_cookware_area'
            elif obj_category == 'dishware':
                area = 'table1_dishware_area'
            elif obj_category == 'tool':
                area = 'table1_tool_area'
        elif place == 'stove':
            if obj_category == 'cookware':
                area = 'stove_cookware_area'
        elif place == 'cutting_board':
            if obj_category == 'ingredient':
                area = 'cutting_board_ingredient_area'
        elif place == 'near_cutting_board':
            if obj_category == 'dishware':
                area = 'near_cutting_board_bowl_area'
        return area

    def _select_pose_from_area(self, obj, obj_to_area):
        candidate_poses = []
        feasible_poses = []
        selected_pose = None

        # update place pose state
        place_available, _ = self._update_place_pose_state()
        print('-'*30)
        print(place_available)

        # candidate_poses
        candidate_poses = self.place_area_poses[obj_to_area]
        print('candidate_poses', candidate_poses)

        # feasible_poses
        for pose in candidate_poses:
            if not place_available[pose]:
                feasible_poses.append(pose)
        print('feasible_poses', feasible_poses)

        # selected_pose
        if feasible_poses:
            selected_pose = random.choice(feasible_poses)        
        print('selected_pose', selected_pose)
        print('-'*30)

        return selected_pose

    def _to_symbolic_state(self, place_pose_state, obj_list):
        symbolic_state = {}

        # holding
        holding_obj = copy.deepcopy(self.objects['attached'])
        if len(holding_obj) > 1:
            AssertionError("more than one holding obj")
        if holding_obj:
            symbolic_state['holding'] = holding_obj[0]

        # in, on, is_near
        for key, val in place_pose_state.items():
            if val:
                # rename for task planner
                re_val = copy.deepcopy(val)
                for i in range(len(val)):
                    # chopped obj
                    if val[i][:8] == 'chopped_':
                        re_val[i] = val[i][8:]
                    # poured obj
                    elif val[i][-2:] in ['_1', '_2', '_3']:
                        re_val[i] = val[i][:-2]
                        
                # symbolic state for bowl, pot, pan, plate
                if self.instance_type[re_val[0]] in ['bowl', 'pot', 'plate', 'pan']:
                    container = self.instance_type[re_val[0]]                    
                    # for container
                    if key in self.place_area_poses['near_cutting_board_bowl_area']:
                        symbolic_state[re_val[0]+'_is_on'] = 'near_cutting_board'
                    else:
                        symbolic_state[re_val[0]+'_is_on'] = self.placement_yaml[key]['type']
                    # for object in/on container
                    if container in ['bowl', 'pot']:
                        for i in range(1, len(val)):
                            symbolic_state[re_val[i]+'_is_in'] = re_val[0]
                    elif container in ['plate', 'pan']:
                        for i in range(1, len(re_val)):
                            symbolic_state[re_val[i]+'_is_on'] = re_val[i-1]
                
                # symbolic state for etc(sandwich)
                else:
                    symbolic_state[re_val[0]+'_is_on'] = self.placement_yaml[key]['type']
                    for i in range(1, len(re_val)):
                        symbolic_state[re_val[i]+'_is_on'] = re_val[i-1]
                    
        return symbolic_state

    def _make_place_pose(self, obj_type):
        if 'place_pos' in self.obj_pose_yaml[obj_type].keys():
            place_pos = self.obj_pose_yaml[obj_type]['place_pos']
        else:
            place_pos = [0, 0, -self.obj_stl_yaml[obj_type]['thickness'][0]-0.001]
        place_orient = utils.rpy_to_quaternion_list(self.obj_pose_yaml[obj_type]['place_orient'])
        place_pose = place_pos + place_orient

        return place_pose

    def initialize(self, arrange_info, fixed_pose=None):
        try:
            # Temp (table setup)
            # raw_input("table1")
            # self.add_box("table1", [0.5, 0, 0.2, 0, 0, 0], (0.5, 3, 0.4))
            # raw_input("table2")
            # self.panda.add_box("table2", )
            
            # initialize self.place_poses
            for key, val in self.placement_yaml.items():
                for area in val['area']:
                    self.place_area_poses[area].append(key)

            for (obj_instance, obj_type, place_area, obj_state) in arrange_info:
                # add object
                placement = self._select_pose_from_area(obj_type, place_area)
                self._arrange(obj_instance, obj_type, placement)

                # initialize self.objects
                if obj_state is not None:
                    self.objects[obj_state].append(obj_instance)

                # initialize self.instance_type 
                self.instance_type[obj_instance] = obj_type

            raw_input("Initial Scene Configuration Completed")

        except Exception as e:
            rospy.logerr(e)

    def get_current_state(self):
        place_pose_state, obj_list = self._update_place_pose_state()
        current_state = self._to_symbolic_state(place_pose_state, obj_list)

        return current_state

    def run(self, action):
        def marker_msg(action):
            marker_ = Marker()
            marker_.header.frame_id = "/table1"
            marker_.header.stamp = rospy.Time.now()
            marker_.type = marker_.TEXT_VIEW_FACING
            marker_.action = marker_.ADD
            marker_.text = str(action)
            marker_.pose.position.x = 0
            marker_.pose.position.y = 0
            marker_.pose.position.z = 0.8
            marker_.pose.orientation.x = 0
            marker_.pose.orientation.y = 0
            marker_.pose.orientation.z = 0
            marker_.pose.orientation.w = 1
            marker_.scale.x = 0.1
            marker_.scale.y = 0.1
            marker_.scale.z = 0.1

            marker_.color.r = 1
            marker_.color.g = 1
            marker_.color.b = 1
            marker_.color.a = 1
            return marker_
        self.marker_pub.publish(marker_msg(action))
        
        # Run each action
        success = False
        ola_info = dict() 
        if action[0] == 'PickUp':
            success, mp_infos = self.pick_up(action[1])
            ola_info['length'] = 4
        elif action[0] == 'Place':
            success, mp_infos = self.place(action[1], action[2], action[3])
            ola_info['length'] = 4
        elif action[0] == 'Pour':
            success, mp_infos = self.pour(action[1], action[2], action[3])
            ola_info['length'] = 3
        elif action[0] == 'PutOn':
            success, mp_infos = self.put_on(action[1], action[2], action[3])
            ola_info['length'] = 4
        elif action[0] == 'Chop':
            success, mp_infos = self.chop(action[1]) ## tool
            ola_info['length'] = 6
        elif action[0] == 'Spread':
            success, mp_infos = self.spread(action[1], action[2]) ## tool
            ola_info['length'] = 6
        elif action[0] == 'Stir':
            success, mp_infos = self.stir(action[1], action[2]) ## tool
            ola_info['length'] = 7
        elif action[0] == 'Scoop':
            success, mp_infos = self.scoop(action[1], action[2]) ## obj_to, tool
            ola_info['length'] = 7
        elif action[0] == 'Scrape':
            success, mp_infos = self.scrape(action[1], action[2]) ## obj_to, tool
            ola_info['length'] = 5
        elif action[0] == 'Activate':
            success, mp_infos = self.activate(action[1], action[2])
            ola_info['length'] = 0
        else:
            AssertionError("action name is wrong")
        
        # Save info
        ola_info['action'] = action
        ola_info['success'] = success
        ola_info['mp_infos'] = mp_infos
        
        return success, ola_info

    ### Object Level Motion Method Start ###
    def pick_up(self, obj):
        obj_type = self.instance_type[obj]

        mp_infos = []
        
        # Parameter
        pre_dist = 0.1
        post_dist = 0.1 # 0.2
        grasp_size = self.obj_pose_yaml[obj_type]['grasp_size']
        grasp_pose = self.obj_pose_yaml[obj_type]['grasp_pose']
        
        # Move to pre-grasp pose
        obj_pose = self.get_object_pose(obj)
        pre_dist_pose = [0, 0, -pre_dist, 0, 0, 0, 1]
        pre_pose = utils.concatenate_to_pose(obj_pose, grasp_pose, pre_dist_pose)
        temp_plan, mp_info = self.move_to(pre_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Move to grasp pose
        temp_plan, mp_info = self.linear_motion([0, 0, pre_dist], True, "eef")
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()
        
        # Get object hierarchy
        obj_hierarchy = [obj]
        if obj in self.contain_objects.keys():
            obj_hierarchy += copy.deepcopy(self.contain_objects[obj])
        rospy.loginfo("obj_hierarchy = {}".format(obj_hierarchy))
        
        # Grasp target object
        _, mp_info = self.hold_object(obj_hierarchy, grasp_size)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.hand_sync(obj, grasp_size)

        # Change object state
        for obj in obj_hierarchy:
            self.objects['activated'].remove(obj)
            self.objects['attached'].append(obj)

        # Move to post-grasp pose
        temp_plan, mp_info = self.linear_motion([0, 0, post_dist], True)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()
        
        return True, mp_infos

    def place_to_pose(self, obj, obj_to_pose):
        obj_type = self.instance_type[obj]

        mp_infos = []

        # Parameter
        pre_dist = 0.1
        if 'place_pos' in self.obj_pose_yaml[obj_type].keys():
            place_pos = self.obj_pose_yaml[obj_type]['place_pos']
        else:
            place_pos = [0, 0, -self.obj_stl_yaml[obj_type]['thickness'][0]-0.001]
        place_orient = utils.rpy_to_quaternion_list(self.obj_pose_yaml[obj_type]['place_orient'])
        grasp_pose = self.obj_pose_yaml[obj_type]['grasp_pose']
        placement_pose = self.placement_yaml[obj_to_pose]['pose']

        # Move to pre place pose
        pre_dist_pose = [0, 0, pre_dist, 0, 0, 0, 1]
        place_pose = place_pos + place_orient
        place_pose_inv = utils.inv_trans_mat(place_pose)
        pre_pose = utils.concatenate_to_pose(pre_dist_pose, placement_pose, place_pose_inv, grasp_pose)
        temp_plan, mp_info = self.move_to(pre_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Place
        temp_plan, mp_info = self.linear_motion([0, 0, -pre_dist], True)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Get object hierarchy
        obj_hierarchy = copy.deepcopy(self.objects['attached'])
        rospy.loginfo(obj_hierarchy)

        # Release object
        _, mp_info = self.release_object(obj_hierarchy)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.hand_sync(obj, 0.4)
        # self.hand_sync(obj_hierarchy[0], 0.4)
        # Motion Check Service Request
        self.motion_check("Place", [obj], ["None"])
        self.scene_sync()

        # Change object state
        for obj in obj_hierarchy:
            self.objects['activated'].append(obj)
            self.objects['attached'].remove(obj)

        # Post-place pose
        temp_plan, mp_info = self.linear_motion([0, 0, -pre_dist], True, "eef")
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        return True, mp_infos

    def place(self, obj, obj_to, obj_category):
        obj_to_area = self._match_place_to_area(obj_to, obj_category)
        scp = self._select_pose_from_area(obj, obj_to_area)
        # scp = self._select_candidate_pose(obj, obj_to)
        if scp:
            success, mp_infos = self.place_to_pose(obj, scp)
            return True and success, mp_infos
        else:
            return False, []
    
    def put_on(self, obj, obj_to, new_obj='None'):
        obj_type = self.instance_type[obj]
        obj_to_type = self.instance_type[obj_to]

        mp_infos = []

        # Parameter
        pre_dist = 0.05
        place_pose = self._make_place_pose(obj_type)
        grasp_pose = self.obj_pose_yaml[obj_type]['grasp_pose']
        # puton_pos = [0, 0, self.obj_stl_yaml[obj_to_type]['thickness'][1]]
        if 'puton_dist' in self.obj_pose_yaml[obj_to_type].keys():
            puton_dist = self.obj_pose_yaml[obj_to_type]['puton_dist']
        else:
            puton_dist = self.obj_stl_yaml[obj_to_type]['thickness'][1]

        # Move to pre put on pose
        pre_dist_pose = [0, 0, pre_dist, 0, 0, 0, 1]
        puton_pose = self.get_object_pose(obj_to)
        puton_pose.position.z += puton_dist
        puton_pose.orientation = Quaternion(0, 0, 0, 1)
        place_pose_inv = utils.inv_trans_mat(place_pose)        
        pre_pose = utils.concatenate_to_pose(pre_dist_pose, puton_pose, place_pose_inv, grasp_pose)
        temp_plan, mp_info = self.move_to(pre_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Puton
        temp_plan, mp_info = self.linear_motion([0, 0, -pre_dist], True)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos                
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Get object hierarchy
        obj_hierarchy = copy.deepcopy(self.objects['attached'])
        
        # Release object
        _, mp_info = self.release_object(obj_hierarchy)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.hand_sync(obj, 0.4)

        # Drop object
        if obj_to_type == 'bowl' and (not self.unity):
            obj_to_pose = utils.add(pose_to_list(self.get_object_pose(obj_to)), [0, 0, 0.02, 0, 0, 0, 0])
            obj_mesh = STL_PATH+self.obj_stl_yaml[obj_type]['file_name']
            obj_size = self.obj_stl_yaml[obj_type]['scale']
            self.add_object(obj, obj_to_pose, obj_mesh, obj_size)

        # Change object state
        for obj in obj_hierarchy:
            self.objects['activated'].append(obj)
            self.objects['attached'].remove(obj)
        
        # Motion Check Service Request
        self.motion_check("PutOn", [obj], [obj_to])
        self.scene_sync()

        # Reassign self.contains_objects
        place_pose_state, _ = self._update_place_pose_state()
        self.contain_objects = dict()
        for key, val in place_pose_state.items():
            if val and (self.instance_type[val[0]] in ['bowl', 'pot', 'plate', 'pan']):
                self.contain_objects[val[0]] = val[1:]
        rospy.loginfo(self.contain_objects)
        # Recover to original pose
        temp_plan, mp_info = self.linear_motion([0, 0, pre_dist], True)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos
        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Only for Tuna Sandwich
        if (new_obj != 'None') and ('sandwich' in self.objects['deactivated']):
            # Delete objects
            del_objects = []
            rospy.loginfo("*****************")
            # rospy.loginfo(place_pose_state)
            for key, val in place_pose_state.items():
                rospy.loginfo('{} : {}'.format(key, val))
                if val and (val[-1] == obj):
                    del_objects = val
                    rospy.loginfo('del_objects = {}'.format(val))
            
            new_obj_pose = pose_to_list(self.get_object_pose(new_obj))
            obj_to_pose = pose_to_list(self.get_object_pose(obj_to))
            for dobj in del_objects:
                dobj_type = self.instance_type[dobj]
                dobj_mesh = STL_PATH+self.obj_stl_yaml[dobj_type]['file_name']
                dobj_size = self.obj_stl_yaml[dobj_type]['scale']
                self.add_object(dobj, new_obj_pose, dobj_mesh, dobj_size)

            # Add new object
            new_obj_type = self.instance_type[new_obj]
            obj_to_pose[2] = 0.4 + self.obj_stl_yaml[new_obj_type]['thickness'][0]
            new_obj_mesh = STL_PATH+self.obj_stl_yaml[new_obj_type]['file_name']
            new_obj_size = self.obj_stl_yaml[new_obj_type]['scale']
            self.add_object(new_obj, obj_to_pose, new_obj_mesh, new_obj_size)
            self.motion_check("Sandwich", ["None"], ["None"])
            
            # Change object state
            for dobj in del_objects:
                self.objects['activated'].remove(dobj)
                self.objects['deactivated'].append(dobj)
            self.objects['deactivated'].remove(new_obj)
            self.objects['activated'].append(new_obj)
            self.scene_sync()
            
        return True, mp_infos

    def pour(self, obj, obj_to, new_obj):
        obj_type = self.instance_type[obj]
        obj_to_type = self.instance_type[obj_to]

        mp_infos = []
        
        # Parameter
        pour_angle = -2*m.pi/5
        pour_pos = [0, -self.obj_stl_yaml[obj_type]['thickness'][1], sum(self.obj_stl_yaml[obj_to_type]['thickness']) + 0.1]

        # Move to obj_to
        pre_pose = self.get_object_pose(obj_to)
        pre_pose.position.x += pour_pos[0]
        pre_pose.position.y += pour_pos[1]
        pre_pose.position.z += pour_pos[2]
        pre_pose.orientation = self.get_cur_pose().orientation
        temp_plan, mp_info = self.move_to(pre_pose, True)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos                
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()
        
        # Pour
        pour_angle_pose = utils.list_to_pose([0, 0, 0, 0, 0, pour_angle])
        pour_pose = utils.concatenate_to_pose(pre_pose, pour_angle_pose)
        temp_plan, mp_info = self.move_to(pour_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()
        
        # Get pour_obj name
        self.num_of_pour[obj] += 1
        pour_obj = new_obj + '_' + str(self.num_of_pour[obj])
        pour_obj_type = self.instance_type[pour_obj]
        rospy.loginfo(pour_obj)

        # Add pour_obj
        # if not self.unity:
        #     if obj_to == 'bowl':
        #         obj_to_pose = utils.add(pose_to_list(self.get_object_pose(obj_to)), [0, 0, 0.02, 0, 0, 0, 0])
        #     else:
        #         obj_to_pose = utils.add(pose_to_list(self.get_object_pose(obj_to)), [0, 0, 0.01, 0, 0, 0, 0])
        #     pour_obj_mesh = STL_PATH+self.obj_stl_yaml[pour_obj_type]['file_name']
        #     pour_obj_size = self.obj_stl_yaml[pour_obj_type]['scale']
        #     self.add_object(pour_obj, obj_to_pose, pour_obj_mesh, pour_obj_size)
        if not self.unity:
            if obj_to == 'bowl':
                obj_to_pose = utils.add(pose_to_list(self.get_object_pose(obj_to)), [0, 0, 0.02, 0, 0, 0, 0])
                pour_obj_mesh = STL_PATH+self.obj_stl_yaml[pour_obj_type]['file_name']
                pour_obj_size = self.obj_stl_yaml[pour_obj_type]['scale']
                self.add_object(pour_obj, obj_to_pose, pour_obj_mesh, pour_obj_size)

        if obj_to == 'bowl':
            # Change object state
            self.objects['activated'].append(pour_obj)
            self.objects['deactivated'].remove(pour_obj)

        # Motion Check Service Request
        self.motion_check("Pour", [new_obj, pour_obj], [obj_to])
        self.scene_sync()

        # Reassign self.contains_objects
        rospy.loginfo("reassign")
        time.sleep(0.7)
        place_pose_state, _ = self._update_place_pose_state()
        self.contain_objects = dict()
        for key, val in place_pose_state.items():
            if val and (self.instance_type[val[0]] in ['bowl', 'pot', 'plate', 'pan']):
                self.contain_objects[val[0]] = val[1:]
        rospy.loginfo(self.contain_objects)

        # Recover pose
        temp_plan, mp_info = self.move_to(pre_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        return True, mp_infos

    def chop(self, obj, chop_num=2):
        obj_type = self.instance_type[obj]
        cobj_type = 'chopped_'+obj_type

        mp_infos = []

        # Parameter
        pre_dist = 0.1
        use_orient = utils.rpy_to_quaternion(self.obj_pose_yaml['knife']['use_orient'])
        chop_pos = [0, 0, self.obj_stl_yaml[obj_type]['thickness'][1]]
        cut_size = sum(self.obj_stl_yaml[obj_type]['thickness'])

        # Change link
        self.move_group.clear_pose_target('panda_link_ee')
        self.move_group.set_end_effector_link('panda_link_knife')

        # Change to using pose
        initial_pose = self.get_cur_pose()
        use_pose = copy.deepcopy(initial_pose)
        use_pose.orientation = use_orient
        temp_plan, mp_info = self.move_to(use_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()
        
        # Move to obj
        pre_dist_pose = [0, 0, pre_dist, 0, 0, 0, 1]
        chop_pose = self.get_object_pose(obj)
        chop_pose.position.x += chop_pos[0]
        chop_pose.position.y += chop_pos[1]
        chop_pose.position.z += chop_pos[2]
        chop_pose.orientation = use_orient
        tar_pose = utils.concatenate_to_pose(pre_dist_pose, chop_pose)
        temp_plan, mp_info = self.move_to(tar_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Pre-cutting
        temp_plan, mp_info = self.linear_motion([0, 0, -pre_dist], True)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        # Motion Check Service Request
        self.motion_check("Before_Chop", [obj], ["None"])
        self.scene_sync()

        # Cutting
        for i in range(chop_num):        
            temp_plan, mp_info = self.reciprocating_motion('Z', cut_size, False)
            mp_infos.append(mp_info)
            if not mp_info['success']:
                return False, mp_infos
            # Service request to Unity
            self.panda_plan(temp_plan)
        
        ### TEMP ###
        # self.add_object()
        # self.update_object_pose()

        # Change object pose
            # obj_pose = utils.add(pose_to_list(self.get_object_pose(obj)), [0, 0, -0.01, 0, 0, 0, 0])
            # obj_pose = utils.add(pose_to_list(self.get_object_pose(obj))[:3], [0, 0, -0.01])+[0, 0, 0, 1]
        obj_pose = pose_to_list(self.get_object_pose(obj))
        obj_pose[2] -= self.obj_stl_yaml[obj_type]['thickness'][0]
        obj_pose[2] += self.obj_stl_yaml[cobj_type]['thickness'][0]
        obj_pose = obj_pose[:3] + [0, 0, 0, 1]
        obj_mesh = STL_PATH + self.obj_stl_yaml[obj_type]['file_name']
        obj_size = self.obj_stl_yaml[obj_type]['scale']

        cobj_pose = pose_to_list(self.get_object_pose('chopped_'+obj))
        cobj_mesh = STL_PATH + self.obj_stl_yaml[cobj_type]['file_name']
        cobj_size = self.obj_stl_yaml[cobj_type]['scale']

        self.add_object(obj, cobj_pose, obj_mesh, obj_size)
        self.add_object('chopped_'+obj, obj_pose, cobj_mesh, cobj_size)

        # Change object state
        self.objects['activated'].remove(obj)
        self.objects['deactivated'].append(obj)
        self.objects['activated'].append('chopped_'+obj)
        self.objects['deactivated'].remove('chopped_'+obj)

        # Motion Check Service Request        
        self.motion_check("After_Chop", [obj], ["chopped_"+obj])
        self.scene_sync()

        # Recover orientation
        recover_pose = self.get_cur_pose()
        recover_pose.orientation = initial_pose.orientation
        temp_plan, mp_info = self.move_to(recover_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Recover link
        self.move_group.clear_pose_target('panda_link_knife')
        self.move_group.set_end_effector_link('panda_link_ee')

        return True, mp_infos

    def spread(self, obj, obj_to):
        obj_type = self.instance_type[obj]
        obj_to_type = self.instance_type[obj_to]

        mp_infos = []

        # Parameter
        pre_dist = 0.2
        use_orient = utils.rpy_to_quaternion(self.obj_pose_yaml['spreader']['use_orient'])
        spread_dist = 0.04
        spread_pos = [0, -spread_dist/2, self.obj_stl_yaml[obj_to_type]['thickness'][1]]

        # Change link
        self.move_group.clear_pose_target('panda_link_ee')
        self.move_group.set_end_effector_link('panda_link_spreader')
        
        # Change to using pose
        initial_pose = self.get_cur_pose()
        use_pose = copy.deepcopy(initial_pose)
        use_pose.orientation = use_orient
        temp_plan, mp_info = self.move_to(use_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Move to obj
        tar_pose = self.get_object_pose(obj)
        tar_pose.position.z += (self.obj_stl_yaml[obj]['thickness'][1] + 0.1)
        tar_pose.orientation = use_orient
        temp_plan, mp_info = self.move_to(tar_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Ready to spread
        temp_plan, mp_info = self.reciprocating_motion("Z", 0.08)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()
        
        # Move to obj_to
        pre_dist_pose = [0, 0, pre_dist, 0, 0, 0, 1]
        spread_pose = self.get_object_pose(obj_to)
        spread_pose.position.x += spread_pos[0]
        spread_pose.position.y += spread_pos[1]
        spread_pose.position.z += spread_pos[2]
        spread_pose.orientation = use_orient
        pre_pose = utils.concatenate_to_pose(pre_dist_pose, spread_pose)
        temp_plan, mp_info = self.move_to(pre_pose, True)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Spread
        temp_plan, mp_info = self.linear_motion([0, 0, -pre_dist], True)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        # Motion Check Service Request  
        # self.motion_check("Before_Spread", [obj], ["None"])
        self.scene_sync()

        temp_plan, mp_info = self.linear_motion([0, spread_dist, 0], False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        # Motion Check Service Request  
        # self.motion_check("After_Spread", [obj], ["spread_"+obj])
        self.scene_sync()

        temp_plan, mp_info = self.linear_motion([0, 0, pre_dist], False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos    
        # Service request to Unity
        self.panda_plan(temp_plan)

        ### TEMP ###
        # self.add_object()
        # self.update_object_pose()

        # Change object pose
        # if not self.unity:
        # obj_pose = pose_to_list(self.get_object_pose(obj))
        # obj_mesh = STL_PATH + self.obj_stl_yaml[obj_type]['file_name']
        # obj_size = self.obj_stl_yaml[obj_type]['scale']

        # cobj_type = 'spread_'+obj_type
        # cobj_pose = pose_to_list(self.get_object_pose('spread_'+obj))
        # cobj_mesh = STL_PATH + self.obj_stl_yaml[cobj_type]['file_name']
        # cobj_size = self.obj_stl_yaml[cobj_type]['scale']

        # self.add_object(obj, cobj_pose, obj_mesh, obj_size)
        # self.add_object("spread_"+obj, obj_pose, cobj_mesh, cobj_size)

        # Change object state
        # self.objects['activated'].remove(obj)
        # self.objects['deactivated'].append(obj)
        # self.objects['activated'].append('spread_'+obj)
        # self.objects['deactivated'].remove('spread_'+obj)

        # Recover orientation
        recover_pose = self.get_cur_pose()
        recover_pose.orientation = initial_pose.orientation
        temp_plan, mp_info = self.move_to(recover_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()
        
        # Recover link
        self.move_group.clear_pose_target('panda_link_spreader')
        self.move_group.set_end_effector_link('panda_link_ee')

        return True, mp_infos

    def stir(self, obj, new_obj, stir_num=2):
        obj_type = self.instance_type[obj]

        mp_infos = []

        # Parameter
        pre_dist = 0.05
        use_orient = utils.rpy_to_quaternion(self.obj_pose_yaml['spatula']['use_orient'])
        stir_r = 0.05
        stir_pos = [0, 0, self.obj_stl_yaml['bowl']['thickness'][1]-0.02]

        # Change link
        self.move_group.clear_pose_target('panda_link_ee')
        self.move_group.set_end_effector_link('panda_link_spatula')

        # Change to using pose
        initial_pose = self.get_cur_pose()
        use_pose = copy.deepcopy(initial_pose)
        use_pose.orientation = use_orient
        temp_plan, mp_info = self.move_to(use_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Move to obj
        stir_pose = self.get_object_pose(obj)
        stir_pose.position.x += stir_pos[0]
        stir_pose.position.y += stir_pos[1]
        stir_pose.position.z += stir_pos[2]
        stir_pose.orientation = use_orient
        pre_dist_pose = [0, 0, pre_dist, 0, 0, 0, 1]
        pre_pose = utils.concatenate_to_pose(pre_dist_pose, stir_pose)
        temp_plan, mp_info = self.move_to(pre_pose, True)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Stir
        temp_plan, mp_info = self.linear_motion([0, 0, -pre_dist], True)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        for i in range(stir_num):
            temp_plan, mp_info = self.circular_motion('Z', 'CW', stir_r, 0, 360, False)
            mp_infos.append(mp_info)
            if not mp_info['success']:
                return False, mp_infos
            # Service request to Unity
            self.panda_plan(temp_plan)

        ### TEMP ###
        # self.add_object()
        # self.update_object_pose()

        # Change object pose
        # if not self.unity:
        if new_obj in self.objects['deactivated']:
            obj_pose = utils.add(pose_to_list(self.get_object_pose(obj)), [0, 0, 0.02, 0, 0, 0, 0])
            nobj_type = self.instance_type[new_obj]
            nobj_mesh = STL_PATH + self.obj_stl_yaml[nobj_type]['file_name']
            nobj_size = self.obj_stl_yaml[nobj_type]['scale']
            self.add_object(new_obj, obj_pose, nobj_mesh, nobj_size)

            for dobj in self.contain_objects[obj]:
                dobj_type = self.instance_type[dobj]
                dobj_pose = [0, 4, 4, 0, 0, 0, 1]
                dobj_mesh = STL_PATH + self.obj_stl_yaml[dobj_type]['file_name']
                dobj_size = self.obj_stl_yaml[dobj_type]['scale']
                self.add_object(dobj, dobj_pose, dobj_mesh, dobj_size)
            
            # Change object state
            for cobj in self.contain_objects[obj]:
                self.objects['activated'].remove(cobj)
                self.objects['deactivated'].append(cobj)
            self.objects['activated'].append(new_obj)
            self.objects['deactivated'].remove(new_obj)

            # Motion Check Service Request
            self.motion_check("Stir", self.contain_objects[obj], [new_obj])
        self.scene_sync()

        # Recover pose
        temp_plan, mp_info = self.linear_motion([0, 0, pre_dist], True)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Recover orientation
        recover_pose = self.get_cur_pose()
        recover_pose.orientation = initial_pose.orientation
        temp_plan, mp_info = self.move_to(recover_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Recover link
        self.move_group.clear_pose_target('panda_link_spatula')
        self.move_group.set_end_effector_link('panda_link_ee')

        return True, mp_infos

    def scoop(self, obj, obj_to):
        obj_type = self.instance_type[obj]
        obj_to_type = self.instance_type[obj_to]
        
        mp_infos = []

        # Parameter
        use_orient = utils.rpy_to_quaternion(self.obj_pose_yaml['scooper']['use_orient'])
        if "chopped" in obj:
            scoop_pos = [0, 0, self.obj_stl_yaml[obj_type]["thickness"][1]+0.1]
        else:
            scoop_pos = [0, 0, self.obj_stl_yaml['bowl']['thickness'][1]]
        scoop_r = 0.05
        scoop_to_pos = [0, -0.025, self.obj_stl_yaml[obj_to_type]['thickness'][1]+0.1]
        scoop_to_angle = -1*m.pi/10

        # Change link
        self.move_group.clear_pose_target('panda_link_ee')
        self.move_group.set_end_effector_link('panda_link_scooper')

        # # Drop object (delete)
        # obj_pose = utils.pose_to_list(self.get_object_pose(obj))
        # obj_pose[2] -= 0.05
        # self.add_object(obj, obj_pose, STL_PATH+self.obj_stl_yaml[obj]['file_name'], self.obj_stl_yaml[obj_type]['scale'])

        # Change to using pose
        initial_pose = self.get_cur_pose()
        use_pose = copy.deepcopy(initial_pose)
        use_pose.orientation = use_orient
        temp_plan, mp_info = self.move_to(use_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Move to obj
        scoop_pose = self.get_object_pose(obj)
        scoop_pose.orientation = self.get_cur_pose().orientation
        scoop_pose.position.x += scoop_pos[0]
        scoop_pose.position.y += scoop_pos[1]
        scoop_pose.position.z += scoop_pos[2]
        scoop_pose.orientation = use_orient
        temp_plan, mp_info = self.move_to(scoop_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.motion_check("Before_Scoop", [obj], ["None"])
        self.scene_sync()

        # Scoop
        # temp_plan, mp_info = self.circular_motion('Y', 'CW', scoop_r, 90, 180, False)
        # temp_plan, mp_info = self.linear_motion([0, 0, -0.1], True) ## ?
        # temp_plan, mp_info = self.reciprocating_motion('Z', 0.1, False)
        temp_plan, mp_info = self.linear_motion([0, 0, -0.1], True)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        # Motion Check Service Request
        self.motion_check("After_Scoop", [obj], ["None"])
        self.scene_sync()
        # post-scoop
        temp_plan, mp_info = self.linear_motion([0, 0, 0.1], True)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Move to obj_to
        pre_pose = self.get_object_pose(obj_to)
        pre_pose.position.x += scoop_to_pos[0]
        pre_pose.position.y += scoop_to_pos[1]
        pre_pose.position.z += scoop_to_pos[2]
        pre_pose.orientation = initial_pose.orientation
        temp_plan, mp_info = self.move_to(pre_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Scoop to
        scoop_to_angle_pose = utils.list_to_pose([0, 0, 0, 0, scoop_to_angle, 0])
        scoop_to_pose = utils.concatenate_to_pose(pre_pose, scoop_to_angle_pose)
        temp_plan, mp_info = self.move_to(scoop_to_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)

        # Change object pose
        if not self.unity:
            obj_to_pose = utils.add(pose_to_list(self.get_object_pose(obj_to)), [0, 0, 0.015, 0, 0, 0, 0])
            obj_mesh = STL_PATH + self.obj_stl_yaml[obj_type]['file_name']
            obj_size = self.obj_stl_yaml[obj_type]['scale']
            self.add_object(obj, obj_to_pose, obj_mesh, obj_size)
        
        # Motion Check Service Request
        self.motion_check("ScoopOn", [obj], [obj_to])
        self.scene_sync()

        # Recover pose
        temp_plan, mp_info = self.move_to(pre_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Recover orientation
        recover_pose = self.get_cur_pose()
        recover_pose.orientation = initial_pose.orientation
        temp_plan, mp_info = self.move_to(recover_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()
        
        # Recover link
        self.move_group.clear_pose_target('panda_link_scooper')
        self.move_group.set_end_effector_link('panda_link_ee')

        return True, mp_infos

    def scrape(self, obj, obj_to):
        obj_type = self.instance_type[obj]

        # Parameter
        pre_dist = 0.09
        use_orient = utils.rpy_to_quaternion(self.obj_pose_yaml['knife']['use_orient'])
        scrape_pos = [0, -0.04, 0] 
        scrape_to_pos = [0, 0, self.obj_stl_yaml['bowl']['thickness'][1]+0.03]

        mp_infos = []

        # Change link
        self.move_group.clear_pose_target('panda_link_ee')
        self.move_group.set_end_effector_link('panda_link_knife')

        # Change to using pose
        initial_pose = self.get_cur_pose()
        use_pose = copy.deepcopy(initial_pose)
        use_pose.orientation = use_orient
        temp_plan, mp_info = self.move_to(use_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Move to start pose
        scrape_pose = self.get_object_pose(obj)
        scrape_pose.position.x += scrape_pos[0]
        scrape_pose.position.y += scrape_pos[1]
        scrape_pose.position.z += scrape_pos[2]
        scrape_pose.orientation = use_orient
        pre_dist_pose = [0, 0, pre_dist, 0, 0, 0, 1]
        pre_pose = utils.concatenate_to_pose(pre_dist_pose, scrape_pose)
        temp_plan, mp_info = self.move_to(pre_pose, True)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()

        # Scrape
        # temp_plan, mp_info = self.linear_motion('Z', -pre_dist, True)
        temp_plan, mp_info = self.linear_motion([0, 0, -pre_dist], True)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos        
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.motion_check("Before_Scrape", [obj], ["None"])
        self.scene_sync()

        scrape_to_pose = self.get_object_pose(obj_to)
        scrape_to_pose.position.x += scrape_to_pos[0]
        scrape_to_pose.position.y += scrape_to_pos[1]
        scrape_to_pose.position.z += scrape_to_pos[2]
        scrape_to_pose.orientation = use_orient
        dist_x = scrape_to_pose.position.x - pre_pose.position.x
        dist_y = scrape_to_pose.position.y - pre_pose.position.y
        temp_plan, mp_info = self.linear_motion([dist_x, dist_y, 0], False)  # <TEMP> direction + or -
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos                
        # Service request to Unity
        self.panda_plan(temp_plan)

        # Change object pose
        if not self.unity:
            obj_to_pose = utils.add(pose_to_list(self.get_object_pose(obj_to)), [0, 0, 0.03, 0, 0, 0, 0])
            obj_mesh = STL_PATH + self.obj_stl_yaml[obj_type]['file_name']
            obj_size = self.obj_stl_yaml[obj_type]['scale']
            self.add_object(obj, obj_to_pose, obj_mesh, obj_size, "world")
        
        # Motion Check Service Request
        self.motion_check("After_Scrape", [obj], [obj_to])
        self.scene_sync()
        
        # Reassign self.contains_objects
        rospy.loginfo("reassign")
        time.sleep(0.7)
        place_pose_state, _ = self._update_place_pose_state()
        # rospy.loginfo(place_pose_state)
        self.contain_objects = dict()
        for key, val in place_pose_state.items():
            if val and (self.instance_type[val[0]] in ['bowl', 'pot', 'plate', 'pan']):
                self.contain_objects[val[0]] = val[1:]
        rospy.loginfo(self.contain_objects)

        # Recover to initial orientation
        recover_pose = self.get_cur_pose()
        recover_pose.orientation = initial_pose.orientation
        temp_plan, mp_info = self.move_to(recover_pose, False)
        mp_infos.append(mp_info)
        if not mp_info['success']:
            return False, mp_infos                
        # Service request to Unity
        self.panda_plan(temp_plan)
        self.scene_sync()
        
        # Recover link
        self.move_group.clear_pose_target('panda_link_knife')
        self.move_group.set_end_effector_link('panda_link_ee')

        return True, mp_infos

    def activate(self, obj, cooked_obj):
        # obj = 'stove'        
        rospy.loginfo('obj={}, cooked_obj={}'.format(obj, cooked_obj))
        self.motion_check("Activate", [cooked_obj], ["None"])

        ''' Not Assigned
        # Move to activate pose
        obj_pose = self.get_object_pose(obj)
        obj_mat = utils.pose_to_mat(obj_pose)
        
        rel_pose_list = self.obj_pose_yaml[obj]['activate_pose']
        rel_mat = utils.pose_list_to_mat(rel_pose_list)
        tar_mat = np.dot(obj_mat, rel_mat)
        tar_pose = utils.mat_to_pose(tar_mat)
        self.move_to(tar_pose, False)
        
        # Activate Request to Unity
        '''
        mp_infos = []
        return True, mp_infos

    def deactivate(self, obj):
        pass
    
def main():
    # rospy.init_node('object_level_motion', anonymous=True)
    obj_test = ObjectLevelMotion(False)
    sandwich = sample.shrimp_salad

    raw_input('[initialize]')
    obj_test.initialize(sandwich.obj_place)

    raw_input('[task planner]')
    current_state = obj_test.get_current_state()
    sandwich_plan = sandwich.total_action_sequences
    for action_sequences in sandwich_plan:
        for action in action_sequences:
            success = obj_test.run(action)
            current_state = obj_test.get_current_state()
            rospy.loginfo('*'*40)
            rospy.loginfo(current_state)
            rospy.loginfo('*'*40)
            if not success:
                current_state = obj_test.get_current_state()
                rospy.loginfo("replan!!!!!!!!!!")
                exit()


if __name__ == '__main__':
    main()
