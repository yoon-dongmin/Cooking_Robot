#! /usr/bin/env python
from pose_level_motion_get_pose import *
import tf
import sys
import copy
import rospy
import yaml
import math
from math import pi
import numpy as np
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list, list_to_pose


class ObjectLevelMotion(LowLevelMotion):
    def __init__(self, self_play=False):
        LowLevelMotion.__init__(self)

        self.stack_count = 0
        # with open('/home/wng/moveit_ws/src/panda_moveit_function/scripts/object_information.yaml') as f:
            # self.obj_info = yaml.load(f, Loader=yaml.FullLoader)

    def pick_up(self, obj):
        # if object == 'movable':  # <TEMP> object : type of object
        # Move to pre-grasping pose
        obj_pose = self.get_object_pose(obj)
        obj_mat = pose_to_mat(obj_pose)
        rel_pose_list = self.obj_info[obj]['pre_grasp_pose']
        rel_mat = pose_list_to_mat(rel_pose_list)
        tar_mat = np.dot(obj_mat, rel_mat)
        tar_pose = mat_to_pose(tar_mat)
        self.move_to(tar_pose, False)

        # Move to grasping pose
        g_dis = self.obj_info[obj]['grasp_distance']
        g_rel_pose_list = [0, 0, g_dis, 0, 0, 0]
        g_rel_mat = pose_list_to_mat(g_rel_pose_list)
        tar_mat = np.dot(tar_mat, g_rel_mat)
        tar_pose = mat_to_pose(tar_mat)
        self.move_to(tar_pose, True)

        # Grasp target object
        g_size = self.obj_info[obj]['grasp_size']
        self.hold_object(obj, g_size)

        # Post-grasping
        self.linear_motion('Z', 0.1, True)
        # else:
        # print("Wrong Object Type")

    def scoop(self, obj):
        tar_pose = self.get_object_pose(obj)
        tar_pose.orientation = self.get_cur_pose().orientation
        tar_pose.position.z += 0.1
        self.move_to(tar_pose, False)
        
        self.linear_motion("Z", -0.1, False)
        self.linear_motion("Z", 0.1, False)

    def place(self, obj, obj_to):
        # if object == 'movable':  # <TEMP> object : type of object
        # Move to place pose
        obj_h = self.obj_info[obj]['thickness'][0] + self.obj_info[obj]['grasp_offset']
        place_h = self.obj_info[obj_to]['thickness'][1]
        tar_pose = self.get_object_pose(obj_to)

        # Add Candidate place search in future
        tar_pose.position.z = tar_pose.position.z + obj_h + place_h + 0.05
        tar_pose.orientation = self.get_cur_pose().orientation

        self.move_to(tar_pose, True)
        
        self.linear_motion("Z", -0.05, False)
        self.linear_motion("Z", -0.05, False)

        # Release Object
        self.release_object(obj)
        # else:
        #     print("Wrong Object Type")

    def place_(self, obj, obj_to):
        candidate_position = self.obj_info[obj_to]['candidate_1']
        tar_pose = self.get_cur_pose()
        tar_pose.position.x = candidate_position[0]
        tar_pose.position.y = candidate_position[1]
        tar_pose.position.z = candidate_position[2] + \
            self.obj_info[obj]['ref_size'][4]

        self.move_to(tar_pose, False)
        self.release_object(obj)

    def pour(self, obj, obj_to):
        # if object == 'ingredient':  # <TEMP> object : type of object
        # Move to container
        obj_to_pose = self.get_object_pose(obj_to)
        obj_to_mat = pose_to_mat(obj_to_pose)
        rel_pose_list = self.obj_info[obj_to]['pour_pose']
        rel_mat = pose_list_to_mat(rel_pose_list)
        tar_mat = np.dot(obj_to_mat, rel_mat)
        tar_pose = mat_to_pose(tar_mat)
        self.move_to(tar_pose, False)

        # Change orientation
        cur_pose = self.get_cur_pose()
        cur_mat = pose_to_mat(cur_pose)
        rel_ori_mat = pose_to_mat(list_to_pose(
            [0, 0, 0, 0, 0, -3*pi/5]))  # <TEMP> Angle fix or not
        tar_pose = mat_to_pose(np.dot(cur_mat, rel_ori_mat))
        self.move_to(tar_pose, False)

        # Recover to original orientation
        self.move_to(cur_pose, False)

        # else:
        #     print("Wrong Object Type")

    def scrape(self, obj):  # dependent on obj status
        # if object == '':  # <TEMP> object : type of object
        # Move to start pose
        obj_pose = self.get_object_pose(obj)
        obj_mat = pose_to_mat(obj_pose)
        rel_pose_list = self.obj_info[obj]['scrape_start_pose']
        rel_mat = pose_list_to_mat(rel_pose_list)
        tar_mat = np.dot(obj_mat, rel_mat)
        tar_pose = mat_to_pose(tar_mat)
        self.move_to(tar_pose)

        # Move to terminal pose
        scrape_distance = self.obj_info[obj]['scrape_distance']
        self.linear_motion('Y', -scrape_distance, True)  # <TEMP> direction
        # else:
        #     print("Wrong Object Type")

    # def put_in(self, obj, obj_to):
    #     if (object == 'ingredient') & (object == 'tool'):  # <TEMP> object : type of object
    #         # Move to place pose
    #         self.move_to()

    #         # Release object
    #         self.release_object()

    #     else:
    #         print("Wrong Object Type")

    def put_on(self, obj, obj_to):
        # if object == 'ingredient':  # <TEMP> object : type of object
        # Move to place pose
        obj_h = self.obj_info[obj]['thickness'][0] + self.obj_info[obj]['grasp_offset']
        place_h = self.obj_info[obj_to]['thickness'][1]
        tar_pose = self.get_object_pose(obj_to)

        # Add Candidate place search in future
        tar_pose.position.z = tar_pose.position.z + obj_h + place_h + 0.05
        tar_pose.orientation = self.get_cur_pose().orientation

        self.move_to(tar_pose, True)
        
        self.linear_motion("Z", -0.05, False)
        self.linear_motion("Z", -0.05, False)

        # Release Object
        self.release_object(obj)
        # else:
        #     print("Wrong Object Type")

    def spread(self, obj, obj_to):
        pass

    def chop(self, obj, chop_num):
        # if object == 'ingredient':  # <TEMP> object : type of object

        use_ori = self.obj_info['knife']['use_orientation']
        rel_pose_list = [0, 0, self.obj_info[obj]['ref_size']
                         [4]+self.obj_info[obj]['ref_size'][5]+0.1] + use_ori
        rel_pose_mat = pose_to_mat(list_to_pose(rel_pose_list))
        cur_pose = self.get_object_pose('cutting_board')
        cur_mat = pose_to_mat(cur_pose)
        tar_pose = mat_to_pose(np.dot(cur_mat, rel_pose_mat))
        self.move_to(tar_pose, False)

        # Cut
        cut_size = self.obj_info[obj]['ref_size'][4] + \
            self.obj_info[obj]['ref_size'][5]  # <TEMP>
        for i in range(chop_num):
            if i == 0:
                self.linear_motion('Y', -0.18, True)
                self.linear_motion('Z', -0.13, True)

            self.linear_motion('Z', -cut_size, False)
            self.linear_motion('Z', cut_size, False)
        # else:
        #     print("Wrong Object Type")

    def stir(self, obj, stir_num):
        # if object == 'container':  # <TEMP> object : type of object
        # Change to using pose
        use_ori = self.obj_info['spatulas']['use_orientation']
        rel_pose_list = [0, 0, 0.25] + use_ori
        rel_pose_mat = pose_to_mat(list_to_pose(rel_pose_list))
        cur_pose = self.get_object_pose(obj)
        cur_mat = pose_to_mat(cur_pose)
        tar_pose = mat_to_pose(np.dot(cur_mat, rel_pose_mat))
        self.move_to(tar_pose, False)

        # Move to start pose
        self.linear_motion('Z', -0.07, False)
        stir_r = self.obj_info[obj]['stir_radius']

        # Stir
        for i in range(stir_num):
            self.circular_motion('Z', 'CW', stir_r, 360, False)

        # Recover to original pose
        self.linear_motion('Z', 0.07, False)

    def activate(self, obj):
        # if object == 'fixed':  # <TEMP> object : type of object
        # Move to activate pose
        obj_pose = self.get_object_pose(obj)
        obj_mat = pose_to_mat(obj_pose)
        rel_pose_list = self.obj_info[obj]['activate_pose']
        rel_mat = pose_list_to_mat(rel_pose_list)
        tar_mat = np.dot(obj_mat, rel_mat)
        tar_pose = mat_to_pose(tar_mat)
        self.move_to(tar_pose, False)

        # else:
        #     print("Wrong Object Type")

    def deactivate(self, obj):
        pass

    def temp(self):
        print(self.get_cur_pose())


def main():

    objtest = ObjectLevelMotion()
    
    raw_input("start")
    
    # objtest.move_to(list_to_pose([0.8, 0, 0.5, 0, 0, 0]), False)
    # objtest.move_to(list_to_pose([0.5, 0, 0.5, 0, 0, 0]), False)
    # objtest.add_box('box', list_to_pose([0.5, 0, 0.4, 0, 0, 0]), (0.1, 0.1, 0.0001))
    objtest.add_object('temp', list_to_pose(
        [0.6699197, 0.6606096, 0.4149285, 0, 0, 0]), "/home/wng/unity_ws/ROS/src/object_sample/tuna_sandwich.stl", (1, 1, 0.5))
    raw_input("ddd")
    # objtest.add_object('temp_2', list_to_pose([0.5, 0.3, 0.4, 0, 0, 0]), "/home/wng/object_sample/salt.stl", (0.3, 0.3, 0.3))
    # objtest.move_to(list_to_pose([0.51, -0.052, 0.5, -pi/2, pi/2, 0]), False)
    objtest.move_to(list_to_pose([0.6699197, 0.6606096, 0.415+0.03+0.1, pi, 0, pi/2]), False)
    # objtest.linear_motion("Z", -0.05, True)
    raw_input("pose")
    objtest.get_rel_pose('temp')
    objtest.hold_object('temp', 0.038)
    raw_input()
    objtest.release_object('temp')

    # raw_input()
    # obj_pose = objtest.get_object_pose('temp_2')
    # obj_mat = pose_to_mat(obj_pose)
    # rel_pose_list = [
    #   -0.049987797503577847,
    #   1.1161837369683125e-05,
    #   7.1522927820977245e-05,
    #   0.50019299488910507,
    #   0.50005945412085939,
    #   0.49984951629812419,
    #   0.49989796085275967,
    # ]
    # rel_mat = pose_list_to_mat(rel_pose_list)
    # tar_mat = np.dot(obj_mat, rel_mat)
    # tar_pose = mat_to_pose(tar_mat)
    # objtest.move_to(tar_pose, False)
    # objtest.linear_motion("X", 0.05, True)
    # objtest.hold_object('temp_2', 0.021)
    # cur_pos = objtest.get_cur_pose()
    # cur_pos.position.x = 0.5
    # cur_pos.position.y = -0.107
    # cur_pos.position.z = 0.6
    # objtest.move_to(cur_pos, False)
    # objtest.get_rel_pose('temp')
    # raw_input()
    # objtest.release_object('temp_2')

    # print(pose_to_list(objtest.get_cur_pose()))
    # objtest.linear_motion("Z", -0.05, True)
    # objtest.add_box('desk_1', list_to_pose(
    #     [0.7, 0, 0.2, 0, 0, 0]), (0.4, 0.7, 0.4))
    # objtest.add_box('desk_2', list_to_pose(
    #     [0, 0.7, 0.2, 0, 0, 0]), (0.7, 0.4, 0.4))
    # objtest.add_box('desk_3', list_to_pose(
    #     [-0.5, 0.7, 0.37, 0, 0, 0]), (0.3, 0.4, 0.06))
    # objtest.add_object('spatulas', list_to_pose(
    #     [0.5, -0.27, 0.4005, 0, 0, -1.570796]), "/home/wng/object_sample/spatulas.stl", (0.5, 0.5, 0.5))
    # objtest.add_object('knife', list_to_pose(
    #     [0.5, 0.3, 0.4003, -1.570796, 0, 0]), "/home/wng/object_sample/knife.stl", (0.01, 0.01, 0.01))
    # objtest.add_object('bowl', list_to_pose(
    #     [-0.2, 0.6, 0.435, 0, 0, pi/2]), "/home/wng/object_sample/bowl.stl", (0.01, 0.01, 0.01))
    # objtest.add_object('bowl', list_to_pose(
    #     [0.45, 0.0, 0.35, 0, 0, 0]), "/home/wng/object_sample/bowl.stl", (0.01, 0.01, 0.01))
    # objtest.add_object('cutting_board', list_to_pose(
    #     [0.2, 0.6, 0.413, 0, 0, 0]), "/home/wng/object_sample/cuttingboard.stl", (0.01, 0.01, 0.01))
    # objtest.add_object('dish_1', list_to_pose(
    #     [0.8, -0.15, 0.4001, 0, 0, 0]), "/home/wng/object_sample/dish.stl", (0.01, 0.01, 0.01))
    # objtest.add_object('dish_2', list_to_pose(
    #     [0.8, 0.15, 0.4001, 0, 0, 0]), "/home/wng/object_sample/dish.stl", (0.01, 0.01, 0.01))
    # objtest.add_object('potato', list_to_pose(
    #     [0.6, -0.15, 0.400, 1.570796, 0, 0]), "/home/wng/object_sample/potato.stl", (0.002, 0.002, 0.002))
    # objtest.add_object('carrot', list_to_pose(
    #     [0.6, 0.15, 0.400, 1.570796, 0, 0]), "/home/wng/object_sample/carrot.stl", (0.002, 0.002, 0.002))
    # objtest.add_object('carrot', list_to_pose(
    #     [0.4, 0.0, 0.400, 1.570796, 0, 0]), "/home/wng/object_sample/carrot.stl", (0.002, 0.002, 0.002))
    # objtest.add_object('salt', list_to_pose(
    #     [-0.5, 0.52, 0.4, 1.570796, 0, 0]), "/home/wng/object_sample/salt.stl", (0.002, 0.002, 0.002))

    raw_input()
    objtest.pick_up('carrot')

    # objtest.put_on('carrot', 'bowl')

    # objtest.pick_up('potato')

    # objtest.put_on('potato', 'bowl')

    # objtest.pick_up('spatulas')

    # objtest.stir('bowl', 3)

    raw_input()


if __name__ == '__main__':
    main()
