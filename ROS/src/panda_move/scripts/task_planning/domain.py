#-*- encoding: utf-8 -*-
from collections import defaultdict
from copy import deepcopy

class StripsDomain:
    def __init__(self, feats_vals, actions):
        """ Planning Problem의 domain definition
        - feats_vals(state space) = {feature:possible values}
        - actions(action space) = set of possible action """
        self.feats_vals = feats_vals
        self.actions = self.get_actions()

class CookingDomain:
    boolean = {True, False}

    def __init__(self, objects, knowledge_base, new_objs=None):
        self.knowledge_base = knowledge_base
        self.new_objs = new_objs
        self.objects = objects

        self.object_sets = self._make_object_sets()
        self.actions = self.get_actions()

    def _make_object_sets(self):
        """ object category에 따른 object set을 반환 """
        kb = self.knowledge_base
        objects = self.objects

        obj_sets = defaultdict(set)
        for instance, type in objects.items():
            if 'ingredient' in kb[type]['isA']:
                obj_sets['ingredients'].add(instance)
            if 'ing_bottle' in kb[type]['isA']:
                obj_sets['ing_bottles'].add(instance)
            if 'container' in kb[type]['isA']:
                obj_sets['containers'].add(instance)
            if 'tool' in kb[type]['isA']:
                obj_sets['tools'].add(instance)
            if 'place' in kb[type]['isA']:
                obj_sets['places'].add(instance)

        return obj_sets

    def get_actions(self):
        """ 전체 action set을 반환 """
        ingredients = self.object_sets['ingredients']
        ing_bottles = self.object_sets['ing_bottles']
        containers = self.object_sets['containers']
        places = self.object_sets['places']
        tools = self.object_sets['tools']

        obj = self.objects
        kb = self.knowledge_base
        new_objs = self.new_objs

        actions = {PickUp([x], obj, kb, new_objs) for x in ingredients|ing_bottles|containers|tools}
        actions.update({Place([x], obj, kb, new_objs) for x in places}) ###
        actions.update({PutIn([x], obj, kb, new_objs) for x in containers})
        actions.update({PutOn([x], obj, kb, new_objs) for x in containers})
        actions.update({PourIn(['bowl'], obj, kb, new_objs)})
        actions.update({PourOn([x], obj, kb, new_objs) for x in ingredients})
        actions.update({Stack([x], obj, kb, new_objs) for x in ingredients})
        actions.update({Spread([x, y], obj, kb, new_objs) for x in ingredients for y in ingredients if x!=y})
        actions.update({Scoop([x, y], obj, kb, new_objs) for x in ingredients for y in ingredients if x!=y})
        actions.update({Scrape([x, 'bowl'], obj, kb, new_objs) for x in ingredients})
        actions.update({Chop([x], obj, kb, new_objs) for x in ingredients})
        actions.update({Stir(['bowl'], obj, kb, new_objs)})    
        actions.update({Activate(['stove'], obj, kb, new_objs)})

        return actions

class Action:
    def __init__(self, param_list, objects, knowledge_base, new_objs, cost=1):
        self.param_list = param_list
        self.objects = objects
        self.kb = knowledge_base
        self.new_objs = new_objs
        self.name = None
        self.cost = cost

    def preconds(self, state_asst):
        """ 현재 state_asst에서 action을 수행할 수 있는지 여부 판단 """
        raise NotImplementedError('preconds')

    def effects(self, state_asst):
        """ 현재 state_asst에서 action을 수행한 이후의 state를 결정 """
        raise NotImplementedError('effects')
    
    def isA(self, obj_name, obj_type):
        """ obj_name이 obj_type에 속하는지 판단 """
        if obj_type in self.kb[self.objects[obj_name]]['isA']:
            return True
        else:
            return False
    
    def hasProperty(self, obj_name, obj_prop):
        """ obj_name이 obj_prop의 property를 가지고 있는지 판단 """
        if obj_prop in self.kb[self.objects[obj_name]]['HasProperty']:
            return True
        else:
            return False
    
    def atLocation(self, obj_name, obj_to_name):
        """ obj_name이 obj_to_name에 place가능 한지 판단 """
        if self.objects[obj_to_name] in self.kb[self.objects[obj_name]]['AtLocation']:
            return True
        else:
            return False

    def Contains(self, obj_name):
        """ obj_name이 contain하고 있는 object를 반환 """
        return self.kb[self.objects[obj_name]]['Contains'][0]
    
    def capableOf(self, obj_name, action_name):
        """ obj_name이 action_name에 대해 수행 가능한지 판단 """
        if action_name in self.kb[self.objects[obj_name]]['CapableOf']:
            return True
        else:
            return False

    def get_objects_with_type(self, type):
        """ type의 category에 속하는 object set을 반환 """
        objs_with_type = set()
        for obj_instance, obj_type in self.objects.items():
            if type in self.kb[obj_type]['isA']:
                objs_with_type.add(obj_instance)
        return objs_with_type       
    
    def set_action_name(self, task_level, object_level):
        """ Action의 이름을 설정 """
        self.name = object_level
    
    def reset(self, param_list):
        """ Action을 초기화 """
        self.name = ""
        self.param_list = param_list
    
    def __repr__(self):
        return self.name



class PickUp(Action):
    def __init__(self, param_list, objects, knowledge_base, new_objs):
        Action.__init__(self, param_list, objects, knowledge_base, new_objs)

    def preconds(self, state_asst):
        """ holding이 None이면서 PickUp하려는 obj가 
        ingredient면 조건부 가능, 그 외에는 무조건 가능 """
        obj = self.param_list[0]

        if state_asst['holding'] == 'None':
            if self.isA(obj, 'ingredient'):
                if not(state_asst['chopped_'+obj]) and self.hasProperty(obj, 'graspable') and state_asst['exist_'+obj]:
                    return True
            else:
                return True

        return False

    def effects(self, state_asst):
        """ PickUp한 후, obj을 holding을 하게되며 
        obj와의 in/on 관계는 제거됨 """
        state_asst = deepcopy(state_asst)
        obj = self.param_list[0]

        # state change
        state_asst['holding'] = obj
        state_asst[obj+'_is_in'] = 'None'
        state_asst[obj+'_is_on'] = 'None'

        # set action name
        task_level = 'pick_up_' + obj
        object_level = 'PickUp/{}'.format(obj)
        self.set_action_name(task_level, object_level)

        return state_asst



class Place(Action):
    def __init__(self, param_list, objects, knowledge_base, new_objs):
        Action.__init__(self, param_list, objects, knowledge_base, new_objs)

    def preconds(self, state_asst):
        """ holding 하고 있는 obj가 place에 Place 가능하면 가능 """
        obj = deepcopy(state_asst['holding'])
        place = self.param_list[0]

        if obj is not 'None':
            if self.atLocation(obj, place):
                return True
        
        return False

    def effects(self, state_asst):
        """ Place 한 후, obj는 place 위에 있고 holding은 None이 됨 """
        state_asst = deepcopy(state_asst)
        obj = deepcopy(state_asst['holding'])
        place = self.param_list[0]
        
        # state change
        state_asst['holding'] = 'None'
        state_asst[obj+'_is_on'] = place
        obj_category = self.kb[self.objects[obj]]['isA'][0]

        # set action name
        task_level = 'place_' + obj + '_on_' + place
        object_level = 'Place/{}/{}/{}'.format(obj, place, obj_category)
        self.set_action_name(task_level, object_level)

        return state_asst



class PutIn(Action):
    def __init__(self, param_list, objects, knowledge_base, new_objs):
        Action.__init__(self, param_list, objects, knowledge_base, new_objs)
    
    def preconds(self, state_asst):
        """ holding하는 obj가 ingredient이면서 깊이가 깊은 container에는 PutIn 가능 """
        obj = deepcopy(state_asst['holding'])
        container = self.param_list[0]

        if obj is not 'None':
            if self.isA(obj, 'ingredient'):
                if (container =='bowl') or (container == 'pot'):
                    return True
        return False

    def effects(self, state_asst):
        """ PutIn을 한 후, ingredient는 container 안에 있고 holding은 None이 됨 """
        state_asst = deepcopy(state_asst)
        obj = deepcopy(state_asst['holding'])
        container = self.param_list[0]

        # state change
        state_asst['holding'] = 'None'
        state_asst[obj+'_is_in'] = container

        # set action name
        task_level = 'put_' + obj + '_in_' + container
        object_level = 'PutOn/{}/{}/None'.format(obj,container)
        self.set_action_name(task_level, object_level)

        return state_asst



class PutOn(Action):
    def __init__(self, param_list, objects, knowledge_base, new_objs):
        Action.__init__(self, param_list, objects, knowledge_base, new_objs)
    
    def preconds(self, state_asst):
        """ holding하는 obj가 ingredient이면서 깊이가 얕은 container에 PutOn 가능 """
        obj = deepcopy(state_asst['holding'])
        container = self.param_list[0]

        if obj is not 'None':
            if self.isA(obj, 'ingredient'):
                if (container =='plate') or (container == 'pan'):
                    return True
        return False

    def effects(self, state_asst):
        """ PutOn을 한 후, ingredient는 container 위에 있고 holding은 None이 됨 """
        state_asst = deepcopy(state_asst)
        obj = deepcopy(state_asst['holding'])
        container = self.param_list[0]

        # state change
        state_asst['holding'] = 'None'
        state_asst[obj+'_is_on'] = container

        # set action name
        task_level = 'put_' + obj + '_on_' + container
        object_level = 'PutOn/{}/{}/None'.format(obj,container)
        self.set_action_name(task_level, object_level)

        return state_asst




class PourIn(Action):
    def __init__(self, param_list, objects, knowledge_base, new_objs):
        Action.__init__(self, param_list, objects, knowledge_base, new_objs)
    
    def preconds(self, state_asst):
        """ holding하는 obj가 ing_bottle이면 PourIn 가능 """
        obj = deepcopy(state_asst['holding'])

        if obj is not 'None':
            if self.isA(obj, 'ing_bottle'):
                return True
        
        return False

    def effects(self, state_asst):
        """ PourIn 한 후, ingredient는 container 안에 있고 holding은 None이 됨 """
        state_asst = deepcopy(state_asst)
        obj = deepcopy(state_asst['holding'])
        bowl = 'bowl'

        # state change
        ing_in_bottle = self.Contains(obj)
        state_asst[ing_in_bottle+'_is_in'] = bowl

        # set action name
        task_level = 'pour_' + obj + '_in_' + bowl
        object_level = 'Pour/{}/{}/{}'.format(obj,bowl,ing_in_bottle)
        self.set_action_name(task_level, object_level)

        return state_asst



class PourOn(Action):
    def __init__(self, param_list, objects, knowledge_base, new_objs):
        Action.__init__(self, param_list, objects, knowledge_base, new_objs)
    
    def preconds(self, state_asst):
        """ holding하는 obj가 ing_bottle이고, 
        ing_bottle 안의 ingredient에 PourOn하는 것이 아니면 가능"""
        obj = deepcopy(state_asst['holding'])
        ingredient = self.param_list[0]

        if obj is not 'None':
            if self.isA(obj, 'ing_bottle'):
                ing_in_bottle = self.Contains(obj)
                if ing_in_bottle != ingredient:
                    return True
        return False

    def effects(self, state_asst):
        """ PourOn 한 후, ing_bottle 안의 ingredient는 
        다른 ingredient 위에 있고 holding은 None이 됨 """
        state_asst = deepcopy(state_asst)
        obj = deepcopy(state_asst['holding'])
        ing = self.param_list[0]

        # state change
        ing_in_bottle = self.Contains(obj)
        state_asst['spread_on_'+ing] = ing_in_bottle

        # rename for motion planner
        re_ing = ing
        if state_asst['chopped_'+ing]:
            re_ing = 'chopped_'+ing

        # set action name
        task_level = 'pour_' + obj + '_on_' + ing
        object_level = 'Pour/{}/{}/{}'.format(obj,re_ing,ing_in_bottle)
        self.set_action_name(task_level, object_level)
        
        return state_asst


class Stack(Action):
    def __init__(self, param_list, objects, knowledge_base, new_objs):
        Action.__init__(self, param_list, objects, knowledge_base, new_objs)
    
    def preconds(self, state_asst):
        """ holding하는 obj가 ing이면 이와 
        다른 ing에는 Stack 가능 """
        obj = deepcopy(state_asst['holding'])
        ing = self.param_list[0]

        if obj is not 'None':
            if self.isA(obj, 'ingredient') and state_asst['exist_'+ing] and (obj != ing):
                if self.hasProperty(obj, 'stackable') and self.hasProperty(ing, 'stackable'): ## check
                    return True
        return False

    def effects(self, state_asst):
        """ Stack을 한 후, holding하던 obj는 ing 위에 있고 holding은 None이 됨 """
        """ sandwich recipe 순서 대로 모든 ing가 쌓여있을 경우 new_ing 'sandwich' 생성 """
        state_asst = deepcopy(state_asst)
        obj = deepcopy(state_asst['holding'])
        ing = self.param_list[0]
        
        # state change
        state_asst['holding'] = 'None'
        state_asst[obj+'_is_on'] = ing

        sandwich = 'None'
        if 'sandwich' in self.new_objs.keys():
            recipe = self.new_objs['sandwich']            
            is_sandwich = all([state_asst[recipe[i]+'_is_on'] == recipe[i-1] for i in range(1, len(recipe))])
            if is_sandwich:
                state_asst['sandwich_is_on'] = state_asst[recipe[0]+'_is_on']
                state_asst['exist_sandwich'] = True
                sandwich = 'sandwich'
                for ing_in_recipe in recipe:
                    state_asst[ing_in_recipe+'_is_on'] = 'None'
                    state_asst['exist_'+ing_in_recipe] = False

        # rename for motion planner
        re_ing = deepcopy(ing)
        if state_asst['chopped_'+ing]:
            re_ing = 'chopped_'+ing

        # set action name
        task_level = 'stack_' + obj + '_on_' + ing
        object_level = 'PutOn/{}/{}/{}'.format(obj, re_ing, sandwich)
        self.set_action_name(task_level, object_level)
        return state_asst



class Spread(Action):
    def __init__(self, param_list, objects, knowledge_base, new_objs):
        Action.__init__(self, param_list, objects, knowledge_base, new_objs)
    
    def preconds(self, state_asst):
        """ holding하는 obj가 spread 가능한 tool이고, ing1이 spreadable하다면 가능 """
        obj = deepcopy(state_asst['holding'])
        ing1 = self.param_list[0]
        ing2 = self.param_list[1]

        if obj is not 'None':
            if self.isA(obj, 'tool') and self.capableOf(obj, 'spread'):
                if self.hasProperty(ing1, 'spreadable'):
                    return True
        return False

    def effects(self, state_asst):
        """ Spread를 한 후, ing1은 ing2 위에 spread됨 """
        state_asst = deepcopy(state_asst)
        obj = deepcopy(state_asst['holding'])
        ing1 = self.param_list[0]
        ing2 = self.param_list[1]
        
        # state change
        state_asst['spread_on_'+ing2] = ing1
        # state_asst[ing1+'_is_on'] = 'None'
        # state_asst['exist_'+ing1] = False

        # set action name
        task_level = 'spread_' + ing1 + '_on_' + ing2
        object_level = 'Spread/{}/{}/{}'.format(ing1, ing2, obj)
        self.set_action_name(task_level, object_level)
        return state_asst



class Scoop(Action):
    def __init__(self, param_list, objects, knowledge_base, new_objs):
        Action.__init__(self, param_list, objects, knowledge_base, new_objs)
    
    def preconds(self, state_asst):
        """ holding 하는 obj가 scoop 가능한 tool이고, ing1이 scoopable이면 가능 """
        obj = deepcopy(state_asst['holding'])
        ing1 = self.param_list[0]
        ing2 = self.param_list[1]

        if obj is not 'None':
            if self.isA(obj, 'tool') and self.capableOf(obj, 'scoop'):
                if self.hasProperty(ing1, 'scoopable') or state_asst['chopped_'+ing1]:
                    return True
        return False

    def effects(self, state_asst):
        """ Scoop을 한 후, ing1는 ing2 위에 있게 됨 """
        state_asst = deepcopy(state_asst)
        obj = deepcopy(state_asst['holding'])
        ing1 = self.param_list[0]
        ing2 = self.param_list[1]

        # state change
        state_asst[ing1+'_is_in'] = 'None'
        state_asst[ing1+'_is_on'] = ing2

        # rename for motion planner
        re_ing1 = ing1
        if state_asst['chopped_'+ing1]:
            re_ing1 = 'chopped_'+ing1            

        # set action name
        task_level = 'scoop_' + ing1 + '_on_' + ing2
        object_level = 'Scoop/{}/{}/{}'.format(re_ing1, ing2, obj)
        self.set_action_name(task_level, object_level)
        return state_asst


class Scrape(Action):
    def __init__(self, param_list, objects, knowledge_base, new_objs):
        Action.__init__(self, param_list, objects, knowledge_base, new_objs)
    
    def preconds(self, state_asst):
        """ holding 하고 있는 obj가 scrape가능한 tool이고, ing는 chopped인 상태면서,
        bowl이 near_cutting_board에 있으면 Scrape 가능 """
        obj = deepcopy(state_asst['holding'])
        ing = self.param_list[0]
        # bowl = self.param_list[1]
        bowl = 'bowl'

        if obj is not 'None':
            if self.isA(obj, 'tool') and self.capableOf(obj, 'scrape'):
                # if state_asst['chopped_'+ing] and state_asst['is_near']:
                if state_asst['chopped_'+ing] and (state_asst[bowl+'_is_on'] == 'near_cutting_board'):
                    return True
        return False

    def effects(self, state_asst):
        """ Scrape을 한 후, ingredient는 bowl 안에 있음 """
        state_asst = deepcopy(state_asst)
        obj = deepcopy(state_asst['holding'])
        ing = self.param_list[0]
        bowl = 'bowl'

        # state change
        state_asst[ing+'_is_on'] = 'None'
        state_asst[ing+'_is_in'] = bowl

        # rename for motion planner
        re_ing = ing
        if state_asst['chopped_'+ing]:
            re_ing = 'chopped_'+ing

        # set action name
        task_level = 'scrape_'+ing+'_in_'+bowl
        object_level = 'Scrape/{}/{}/{}'.format(re_ing, bowl, obj)
        self.set_action_name(task_level, object_level)
        return state_asst


class Chop(Action):
    def __init__(self, param_list, objects, knowledge_base, new_objs):
        Action.__init__(self, param_list, objects, knowledge_base, new_objs)

    def preconds(self, state_asst):
        """ holding하는 obj가 chop가능한 tool이며, 
        ing가 cutting_board 위에 있으면 Chop 가능 """
        obj = deepcopy(state_asst['holding'])
        ing = self.param_list[0]

        if obj is not 'None':
            if self.isA(obj, 'tool') and self.capableOf(obj, 'chop'):
                if state_asst[ing+'_is_on'] == 'cutting_board':
                    return True
        return False

    def effects(self, state_asst):
        """ Chop을 한 후, ing는 chopped 됨 """
        state_asst = deepcopy(state_asst)
        obj = deepcopy(state_asst['holding'])
        ing = self.param_list[0]

        # state change
        state_asst['chopped_'+ing] = True

        # set action name
        task_level = 'chop_' + ing
        object_level = 'Chop/{}/{}'.format(ing, obj)
        self.set_action_name(task_level, object_level)
        return state_asst


class Stir(Action):
    def __init__(self, param_list, objects, knowledge_base, new_objs):
        Action.__init__(self, param_list, objects, knowledge_base, new_objs)
        self.ings_in_bowl = []
        self.new_ing = None

    def preconds(self, state_asst):
        """ holding하는 obj가 stir 가능한 tool이고, 
        bowl 안에 있는 ingredient list가 new_ing recipe의 list와 동일하면 Stir 가능 """
        obj = deepcopy(state_asst['holding'])
        # bowl = self.param_list[0]
        bowl = 'bowl'

        if obj is not 'None':
            if self.isA(obj, 'tool') and self.capableOf(obj, 'stir'):
                # bowl 안에 있는 ingredient를 모음
                ings_in_bowl = []
                for key, value in state_asst.items():
                    if (key[-3:] == '_in') and (value == bowl):
                        ings_in_bowl.append(key[:-6])

                # bowl 안에 있는 ingredient가 recipe와 동일해야 함
                for new_ing, new_ing_comp in self.new_objs.items():
                    if (set(ings_in_bowl) == set(new_ing_comp)):
                        self.ings_in_bowl = ings_in_bowl
                        self.new_ing = new_ing
                        return True
                
        return False

    def effects(self, state_asst):
        """ Stir을 한 후, bowl 안에 있는 ingredient들은 제거되고, new_ing 생성 """
        state_asst = deepcopy(state_asst)
        obj = deepcopy(state_asst['holding'])
        bowl = 'bowl'

        # state change
        # recipe가 존재하면 새로운 ingredient 생성하고
        # 기존의 ingredient는 state 및 존재 제거
        for ing in self.ings_in_bowl:
            state_asst['exist_'+ing] = False
            state_asst[ing+'_is_in'] = 'None'
            state_asst[ing+'_is_on'] = 'None'
            # state_asst['cooked_'+ing] = False
            # state_asst['chopped_'+ing] = False
        new_ing = self.new_ing
        state_asst['exist_'+new_ing] = True
        state_asst[new_ing+'_is_in'] = bowl

        # set action name
        task_level = 'stir_' + bowl
        object_level = 'Stir/{}/{}/{}'.format(bowl, new_ing, obj)
        self.set_action_name(task_level, object_level)

        return state_asst


class Activate(Action):
    def __init__(self, param_list, objects, knowledge_base, new_objs):
        Action.__init__(self, param_list, objects, knowledge_base, new_objs)

    def preconds(self, state_asst):
        """ holding 하는 것이 없으면 Activate 가능 """
        if state_asst['holding'] is 'None':
            return True
        return False

    def effects(self, state_asst):
        """ Activate를 한 후, pan 안에 있는 ingredient들은 모두 cooked """
        state_asst = deepcopy(state_asst)
        stove = self.param_list[0]
        cookware = 'pan'
        ingredients = self.get_objects_with_type('ingredient')

        # state change
        # pan이 stove위에 있으면 pan 안에 있는 ingredient를 모은다
        ing_on_pan = None
        if state_asst[cookware+'_is_on'] == stove:
            for ing in ingredients:
                if state_asst[ing+'_is_on'] == cookware:
                    state_asst['cooked_'+ing] = True
                    ing_on_pan = ing             

        # set action name
        task_level = 'activate_' + stove
        object_level = 'Activate/{}/{}'.format(stove, ing_on_pan)
        self.set_action_name(task_level, object_level)
        
        return state_asst


def in_relation(x):
    return x+'_is_in'


def on_relation(x):
    return x+'_is_on'


def cooked(x):
    return 'cooked_'+x


def chopped(x):
    return 'chopped_'+x


def is_exist(x):
    return 'exist_'+x


def spread(x):
    return 'spread_on_'+x