
boolean = {True, False}
# ==================================
# STRIPS
# ==================================


class Strips:
    def __init__(self, name, preconds, effects, cost=1):
        self.name = name
        self.preconds = preconds
        self.effects = effects
        self.cost = cost

    def __repr__(self):
        return self.name


class StripsDomain:
    def __init__(self, feats_vals, actions):
        self.feats_vals = feats_vals
        self.actions = actions

# ==================================
# Kitchen Env
# ==================================


class Action:
    def __init__(self, param_list, object_kb):
        self.param_list = param_list
        self.obj_type = object_kb.object_type
        self.obj_dict = object_kb.objects_dict
        self.name = None

    def preconds(self, state_asst):
        """ 현재 state_asst에서 action을 수행할 수 있는지 여부 """
        raise NotImplementedError('preconds')

    def effects(self, state_asst):
        """ 현재 state_asst에서 action을 수행한 이후의 state """
        raise NotImplementedError('effects')

    def __repr__(self):
        return self.name


class PickUp(Action):
    def __init__(self, param_list, obj_kb):
        Action.__init__(self, param_list, obj_kb)
        self.name = 'pick_up_' + param_list[0]

    def preconds(self, state_asst):
        """ holding이 None이면서 movable를 PickUp하려고 하면 가능
        만약 movable이 ingredient일 경우 exist해야 PickUp 가능 """
        movable = self.param_list[0]

        is_ingredient = (self.obj_dict[movable] in self.obj_type['ingredient'])

        if state_asst['holding'] == 'None':
            if is_ingredient:
                if state_asst['exist_'+movable] == True:
                    return True
            else:
                return True

        return False

    def effects(self, state_asst):
        """ PickUp한 후, movable을 holding을 하게되며
        movable과의 in/on 관계는 제거됨 """
        movable = self.param_list[0]
        state_asst['holding'] = movable
        state_asst[movable+'_is_in'] = 'None'
        state_asst[movable+'_is_on'] = 'None'
        return state_asst


class Place(Action):
    def __init__(self, param_list, obj_kb):
        Action.__init__(self, param_list, obj_kb)
        self.name = 'place_' + param_list[0] + '_on_' + param_list[1]

    def preconds(self, state_asst):
        """ movable을 holding 하고 있을 때
        movable이 ingredient면 exist 해야만 Place가 가능,
        ingredient가 아니면 무조건 Place 가능 """
        movable = self.param_list[0]
        place = self.param_list[1]

        is_ingredient = (self.obj_dict[movable] in self.obj_type['ingredient'])

        if state_asst['holding'] == movable:
            if is_ingredient:
                if state_asst['exist_'+movable] == True:
                    return True
            else:
                return True
        return False

    def effects(self, state_asst):
        """ Place를 한 후, movable은 place 위에 있고 holding은 None이 됨 """
        movable = self.param_list[0]
        place = self.param_list[1]

        state_asst['holding'] = 'None'
        state_asst[movable+'_is_on'] = place
        return state_asst


class PutIn(Action):
    def __init__(self, param_list, obj_kb):
        Action.__init__(self, param_list, obj_kb)
        self.name = 'put_' + param_list[0] + '_in_' + param_list[1]

    def preconds(self, state_asst):
        """ ingredient를 holding 하고 있으면 container에는 PutIn 가능 """
        ingredient = self.param_list[0]
        container = self.param_list[1]

        if state_asst['holding'] == ingredient:
            return True
        return False

    def effects(self, state_asst):
        """ PutIn를 한 후, ingredient는 container 안에 있고 holding은 None이 됨 """
        ingredient = self.param_list[0]
        container = self.param_list[1]

        state_asst['holding'] = 'None'
        state_asst[ingredient+'_is_in'] = container
        return state_asst


class Chop(Action):
    def __init__(self, param_list, obj_kb):
        Action.__init__(self, param_list, obj_kb)
        self.name = 'chop_' + param_list[0]

    def preconds(self, state_asst):
        """ ingredient가 cutting_board 위에 있고 knife를 들고 있을때 Chop이 가능 """
        ingredient = self.param_list[0]
        fixed = state_asst[ingredient+'_is_on']
        movable = state_asst['holding']

        if fixed == 'cutting_board':
            if movable == 'knife':
                return True
        return False

    def effects(self, state_asst):
        """ Chop을 한 후, ingredient가 chopped 됨 """
        ingredient = self.param_list[0]
        state_asst['chopped_'+ingredient] = True
        return state_asst


class Stir(Action):
    def __init__(self, param_list, obj_kb):
        Action.__init__(self, param_list, obj_kb)
        self.name = 'stir_' + param_list[0]

    def preconds(self, state_asst):
        """ Bowl 안에 ingredient가 두개 이상 있고 stick을 들고 있을때 Stir이 가능 """
        bowl = self.param_list[0]
        num_of_ings = 0

        # bowl 안에 있는 ingredient 갯수를 셈
        for key, value in state_asst.items():
            if (key[-3:] == '_in') and (value == 'bowl'):
                num_of_ings += 1

        if (num_of_ings > 1) and (state_asst['holding'] == 'stick'):
            return True
        else:
            return False

    def effects(self, state_asst):
        """ Stir을 한 후, bowl 안에 있는 ingredient들 조합의 recipe가 존재한다면 
        bowl 안에 있는 ingredient는 모두 제거해주고 새로운 ingredient를 생성 """
        recipe = ['egg', 'mayonnaise', 'egg_with_mayonnaise']
        bowl = 'bowl'
        ings_in_bowl = []

        # bowl 안에 있는 ingredient를 모은다
        for key, value in state_asst.items():
            if (key[-3:] == '_in') and (value == bowl):
                ings_in_bowl.append(key[:-6])

        # recipe가 존재하면 새로운 ingredient 생성하고
        # 기존의 ingredient는 state 및 존재 제거
        if set(ings_in_bowl) == set(recipe[:-1]):
            for ing in ings_in_bowl:
                state_asst['exist_'+ing] = False
                state_asst[ing+'_is_in'] = 'None'
                state_asst[ing+'_is_on'] = 'None'
                state_asst['cooked_'+ing] = False
                state_asst['chopped_'+ing] = False
            new_ing = recipe[-1]
            state_asst['exist_'+new_ing] = True
            state_asst[new_ing+'_is_in'] = bowl

        return state_asst


class PutOn(Action):
    def __init__(self, param_list, obj_kb):
        Action.__init__(self, param_list, obj_kb)
        self.name = 'put_' + param_list[0] + '_on_' + param_list[1]
    
    def preconds(self, state_asst):
        """ ingredient1를 holding 하고 있고 ingredient2가 존재하면 PutOn 가능 """
        ingredient1 = self.param_list[0]
        ingredient2 = self.param_list[1]

        is_ingredient1 = (
            self.obj_dict[ingredient1] in self.obj_type['ingredient'])
        is_ingredient2 = (
            self.obj_dict[ingredient2] in self.obj_type['ingredient'])

        if is_ingredient1 and (state_asst['holding'] == ingredient1) and is_ingredient2 and state_asst['exist_'+ingredient2]:
            return True
        return False

    def effects(self, state_asst):
        """ PutOn를 한 후, ingredient1는 ingredient2 위에 있고 holding은 None이 됨 """
        ingredient1 = self.param_list[0]
        ingredient2 = self.param_list[1]

        state_asst['holding'] = 'None'
        state_asst[ingredient1+'_is_on'] = ingredient2
        return state_asst


class Activate(Action):
    def __init__(self, param_list, obj_kb):
        Action.__init__(self, param_list, obj_kb)
        self.name = 'activate_' + param_list[0]

    def preconds(self, state_asst):
        """ stove는 항상 Activate 가능 """
        stove = self.param_list[0]
        if stove == 'stove':
            return True
        else:
            return False

    def effects(self, state_asst):
        """ Activate를 한 후, pot안에 있는 ingredient들은 모두 cooked """
        stove = self.param_list[0]
        pot = 'pot'
        ing_in_pot = []

        # pot이 stove위에 있으면 pot 안에 있는 ingredient를 모은다
        if state_asst[pot+'_is_on'] == stove:
            for key, value in state_asst.items():
                if (key[-3:] == '_in') and (value == pot):
                    ing_in_pot.append(key[:-6])

        for ing in ing_in_pot:
            state_asst['cooked_'+ing] = True
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


def create_kitchen_domain(obj_kb):
    """
    action space(set)
    state space(dictionary)
    - key = predicate
    - value = set of possible value
    """
    # 타입별 object set들을 얻음
    movables = obj_kb.get_objects('movable')
    ingredients = obj_kb.get_objects('ingredient')
    containers = obj_kb.get_objects('container')
    places = obj_kb.get_objects('place')

    # action space 정의
    feats_vals = {PickUp([x], obj_kb) for x in movables}
    feats_vals.update({Place([x, y], obj_kb)} for x in movables for y in places)
    feats_vals.update({PutIn([x, y], obj_kb)} for x in ingredients for y in containers)
    feats_vals.update({PutOn([x, y], obj_kb)} for x in ingredients for y in ingredients if x!=y)
    feats_vals.update({Stir(['bowl'], obj_kb)})
    feats_vals.update({Chop([x], obj_kb)} for x in ingredients)
    feats_vals.update({Activate(['stove'], obj_kb)})

    # state space 정의
    stmap = {'holding': movables | {'None'}}
    stmap.update({in_relation(x): containers | {'None'} for x in ingredients})
    stmap.update({on_relation(x): places | ingredients | {'None'}
                 for x in ingredients})
    stmap.update({cooked(x): boolean for x in ingredients})
    stmap.update({chopped(x): boolean for x in ingredients})
    stmap.update({is_exist(x): boolean for x in ingredients})

    return StripsDomain(feats_vals, stmap)

# ==================================
# Knowledge Base
# ==================================


class ObjectKB:
    def __init__(self, objects, object_type):
        self.object_type = object_type
        self.objects = objects
        self.leaf_type = objects.keys()
        self.objects_dict = self.make_objects_dict()

    def make_objects_dict(self):
        """ 
        objects를 objects_dict로 변환
        - objects = {type: list of instances}
        - objects_dict = {instance: type}
        """
        obj_keys = []
        obj_values = []
        for key, value in self.objects.items():
            obj_keys.extend([key]*len(value))
            obj_values.extend(value)

        return dict(zip(obj_values, obj_keys))

    def get_objects(self, obj_type):
        """ 
        obj_type 타입의 object set 반환 
        - obj_type이 leaf node 일 경우, objects로 부터 해당 key의 item을 반환
        - leaf node가 아닐 경우, obj_type에 속하는 모든 leaf node 반환
        """
        object_set = set()
        if obj_type in self.objects.keys():
            object_set |= set(self.objects[obj_type])
        else:
            for child in self.object_type[obj_type]:
                object_set |= set(self.objects[child])

        return object_set

# ==================================
# Main
# ==================================


def test():
    objects = {'ing': ['egg', 'bread1', 'bread2', 'mayonnaise'],
               'new_ing': ['egg_with_mayonnaise', 'sandwich'],
               'tool': ['stick', 'knife'],
               'container': ['bowl', 'pot'],
               'place': ['cutting_board', 'stove', 'table']}
    object_type = {'ingredient': ['ing', 'new_ing'],
                   'movable': ['ing', 'new_ing', 'tool', 'container'],
                   'fixed': ['place'],
                   'object': ['ing', 'new_ing', 'tool', 'container', 'place']}
    object_kb = ObjectKB(objects, object_type)
    kitchen_dom = create_kitchen_domain(object_kb)

    def run_action(state, action):
        next_state = None
        if action.preconds(state):
            next_state = action.effects(state)
        print('*{} -> {}'.format(action, next_state))
        return next_state

    # test1 = cook egg
    state = {'holding': 'None', 'exist_egg': True,
             'exist_mayonnaise': True, 'exist_bread1': True, 'exist_bread2': True}
    state = run_action(state, PickUp(['egg'], object_kb))
    state = run_action(state, PutIn(['egg', 'pot'], object_kb))
    state = run_action(state, PickUp(['pot'], object_kb))
    state = run_action(state, Place(['pot', 'stove'], object_kb))
    state = run_action(state, Activate(['stove'], object_kb))

    # test2 = chop egg
    state = run_action(state, PickUp(['egg'], object_kb))
    state = run_action(state, Place(['egg', 'cutting_board'], object_kb))
    state = run_action(state, PickUp(['knife'], object_kb))
    state = run_action(state, Chop(['egg'], object_kb))
    state = run_action(state, Place(['knife', 'table'], object_kb))

    # test3 = mix egg with mayo
    state = run_action(state, PickUp(['egg'], object_kb))
    state = run_action(state, PutIn(['egg', 'bowl'], object_kb))
    state = run_action(state, PickUp(['mayonnaise'], object_kb))
    state = run_action(state, PutIn(['mayonnaise', 'bowl'], object_kb))
    state = run_action(state, PickUp(['stick'], object_kb))
    state = run_action(state, Stir(['bowl'], object_kb))
    state = run_action(state, Place(['stick', 'table'], object_kb))

    # test4 = make sandwich
    state = run_action(state, PickUp(['bread1'], object_kb))
    state = run_action(state, Place(['bread1', 'cutting_board'], object_kb))
    state = run_action(state, PickUp(['egg_with_mayonnaise'], object_kb))
    state = run_action(state, PutOn(['egg_with_mayonnaise', 'bread1'], object_kb))
    state = run_action(state, PickUp(['bread2'], object_kb))
    state = run_action(state, PutOn(['bread2', 'egg_with_mayonnaise'], object_kb))


def main():
    kitchen_dom = create_kitchen_domain(object_type, objects_dict)
    initial = {}
    goal = {}
    sandwich = PlanningProblem(kitchen_dom, initial, goal)


# main()
test()
