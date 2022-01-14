###########################################################
test_file_name = 'test_75_predict_v2.csv'

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
obj_state.append(['onion', 'onion', ['exist']])
obj_state.append(['spinach', 'spinach', ['exist']])
obj_state.append(['green_pepper', 'green_pepper', ['exist']])
obj_state.append(['cheese', 'cheese', ['exist']])
obj_state.append(['oregano', 'oregano', ['exist']])
obj_state.append(['black_olive', 'black_olive', ['exist']])
obj_state.append(['tomato', 'tomato', ['exist']])
obj_state.append(['salad', 'salad', []])


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
obj_place.append(['cutting_board', 'cutting_board', 'table1_cutting_board', None])

# ingredeint set
# obj_place.append(['onion', 'onion', 'table1_ing_1', 'activated'])
# obj_place.append(['cucumber', 'cucumber', 'table1_ing_2', 'activated'])
# obj_place.append(['sweet_pepper', 'sweet_pepper', 'table1_ing_3', 'activated'])
# obj_place.append(['feta_cheese', 'feta_cheese', 'table1_ing_4', 'activated'])
# obj_place.append(['oregano', 'oregano', 'table1_ing_5', 'activated'])
# obj_place.append(['black_olive', 'black_olive', 'table1_ing_6', 'activated'])
# obj_place.append(['tomato', 'tomato', 'table1_ing_7', 'activated'])
# obj_place.append(['potato', 'potato', 'table1_ing_8', 'activated'])
obj_place.append(['onion', 'onion', 'table1_ingredient_area', 'activated'])
obj_place.append(['spinach', 'spinach', 'table1_ingredient_area', 'activated'])
obj_place.append(['green_pepper', 'green_pepper', 'table1_ingredient_area', 'activated'])
obj_place.append(['cheese', 'cheese', 'table1_ingredient_area', 'activated'])
obj_place.append(['oregano', 'oregano', 'table1_ingredient_area', 'activated'])
obj_place.append(['black_olive', 'black_olive', 'table1_ingredient_area', 'activated'])
obj_place.append(['tomato', 'tomato', 'table1_ingredient_area', 'activated'])

# for Chop
obj_place.append(['chopped_onion', 'chopped_onion', 'deactivate', 'deactivated'])
obj_place.append(['chopped_spinach', 'chopped_spinach', 'deactivate', 'deactivated'])
obj_place.append(['chopped_green_pepper', 'chopped_green_pepper', 'deactivate', 'deactivated'])
obj_place.append(['chopped_cheese', 'chopped_cheese', 'deactivate', 'deactivated'])
obj_place.append(['chopped_tomato', 'chopped_tomato', 'deactivate', 'deactivated'])
# for Spread

# for Pour

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
task_plan.append(' -> PickUp/onion -> Place/onion/cutting_board/ingredient -> PickUp/knife -> Chop/onion/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/bowl -> Place/bowl/near_cutting_board/dishware -> PickUp/knife -> Scrape/chopped_onion/bowl/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/cucumber -> Place/cucumber/cutting_board/ingredient -> PickUp/knife -> Chop/cucumber/knife')
task_plan.append(' -> Scrape/chopped_cucumber/bowl/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/sweet_pepper -> Place/sweet_pepper/cutting_board/ingredient -> PickUp/knife -> Chop/sweet_pepper/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/feta_cheese -> Place/feta_cheese/cutting_board/ingredient -> PickUp/knife -> Chop/feta_cheese/knife')
task_plan.append(' -> Scrape/chopped_sweet_pepper/bowl/knife')
task_plan.append(' -> Scrape/chopped_feta_cheese/bowl/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/oregano -> PutOn/oregano/bowl/None')
task_plan.append(' -> PickUp/black_olive -> PutOn/black_olive/bowl/None')
task_plan.append(' -> PickUp/tomato -> Place/tomato/cutting_board/ingredient -> PickUp/knife -> Chop/tomato/knife')
task_plan.append(' -> Scrape/chopped_tomato/bowl/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/potato -> Place/potato/cutting_board/ingredient -> PickUp/knife -> Chop/potato/knife')
task_plan.append(' -> Scrape/chopped_potato/bowl/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/spatula -> Stir/bowl/salad/spatula')

###########################################################
# action_sequences
total_action_sequences = []
for result in task_plan:
    action_sequences = [action.split('/') for action in result.split(" -> ") if action]
    total_action_sequences.append(action_sequences)