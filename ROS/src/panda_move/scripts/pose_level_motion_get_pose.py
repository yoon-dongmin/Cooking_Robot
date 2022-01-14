#! /usr/bin/env python
import sys
import copy
import rospy
import numpy as np
import tf
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import math
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list, list_to_pose

# def all_close(goal, actual, tolerance):
#     all_equal = True
#     if type(goal) is list:
#         for index in range(len(goal)):
#             if abs(actual[index]-goal[index]) > tolerance:
#                 return False
#     elif type(goal) is geometry_msgs.msg.PoseStamped:
#         return all_close(goal.pose, actual.pose, tolerance)
#     elif type(goal) is geometry_msgs.msg.Pose:
#         return all_close(pose_to_list(goal), pose_to_list(actual), tolerance)


def position_list(pose):
    pos_list = [pose.position.x, pose.position.y, pose.position.z]
    return pos_list


def orientation_list(pose):
    ori_list = [pose.orientation.x, pose.orientation.y,
                pose.orientation.z, pose.orientation.w]
    return ori_list


def rpy_to_quaternion(pose):
    ori_rpy = tf.transformations.euler_from_quaternion(
        [pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w])
    return ori_rpy


def tf_to_mat(translation, rotation):
    trans_mat = tf.transformations.translation_matrix(translation)
    rot_mat = tf.transformations.quaternion_matrix(rotation)
    pose_mat = tf.transformations.concatenate_matrices(trans_mat, rot_mat)
    return pose_mat


def pose_to_mat(pose):
    pos_list = position_list(pose)
    ori_list = orientation_list(pose)
    pose_mat = tf_to_mat(pos_list, ori_list)
    return pose_mat


def pose_list_to_mat(pose_list):
    trans_mat = tf.transformations.translation_matrix(pose_list[:3])
    rot_mat = tf.transformations.quaternion_matrix(pose_list[3:])
    pose_mat = tf.transformations.concatenate_matrices(trans_mat, rot_mat)
    return pose_mat


def mat_to_pose(pose_mat):
    trans_list = list(tf.transformations.translation_from_matrix(pose_mat))
    rot_list = list(tf.transformations.quaternion_from_matrix(pose_mat))
    pose_list = trans_list + rot_list
    pose = list_to_pose(pose_list)
    return pose


def mat_to_pose_list(pose_mat):
    trans_list = list(tf.transformations.translation_from_matrix(pose_mat))
    rot_list = list(tf.transformations.quaternion_from_matrix(pose_mat))
    pose_list = trans_list + rot_list
    return pose_list


class LowLevelMotion(object):
    def __init__(self):
        super(LowLevelMotion, self).__init__()
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('LowLevelMotion', anonymous=True)
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group_name = "panda_arm"
        self.move_group = moveit_commander.MoveGroupCommander(self.group_name)
        self.move_group.set_planner_id("RRTConnectkConfigDefault")
        # self.move_group.set_planning_time()
        # self.move_group.set_num_planning_attempts()
        # self.move_group.set_max_velocity_scaling_factor()
        # self.move_group.set_max_acceleration_scaling_factor()
        self.move_group.set_end_effector_link('panda_link_ee')
        # Planning Parameter
        self.planning_frame = self.move_group.get_planning_frame()
        self.group_names = self.robot.get_group_names()
        self.eef_link = self.move_group.get_end_effector_link()
        self.grasp_name = "hand"
        self.hand_group = moveit_commander.MoveGroupCommander(self.grasp_name)

    def add_box(self, box_name, box_pose_i, box_size):
        box_pose = geometry_msgs.msg.PoseStamped()
        box_pose.header.frame_id = "panda_link0"
        box_pose.pose = box_pose_i
        self.scene.add_box(box_name, box_pose, size=box_size)

    def add_object(self, object_name, object_pose, object_mesh, object_size):
        obj_pose = geometry_msgs.msg.PoseStamped()
        obj_pose.header.frame_id = "panda_link0"
        obj_pose.pose = object_pose
        self.scene.add_mesh(object_name, obj_pose, object_mesh, object_size)

    def get_object_pose(self, object_name):
        obj_pose = self.scene.get_object_poses([object_name])
        obj_pose = obj_pose.values()[0]
        return obj_pose

    def get_cur_pose(self):
        cur_pose = self.move_group.get_current_pose().pose
        return cur_pose

    def set_orientation_constraint(self, move_group):
        cp = move_group.get_current_pose()
        ce = self.eef_link
        consts = moveit_msgs.msg.Constraints()
        oc = moveit_msgs.msg.OrientationConstraint()
        oc.header.frame_id = cp.header.frame_id
        oc.link_name = ce
        oc.orientation = cp.pose.orientation
        oc.absolute_x_axis_tolerance = 0.01
        oc.absolute_y_axis_tolerance = 0.01
        oc.absolute_z_axis_tolerance = 0.01
        oc.weight = 10
        consts.orientation_constraints = [oc]
        move_group.set_path_constraints(consts)

    def move_to(self, pose_goal, ori_constraint):
        move_group = self.move_group
        if ori_constraint:
            self.set_orientation_constraint(move_group)
        plan = move_group.plan(pose_goal)
        move_group.execute(plan, wait=True)
        if ori_constraint:
            move_group.clear_path_constraints()

    def linear_motion(self, direction, distance, avoid_collision):
        move_group = self.move_group
        waypoints = []
        wpose = move_group.get_current_pose().pose

        if direction == "X":
            wpose.position.x += distance
        elif direction == "Y":
            wpose.position.y += distance
        elif direction == "Z":
            wpose.position.z += distance

        waypoints.append(copy.deepcopy(wpose))
        (plan, fraction) = move_group.compute_cartesian_path(waypoints,
                                                             0.01,
                                                             0.0,
                                                             avoid_collisions=avoid_collision)
        move_group.execute(plan, wait=True)

    def circular_motion(self, normal_direction, direction, radius, angle, avoid_collision):
        move_group = self.move_group
        waypoints = []
        interp_num = 60
        wpose = move_group.get_current_pose().pose

        if normal_direction == "Z":
            circular_center = [wpose.position.x,
                               wpose.position.y, wpose.position.z]
            if direction == "CW":
                for j in range(interp_num):
                    wpose.position.x = circular_center[0] + \
                        radius * math.cos(j*(angle*pi/180)/interp_num)
                    wpose.position.y = circular_center[1] - \
                        radius * math.sin(j*(angle*pi/180)/interp_num)
                    waypoints.append(copy.deepcopy(wpose))
            elif direction == "CCW":
                for j in range(interp_num):
                    wpose.position.x = circular_center[0] + \
                        radius * math.cos(j*(angle*pi/180)/interp_num)
                    wpose.position.y = circular_center[1] + \
                        radius * math.sin(j*(angle*pi/180)/interp_num)
                    waypoints.append(copy.deepcopy(wpose))
            wpose.position.x -= radius
            waypoints.append(copy.deepcopy(wpose))
            (plan, fraction) = move_group.compute_cartesian_path(waypoints,
                                                                 0.01,
                                                                 0.0,
                                                                 avoid_collisions=avoid_collision)
        elif normal_direction == "X":
            circular_center = [wpose.position.x,
                               wpose.position.y, wpose.position.z]
            if direction == "CW":
                for j in range(interp_num):
                    wpose.position.y = circular_center[1] + \
                        radius * math.cos(j*(angle*pi/180)/interp_num)
                    wpose.position.z = circular_center[2] - \
                        radius * math.sin(j*(angle*pi/180)/interp_num)
                    waypoints.append(copy.deepcopy(wpose))
            elif direction == "CCW":
                for j in range(interp_num):
                    wpose.position.y = circular_center[1] + \
                        radius * math.cos(j*(angle*pi/180)/interp_num)
                    wpose.position.z = circular_center[2] + \
                        radius * math.sin(j*(angle*pi/180)/interp_num)
                    waypoints.append(copy.deepcopy(wpose))
            wpose.position.y -= radius
            waypoints.append(copy.deepcopy(wpose))
            (plan, fraction) = move_group.compute_cartesian_path(waypoints,
                                                                 0.01,
                                                                 0.0,
                                                                 avoid_collisions=avoid_collision)
        elif normal_direction == "Y":
            circular_center = [wpose.position.x,
                               wpose.position.y, wpose.position.z]
            if direction == "CW":
                for j in range(interp_num):
                    wpose.position.z = circular_center[2] + \
                        radius * math.cos(j*(angle*pi/180)/interp_num)
                    wpose.position.x = circular_center[0] - \
                        radius * math.sin(j*(angle*pi/180)/interp_num)
                    waypoints.append(copy.deepcopy(wpose))
            elif direction == "CCW":
                for j in range(interp_num):
                    wpose.position.z = circular_center[2] + \
                        radius * math.cos(j*(angle*pi/180)/interp_num)
                    wpose.position.x = circular_center[0] + \
                        radius * math.sin(j*(angle*pi/180)/interp_num)
                    waypoints.append(copy.deepcopy(wpose))
            wpose.position.z -= radius
            waypoints.append(copy.deepcopy(wpose))
            (plan, fraction) = move_group.compute_cartesian_path(waypoints,
                                                                 0.01,
                                                                 0.0,
                                                                 avoid_collisions=avoid_collision)
        move_group.execute(plan, wait=True)

    def hold_object(self, object_name, grasp_size):
        robot = self.robot
        hand_group = self.hand_group
        eef_link = self.eef_link
        touch_links = robot.get_link_names(group=self.grasp_name)
        hand_group.set_joint_value_target([grasp_size, 0])
        hand_group.go()
        hand_group.attach_object(
            object_name, eef_link, touch_links=touch_links)
        self.attach_status = True

    def release_object(self, object_name):
        hand_group = self.hand_group
        hand_group.detach_object(object_name)
        hand_group.set_joint_value_target([0.04, 0])
        hand_group.go()
        self.attach_status = False

    def get_rel_pose(self, object_name):
        listener = tf.TransformListener()
        listener.waitForTransform(
            'rail0', 'panda_link_ee', rospy.Time(0), rospy.Duration(10.0))
        (ef_pose, ef_rot) = listener.lookupTransform(
            'rail0', 'panda_link_ee', rospy.Time(0))
        obj_pose = self.scene.get_object_poses([object_name])
        obj_pose = obj_pose.values()[0]
        ef_tf = tf_to_mat(ef_pose, ef_rot)
        obj_tf = pose_to_mat(obj_pose)
        rel_tf = np.dot(tf.transformations.inverse_matrix(obj_tf), ef_tf)
        rel_pose = mat_to_pose_list(rel_tf)
        print(rel_pose)
        ori_rpy = tf.transformations.euler_from_quaternion(
            [rel_pose[3], rel_pose[4], rel_pose[5], rel_pose[6]])
        print(ori_rpy)