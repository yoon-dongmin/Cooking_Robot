#!/usr/bin/env python2
import sys
import rospy
import math as m
import moveit_commander
import moveit_msgs.msg
from moveit_msgs.msg import Constraints, JointConstraint, PositionConstraint, OrientationConstraint, BoundingVolume, RobotState
import geometry_msgs
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list, list_to_pose
from object_level_motion import ObjectLevelMotion
import sample

def main():
    # rospy.init_node('object_level_motion', anonymous=True)
    obj_test = ObjectLevelMotion(True)
    # obj_test = ObjectLevelMotion(False)

    raw_input('[initialize]')
    # sandwich = sample.club_sandwich
    recipe = sample.club_sandwich
    obj_test.initialize(recipe.obj_place)
    raw_input("Init Sync")
    print(obj_test.objects)
    obj_test.init_sync()
    obj_test.scene_sync()

    obj_test.pick_up("tomato")
    obj_test.put_on("tomato", "cutting_board")
    obj_test.pick_up("knife")
    obj_test.chop("tomato")
    obj_test.place("knife", "table")
    obj_test.pick_up("scooper")
    obj_test.scoop("chopped_tomato", "bread1")
    
    raw_input('[task planner]')
    current_state = obj_test.get_current_state()
    recipe = recipe.total_action_sequences
    for action_sequences in recipe:
        for action in action_sequences:
            success = obj_test.run(action)
            if not success:
                current_state = obj_test.get_current_state()
                print("replan!!!!!!!!!!")
                exit()

def rail_test():
    obj_test = ObjectLevelMotion(True)

    raw_input("start")

    raw_input('[initialize]')
    club_sandwich = sample.club_sandwich.obj_place
    obj_test.initialize(club_sandwich)
    raw_input("Init Sync")
    print(obj_test.objects)
    obj_test.init_sync()
    obj_test.scene_sync()
    
    temp_plan = obj_test.pick_up("bread1")

    raw_input("d")

    obj_test.panda_plan(temp_plan)

    raw_input("d")

    temp_plan = obj_test.put_on("bread1", "bread2")

    raw_input("d")

    obj_test.panda_plan(temp_plan)

    # obj_test.panda_plan(plan)

    raw_input("end")

if __name__ == "__main__":
    # rail_test()
    main()