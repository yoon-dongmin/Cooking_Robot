###########################################################
test_file_name = 'test_shrimp_salad_v2.csv'

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
obj_state.append(['cilantro', 'cilantro', ['exist']])
obj_state.append(['mango', 'mango', ['exist']])
obj_state.append(['scallion', 'scallion', ['exist']])
obj_state.append(['shrimp', 'shrimp', ['exist']])
obj_state.append(['banana', 'banana', ['exist']])
obj_state.append(['walnut', 'walnut', ['exist']])
obj_state.append(['salad', 'salad', []]) ###### 

obj_state.append(['black_pepper', 'black_pepper', ['exist']])
obj_state.append(['lemon_juice', 'lemon_juice', ['exist']])
obj_state.append(['olive_oil', 'olive_oil', ['exist']])
obj_state.append(['salt', 'salt', ['exist']])

# ingredient bottle
obj_state.append(['black_pepper_bottle', 'black_pepper_bottle', None])
obj_state.append(['lemon_juice_bottle', 'lemon_juice_bottle', None])
obj_state.append(['olive_oil_bottle', 'olive_oil_bottle', None])
obj_state.append(['salt_bottle', 'salt_bottle', None])

###########################################################
# instance-type-placement-state
obj_place = []

# fixed set
# obj_place.append(['pan', 'pan', 'table1_pan', 'activated'])
# obj_place.append(['pot', 'pot', 'table1_pot', 'activated'])
# obj_place.append(['plate', 'plate', 'table1_plate', 'activated'])
# obj_place.append(['bowl', 'bowl', 'table1_empty_4', 'activated'])
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
# obj_place.append(['cilantro', 'cilantro', 'table1_ing_1', 'activated'])
# obj_place.append(['shrimp', 'shrimp', 'table1_ing_2', 'activated'])
# obj_place.append(['mango', 'mango', 'table1_ing_3', 'activated'])
# obj_place.append(['scallion', 'scallion', 'table1_ing_4', 'activated'])
# obj_place.append(['banana', 'banana', 'table1_ing_5', 'activated'])
# obj_place.append(['walnut', 'walnut', 'table1_ing_6', 'activated'])
obj_place.append(['cilantro', 'cilantro', 'table1_ingredient_area', 'activated'])
obj_place.append(['shrimp', 'shrimp', 'table1_ingredient_area', 'activated'])
obj_place.append(['mango', 'mango', 'table1_ingredient_area', 'activated'])
obj_place.append(['scallion', 'scallion', 'table1_ingredient_area', 'activated'])
obj_place.append(['banana', 'banana', 'table1_ingredient_area', 'activated'])
obj_place.append(['walnut', 'walnut', 'table1_ingredient_area', 'activated'])

obj_place.append(['lemon_juice_bottle', 'lemon_juice_bottle', 'table1_ing_bottle_area', 'activated'])
obj_place.append(['black_pepper_bottle', 'black_pepper_bottle', 'table1_ing_bottle_area', 'activated'])
obj_place.append(['salt_bottle', 'salt_bottle', 'table1_ing_bottle_area', 'activated'])
obj_place.append(['olive_oil_bottle', 'olive_oil_bottle', 'table1_ing_bottle_area', 'activated'])

# for Chop
obj_place.append(['chopped_cilantro', 'chopped_cilantro', 'deactivate', 'deactivated'])
obj_place.append(['chopped_shrimp', 'chopped_shrimp', 'deactivate', 'deactivated'])
obj_place.append(['chopped_mango', 'chopped_mango', 'deactivate', 'deactivated'])
obj_place.append(['chopped_scallion', 'chopped_scallion', 'deactivate', 'deactivated'])
obj_place.append(['chopped_banana', 'chopped_banana', 'deactivate', 'deactivated'])
obj_place.append(['chopped_potato', 'chopped_potato', 'deactivate', 'deactivated'])

# for Spread

# for Pour
obj_place.append(['olive_oil_1', 'olive_oil', 'deactivate', 'deactivated']) 
obj_place.append(['lemon_juice_1', 'lemon_juice', 'deactivate', 'deactivated']) 
obj_place.append(['black_pepper_1', 'black_pepper', 'deactivate', 'deactivated'])
obj_place.append(['salt_1', 'salt', 'deactivate', 'deactivated'])

# for Stir
# obj_place.append(['salad', 'salad', 'deactivate', 'deactivated'])

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
task_plan.append(' -> PickUp/olive_oil_bottle -> Pour/olive_oil_bottle/bowl/olive_oil')
task_plan.append(' -> Place/olive_oil_bottle/table/ing_bottle -> PickUp/lemon_juice_bottle -> Pour/lemon_juice_bottle/bowl/lemon_juice')
task_plan.append(' -> Place/lemon_juice_bottle/table/ing_bottle -> PickUp/cilantro -> Place/cilantro/cutting_board/ingredient -> PickUp/knife -> Chop/cilantro/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/bowl -> Place/bowl/near_cutting_board/dishware -> PickUp/knife -> Scrape/chopped_cilantro/bowl/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/shrimp -> Place/shrimp/cutting_board/ingredient -> PickUp/knife -> Chop/shrimp/knife')
task_plan.append(' -> Scrape/chopped_shrimp/bowl/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/mango -> Place/mango/cutting_board/ingredient -> PickUp/knife -> Chop/mango/knife')
task_plan.append(' -> Scrape/chopped_mango/bowl/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/scallion -> Place/scallion/cutting_board/ingredient -> PickUp/knife -> Chop/scallion/knife')
task_plan.append(' -> Scrape/chopped_scallion/bowl/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/banana -> Place/banana/cutting_board/ingredient -> PickUp/knife -> Chop/banana/knife')
task_plan.append(' -> Scrape/chopped_banana/bowl/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/walnut -> PutOn/walnut/bowl/None')
task_plan.append(' -> PickUp/black_pepper_bottle -> Pour/black_pepper_bottle/bowl/black_pepper')
task_plan.append(' -> Place/black_pepper_bottle/table/ing_bottle -> PickUp/salt_bottle -> Pour/salt_bottle/bowl/salt')
task_plan.append(' -> Place/salt_bottle/table/ing_bottle -> PickUp/spatula -> Stir/bowl/salad/spatula')

###########################################################
# action_sequences
total_action_sequences = []
for result in task_plan:
    action_sequences = [action.split('/') for action in result.split(" -> ") if action]
    total_action_sequences.append(action_sequences)
