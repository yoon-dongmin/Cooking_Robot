###########################################################
test_file_name = 'test_49_predict2_v2.csv'

###########################################################
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
obj_state.append(['bacon', 'bacon', ['exist']])
obj_state.append(['tomato', 'tomato', ['exist']])
obj_state.append(['ham', 'ham', ['exist']])
obj_state.append(['bread1', 'bread', ['exist']])
obj_state.append(['bread2', 'bread', ['exist']])
obj_state.append(['bread3', 'bread', ['exist']])
obj_state.append(['turkey', 'turkey', ['exist']])
obj_state.append(['cheese', 'cheese', ['exist']])
obj_state.append(['celery', 'celery', ['exist']])
obj_state.append(['sandwich', 'sandwich', []]) ###### 

obj_state.append(['relish', 'relish', ['exist']])

# ingredient bottle
obj_state.append(['relish_bottle', 'relish_bottle', None])

###########################################################
# instance-type-placement-state
obj_place = []

# fixed set
# obj_place.append(['pan', 'pan', 'table1_pan', 'activated'])
# obj_place.append(['pot', 'pot', 'table1_pot', 'activated'])
# obj_place.append(['plate', 'plate', 'table1_plate', 'activated'])
# obj_place.append(['bowl', 'bowl', 'table1_bowl', 'activated'])
# obj_place.append(['spatula', 'spatula', 'table1_spatula', 'activated'])
# obj_place.append(['spreader', 'spreader', 'table1_spreader', 'activated'])
# obj_place.append(['scooper', 'scooper', 'table1_scooper', 'activated'])
# obj_place.append(['knife', 'knife', 'table1_knife', 'activated'])
# obj_place.append(['cutting_board', 'cutting_board', 'table1_cutting_board', None])
obj_place.append(['pan', 'pan', 'table1_cookware_area', 'activated'])
obj_place.append(['pot', 'pot', 'table1_cookware_area', 'activated'])
obj_place.append(['plate', 'plate', 'table1_dishware_area', 'activated'])
obj_place.append(['bowl', 'bowl', 'table1_dishware_area', 'activated'])
obj_place.append(['spatula', 'spatula', 'table1_tool_area', 'activated'])
obj_place.append(['spreader', 'spreader', 'table1_tool_area', 'activated'])
obj_place.append(['scooper', 'scooper', 'table1_tool_area', 'activated'])
obj_place.append(['knife', 'knife', 'table1_tool_area', 'activated'])
obj_place.append(['cutting_board', 'cutting_board', 'table1_cutting_board', None]) ##

# ingredeint set
# obj_place.append(['bacon', 'bacon', 'table1_ing_1', 'activated'])
# obj_place.append(['ham', 'ham', 'table1_ing_3', 'activated'])
# obj_place.append(['bread1', 'bread', 'table1_ing_4', 'activated'])
# obj_place.append(['bread2', 'bread', 'table1_ing_5', 'activated'])
# obj_place.append(['bread3', 'bread', 'table1_ing_6', 'activated'])
# obj_place.append(['turkey', 'turkey', 'table1_ing_7', 'activated'])
# obj_place.append(['cheese', 'cheese', 'table1_ing_8', 'activated'])
# obj_place.append(['lettuce', 'lettuce', 'table1_ing_9', 'activated'])
# obj_place.append(['mayonnaise_bottle', 'mayonnaise_bottle', 'table1_mayonnaise', 'activated'])
obj_place.append(['bacon', 'bacon', 'table1_ingredient_area', 'activated'])
obj_place.append(['ham', 'ham', 'table1_ingredient_area', 'activated'])
obj_place.append(['tomato', 'tomato', 'table1_ingredient_area', 'activated'])
obj_place.append(['bread1', 'bread', 'table1_ingredient_area', 'activated'])
obj_place.append(['bread2', 'bread', 'table1_ingredient_area', 'activated'])
obj_place.append(['bread3', 'bread', 'table1_ingredient_area', 'activated'])
obj_place.append(['turkey', 'turkey', 'table1_ingredient_area', 'activated'])
obj_place.append(['cheese', 'cheese', 'table1_ingredient_area', 'activated'])
obj_place.append(['celery', 'celery', 'table1_ingredient_area', 'activated'])
obj_place.append(['relish_bottle', 'relish_bottle', 'table1_ing_bottle_area', 'activated'])

# for Chop   
obj_place.append(['chopped_tomato', 'chopped_tomato', 'deactivate', 'deactivated'])

# for Spread

# for Pour
obj_place.append(['relish_1', 'relish', 'deactivate', 'deactivated'])
obj_place.append(['relish_2', 'relish', 'deactivate', 'deactivated'])

# for Stir

# for PutOn

###########################################################
# network_output -> goals, using_ings, recipe
goals = []
using_ings = []

goals.append({'cooked_bacon': True})
using_ings.append([{'bacon'}, {}])

recipe = {'sandwich' : ['bread1', 'ham', 'turkey', 'cheese', 'bread2', 'bacon', 'lettuce', 'tomato', 'bread3']}

network_output = (goals, using_ings, recipe)

###########################################################
# task_plan
task_plan = []
task_plan.append(' -> PickUp/pan -> Place/pan/stove/cookware -> PickUp/bacon -> PutOn/bacon/pan/None -> Activate/stove/bacon')
task_plan.append(' -> PickUp/tomato -> Place/tomato/cutting_board/ingredient -> PickUp/knife -> Chop/tomato/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/mayonnaise_bottle -> Pour/mayonnaise_bottle/bread1/mayonnaise')
task_plan.append(' -> Place/mayonnaise_bottle/table/ing_bottle -> PickUp/ham -> PutOn/ham/bread1/None')
task_plan.append(' -> PickUp/turkey -> PutOn/turkey/ham/None')
task_plan.append(' -> PickUp/cheese -> PutOn/cheese/turkey/None')
task_plan.append(' -> PickUp/mayonnaise_bottle -> Pour/mayonnaise_bottle/bread2/mayonnaise')
task_plan.append(' -> Place/mayonnaise_bottle/table/ing_bottle -> PickUp/bread2 -> PutOn/bread2/cheese/None')
task_plan.append(' -> PickUp/bacon -> PutOn/bacon/bread2/None')
task_plan.append(' -> PickUp/lettuce -> PutOn/lettuce/bacon/None')
task_plan.append(' -> PickUp/scooper -> Scoop/chopped_tomato/lettuce/scooper')
task_plan.append(' -> Place/scooper/table/tool -> PickUp/bread3 -> PutOn/bread3/chopped_tomato/sandwich')

###########################################################
# action_sequences
total_action_sequences = []
for result in task_plan:
    action_sequences = [action.split('/') for action in result.split(" -> ") if action]
    total_action_sequences.append(action_sequences)
