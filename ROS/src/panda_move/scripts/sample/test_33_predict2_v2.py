###########################################################
test_file_name = 'test_33_predict2_v2.csv'

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
# obj_state.append(['butter1', 'butter', ['exist']])
# obj_state.append(['butter2', 'butter', ['exist']])
obj_state.append(['butter', 'butter', ['exist']])
obj_state.append(['cabbage', 'cabbage', ['exist']])
obj_state.append(['bread1', 'bread', ['exist']])
obj_state.append(['bread2', 'bread', ['exist']])
obj_state.append(['tuna', 'tuna', ['exist']])
obj_state.append(['sandwich', 'sandwich', []])
obj_state.append(['tuna_spread', 'tuna_spread', []])

obj_state.append(['salt', 'salt', ['exist']])
obj_state.append(['pepper', 'pepper', ['exist']])
obj_state.append(['mayonnaise', 'mayonnaise', ['exist']])

# ingredient bottle
obj_state.append(['salt_bottle', 'salt_bottle', None])
obj_state.append(['pepper_bottle', 'pepper_bottle', None])
obj_state.append(['mayonnaise_bottle', 'mayonnaise_bottle', None])

###########################################################
# objects-type-placement
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
# obj_place.append(['tuna', 'tuna', 'table1_ing_1', 'activated'])
# obj_place.append(['onion', 'onion', 'table1_ing_2', 'activated'])
# obj_place.append(['butter', 'butter', 'table1_ing_3', 'activated'])
# obj_place.append(['lettuce', 'lettuce', 'table1_ing_9', 'activated'])
# obj_place.append(['bread1', 'bread', 'table1_ing_6', 'activated'])
# obj_place.append(['bread2', 'bread', 'table1_ing_4', 'activated'])
obj_place.append(['tuna', 'tuna', 'table1_ingredient_area', 'activated'])
obj_place.append(['onion', 'onion', 'table1_ingredient_area', 'activated'])
obj_place.append(['butter', 'butter', 'table1_ingredient_area', 'activated'])
# obj_place.append(['butter1', 'butter', 'table1_ingredient_area', 'activated'])
# obj_place.append(['butter2', 'butter', 'table1_ingredient_area', 'activated'])
obj_place.append(['cabbage', 'cabbage', 'table1_ingredient_area', 'activated'])
obj_place.append(['bread1', 'bread', 'table1_ingredient_area', 'activated'])
obj_place.append(['bread2', 'bread', 'table1_ingredient_area', 'activated'])

# obj_place.append(['tuna_can', 'tuna_can', 'table1_sugar', 'activated'])
# obj_place.append(['salt_bottle', 'salt_bottle', 'table1_sugar', 'activated'])
# obj_place.append(['sugar_bottle', 'sugar_bottle', 'table1_salt', 'activated'])
# obj_place.append(['pepper_bottle', 'pepper_bottle', 'table1_pepper', 'activated'])
# obj_place.append(['mayonnaise_bottle', 'mayonnaise_bottle', 'table1_mayonnaise', 'activated'])
obj_place.append(['salt_bottle', 'salt_bottle', 'table1_ing_bottle_area', 'activated'])
obj_place.append(['pepper_bottle', 'pepper_bottle', 'table1_ing_bottle_area', 'activated'])
obj_place.append(['mayonnaise_bottle', 'mayonnaise_bottle', 'table1_ing_bottle_area', 'activated'])

# for Chop                                                                                                                                                     
obj_place.append(['chopped_onion', 'chopped_onion', 'deactivate', 'deactivated'])
obj_place.append(['chopped_tuna', 'chopped_tuna', 'deactivate', 'deactivated'])
obj_place.append(['chopped_sandwich', 'chopped_tuna_sandwich', 'deactivate', 'deactivated'])
obj_place.append(['chopped_cabbage', 'chopped_cabbage', 'deactivate', 'deactivated'])

# for Spread (removed)
# obj_place.append(['spread_butter', 'spread_butter', 'deactivate', 'deactivated'])

# for Pour (removed if poured on)
obj_place.append(['mayonnaise_1', 'mayonnaise', 'deactivate', 'deactivated'])
obj_place.append(['pepper_1', 'pepper', 'deactivate', 'deactivated'])
# obj_place.append(['tuna_1', 'tuna', 'deactivate', 'deactivated'])
obj_place.append(['salt_1', 'salt', 'deactivate', 'deactivated'])

# for Stir
obj_place.append(['tuna_spread', 'tuna_spread', 'deactivate', 'deactivated'])

# for PutOn
obj_place.append(['sandwich', 'tuna_sandwich', 'deactivate', 'deactivated'])

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
task_plan.append(' -> PickUp/tuna -> Place/tuna/cutting_board/ingredient -> PickUp/knife -> Chop/tuna/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/bowl -> Place/bowl/near_cutting_board/dishware -> PickUp/knife -> Scrape/chopped_tuna/bowl/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/mayonnaise_bottle -> Pour/mayonnaise_bottle/bowl/mayonnaise')
task_plan.append(' -> Place/mayonnaise_bottle/table/ing_bottle -> PickUp/onion -> Place/onion/cutting_board/ingredient -> PickUp/knife -> Chop/onion/knife')
task_plan.append(' -> Scrape/chopped_onion/bowl/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/sugar_bottle -> Pour/sugar_bottle/bowl/sugar')
task_plan.append(' -> Place/sugar_bottle/table/ing_bottle -> PickUp/pepper_bottle -> Pour/pepper_bottle/bowl/pepper')
task_plan.append(' -> Place/pepper_bottle/table/ing_bottle -> PickUp/spatula -> Stir/bowl/tuna_spread/spatula')
task_plan.append(' -> Place/spatula/table/tool -> PickUp/butter -> PutOn/butter/bread1/None -> PickUp/spreader -> Spread/butter/bread1/spreader')
task_plan.append(' -> Place/spreader/table/tool -> PickUp/butter -> PutOn/butter/bread2/None -> PickUp/spreader -> Spread/butter/bread2/spreader')
task_plan.append(' -> Place/spreader/table/tool -> PickUp/scooper -> Scoop/tuna_spread/bread1/scooper')
task_plan.append(' -> Place/scooper/table/tool -> PickUp/lettuce -> Place/lettuce/cutting_board/ingredient -> PickUp/knife -> Chop/lettuce/knife')
task_plan.append(' -> Place/knife/table/tool -> PickUp/scooper -> Scoop/chopped_lettuce/tuna_spread/scooper')
task_plan.append(' -> Place/scooper/table/tool -> PickUp/salt_bottle -> Pour/salt_bottle/chopped_lettuce/salt')
task_plan.append(' -> Place/salt_bottle/table/ing_bottle -> PickUp/bread2 -> PutOn/bread2/chopped_lettuce/sandwich')
task_plan.append(' -> PickUp/sandwich -> Place/sandwich/cutting_board/ingredient -> PickUp/knife -> Chop/sandwich/knife')

##########################################################
# action_sequences
total_action_sequences = []
for result in task_plan:
    action_sequences = [action.split('/') for action in result.split(" -> ") if action]
    total_action_sequences.append(action_sequences)