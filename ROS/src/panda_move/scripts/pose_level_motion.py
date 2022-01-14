#! /usr/bin/env python
from sre_constants import SUCCESS
import sys
import copy
import time
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import math as m

import numpy as np
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list, list_to_pose
from tf2_ros import StaticTransformBroadcaster, TransformBroadcaster
from geometry_msgs.msg import TransformStamped, Pose
from visualization_msgs.msg import Marker, MarkerArray
import utils

def pose_to_tf(frame_id, child_frame_id, pose):
    t = TransformStamped()
    t.header.frame_id = frame_id
    t.child_frame_id = child_frame_id
    if isinstance(pose, Pose):
        t.transform.translation.x = pose.position.x
        t.transform.translation.y = pose.position.y
        t.transform.translation.z = pose.position.z
        t.transform.rotation = pose.orientation
    else:
        rospy.logerr("pose is not Pose type")
    return t

# def marker_msg(pose, stamp):
#     marker_ = Marker()
#     marker_.header.frame_id = "/world"
#     marker_.header.stamp = stamp
#     marker_.type = marker_.SPHERE
#     marker_.action = marker_.ADD
#     marker_.pose = pose
#     marker_.scale.x = 0.05
#     marker_.scale.y = 0.05
#     marker_.scale.z = 0.05
#     marker_.color.r = 1
#     marker_.color.g = 0
#     marker_.color.b = 0
#     marker_.color.a = 1
#     return marker_

# def marker_array_msg(waypoints):
#     stamp = rospy.Time.now()
#     marker_array = MarkerArray()
#     marker_array.markers = [marker_msg(pose, stamp) for pose in waypoints]
#     return marker_array

def marker_msg(pose, stamp, i):
    marker_ = Marker()
    marker_.id = i
    marker_.header.frame_id = "/world"
    marker_.header.stamp = stamp
    marker_.type = marker_.SPHERE
    marker_.action = marker_.ADD
    marker_.pose = pose
    marker_.scale.x = 0.05
    marker_.scale.y = 0.05
    marker_.scale.z = 0.05
    marker_.color.r = 1
    marker_.color.g = 0
    marker_.color.b = 0
    marker_.color.a = 1
    return marker_

def marker_array_msg(waypoints):
    stamp = rospy.Time.now()
    marker_array = MarkerArray()
    for i, pose in enumerate(waypoints):
        marker_array.markers.append(marker_msg(pose, stamp, i))
    return marker_array

class PoseLevelMotion(object):
    def __init__(self, self_play=True):
        super(PoseLevelMotion, self).__init__()
        moveit_commander.roscpp_initialize(sys.argv)

        rospy.init_node('PandaMove', anonymous=True)

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
        self.grasp_state = False
        self.hand_group = moveit_commander.MoveGroupCommander(self.grasp_name)

        # Joint
        self.joint = [moveit_commander.RobotCommander.Joint(
            self.robot, 'rail_joint')]
        self.joint.append(moveit_commander.RobotCommander.Joint(
            self.robot, 'panda_joint1'))
        self.joint.append(moveit_commander.RobotCommander.Joint(
            self.robot, 'panda_joint2'))
        self.joint.append(moveit_commander.RobotCommander.Joint(
            self.robot, 'panda_joint3'))
        self.joint.append(moveit_commander.RobotCommander.Joint(
            self.robot, 'panda_joint4'))
        self.joint.append(moveit_commander.RobotCommander.Joint(
            self.robot, 'panda_joint5'))
        self.joint.append(moveit_commander.RobotCommander.Joint(
            self.robot, 'panda_joint6'))
        self.joint.append(moveit_commander.RobotCommander.Joint(
            self.robot, 'panda_joint7'))
        self.joint.append(moveit_commander.RobotCommander.Joint(
            self.robot, 'panda_finger_joint1'))
        self.joint.append(moveit_commander.RobotCommander.Joint(
            self.robot, 'panda_finger_joint2'))

        # Visualization
        self.br = StaticTransformBroadcaster()
        self.marker_array_pub = rospy.Publisher('waypoints', MarkerArray, queue_size=1)

        # 
        self.self_play = self_play

    def add_box(self, box_name, box_pose_i, box_size, frame_id="world"):
        box_pose = geometry_msgs.msg.PoseStamped()
        box_pose.header.frame_id = frame_id
        box_pose.pose = list_to_pose(box_pose_i)
        self.scene.add_box(box_name, box_pose, size=box_size)

    def add_object(self, object_name, object_pose, object_mesh, object_size, frame_id="world"):
        obj_pose = geometry_msgs.msg.PoseStamped()
        obj_pose.header.frame_id = frame_id
        obj_pose.pose = list_to_pose(object_pose)
        self.scene.add_mesh(object_name, obj_pose, object_mesh, object_size)

    def get_cur_pose(self):
        cur_pose = self.move_group.get_current_pose().pose
        return cur_pose

    def get_object_pose(self, object_name):
        try:
            obj_pose = self.scene.get_object_poses([object_name])
            obj_pose = obj_pose.values()[0]        
            return obj_pose
        except Exception as e:
            rospy.logerr('cannot get object pose: '+object_name)
            rospy.logerr(e)
            obj_pose = []
            return obj_pose

    def get_object_poses(self):
        obj_poses = dict()
        co = self.scene.get_objects()
        for key, val in co.items():
            obj_poses[key] = val.mesh_poses[0]
        return obj_poses

    def update_object_pose(self, object_name, object_pose):
        obj_pose = geometry_msgs.msg.PoseStamped()
        obj_pose.header.frame_id = "world"
        obj_pose.pose = object_pose
        self.scene.update_pose(object_name, obj_pose)

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
        mp_info = dict()
        planning_time = 0
        execution_time = 0
        success = False
        traj_length = 0

        move_group = self.move_group

        # visualize
        self.br.sendTransform(pose_to_tf('world', 'target_pose', pose_goal))

        # orientation constraint
        if ori_constraint:
            self.set_orientation_constraint(move_group)
        else:
            move_group.clear_path_constraints()
        
        # plan
        start = time.time()
        plan = move_group.plan(pose_goal)
        planning_time = time.time() - start
        traj_length = len(plan.joint_trajectory.points)

        if self.self_play:
            rospy.loginfo('move_to: {}'.format(traj_length))
        else:
            raw_input('move_to: {}'.format(traj_length))

        # retime trajectory
        cur_state = move_group.get_current_state()
        plan = move_group.retime_trajectory(cur_state, plan, 2.0, 1.0)

        # execute
        start = time.time()
        move_group.execute(plan, wait=True)
        execution_time = time.time() - start
        
        if ori_constraint:
            move_group.clear_path_constraints()

        # info
        mp_info['planning_time'] = planning_time
        mp_info['execution_time'] = execution_time
        mp_info['trajectory_length'] = traj_length
        mp_info['target_pose'] = utils.pose_to_list(pose_goal)
        mp_info['success'] = True if traj_length>0 else False

        return plan, mp_info
    
    def linear_motion(self, distance, avoid_collision=True, reference="world"):
        move_group = self.move_group
        waypoints = []
        wpose = move_group.get_current_pose().pose

        if reference == "world":
            wpose.position.x += distance[0]
            wpose.position.y += distance[1]
            wpose.position.z += distance[2]
        elif reference == "eef":
            lpose = distance + [0, 0, 0, 1]
            wpose = utils.concatenate_to_pose(wpose, lpose)
        waypoints.append(copy.deepcopy(wpose))

        # Visualize
        self.marker_array_pub.publish(marker_array_msg(waypoints))
        
        # Plan
        start = time.time()
        (plan, fraction) = move_group.compute_cartesian_path(waypoints,
                                                                0.03,
                                                                0.0,
                                                                avoid_collisions=avoid_collision)
        planning_time = time.time() - start
        
        if self.self_play:
            rospy.loginfo('linear_motion: {}'.format(fraction))
        else:
            raw_input('linear_motion: {}'.format(fraction))
        
        # Execute
        start = time.time()
        move_group.execute(plan, wait=True)
        execution_time = time.time() - start

        # info
        mp_info = dict()
        mp_info['planning_time'] = planning_time
        mp_info['execution_time'] = execution_time
        mp_info['fraction'] = fraction
        mp_info['success'] = True if fraction>0 else False

        return plan, mp_info

    def reciprocating_motion(self, direction, distance, avoid_collision=True, reference="world"):
        move_group = self.move_group
        waypoints = []
        wpose = move_group.get_current_pose().pose

        if reference == "world":
            if direction == "X":
                wpose.position.x -= distance
                waypoints.append(copy.deepcopy(wpose))
                wpose.position.x += distance
                waypoints.append(copy.deepcopy(wpose))
            elif direction == "Y":
                wpose.position.y -= distance
                waypoints.append(copy.deepcopy(wpose))
                wpose.position.y += distance
                waypoints.append(copy.deepcopy(wpose))
            elif direction == "Z":
                wpose.position.z -= distance
                waypoints.append(copy.deepcopy(wpose))
                wpose.position.z += distance
                waypoints.append(copy.deepcopy(wpose))

        elif reference == "eef":
            if direction == "X":
                lpose = [-distance, 0, 0, 0, 0, 0, 1]
                wpose = utils.concatenate_to_pose(wpose, lpose)
                waypoints.append(copy.deepcopy(wpose))
                lpose = [distance, 0, 0, 0, 0, 0, 1]
                wpose = utils.concatenate_to_pose(wpose, lpose)
                waypoints.append(copy.deepcopy(wpose))
            elif direction == "Y":
                lpose = [0, -distance, 0, 0, 0, 0, 1]
                wpose = utils.concatenate_to_pose(wpose, lpose)
                waypoints.append(copy.deepcopy(wpose))
                lpose = [0, distance, 0, 0, 0, 0, 1]
                wpose = utils.concatenate_to_pose(wpose, lpose)
                waypoints.append(copy.deepcopy(wpose))
            elif direction == "Z":
                lpose = [0, 0, -distance, 0, 0, 0, 1]
                wpose = utils.concatenate_to_pose(wpose, lpose)
                waypoints.append(copy.deepcopy(wpose))
                lpose = [0, distance, 0, 0, 0, 0, 1]
                wpose = utils.concatenate_to_pose(wpose, lpose)
                waypoints.append(copy.deepcopy(wpose))

        # Plan
        start = time.time()
        (plan, fraction) = move_group.compute_cartesian_path(waypoints,
                                                                0.03,
                                                                0.0,
                                                                avoid_collisions=avoid_collision)
        planning_time = time.time() - start

        # Execute
        start = time.time()
        if self.self_play:
            rospy.loginfo('reciprocating_motion: {}'.format(fraction))
        else:
            raw_input('reciprocating_motion: {}'.format(fraction))
            # rospy.loginfo('reciprocating_motion: {}'.format(fraction))
        execution_time = time.time() - start

        # info
        mp_info = dict()
        mp_info['planning_time'] = planning_time
        mp_info['execution_time'] = execution_time
        mp_info['fraction'] = fraction
        mp_info['success'] = True if fraction>0 else False

        return plan, mp_info

    def circular_motion(self, normal_direction, direction, radius, start_angle, end_angle, avoid_collision):
        move_group = self.move_group
        waypoints = []
        interp_num = 60
        distance_min = 0.02  # Minimum distance per trajectory step
        wpose = move_group.get_current_pose().pose
        circular_center = [wpose.position.x,
                            wpose.position.y, wpose.position.z]

        if normal_direction == "Z":
            if direction == "CW":
                for j in range(interp_num):
                    delta = (j*(end_angle-start_angle))/interp_num
                    wpose.position.x = circular_center[0] + \
                        radius * m.cos((start_angle+delta)*m.pi/180)
                    wpose.position.y = circular_center[1] - \
                        radius * m.sin((start_angle+delta)*m.pi/180)
                    waypoints.append(copy.deepcopy(wpose))
            elif direction == "CCW":
                for j in range(interp_num):
                    delta = (j*(end_angle-start_angle))/interp_num
                    wpose.position.x = circular_center[0] + \
                        radius * m.cos((start_angle+delta)*m.pi/180)
                    wpose.position.y = circular_center[1] + \
                        radius * m.sin((start_angle+delta)*m.pi/180)
                    waypoints.append(copy.deepcopy(wpose))
            wpose.position.x = circular_center[0]
            wpose.position.y = circular_center[1]
            waypoints.append(copy.deepcopy(wpose))

        elif normal_direction == "X":
            if direction == "CW":
                for j in range(interp_num):
                    delta = (j*(end_angle-start_angle))/interp_num
                    wpose.position.y = circular_center[1] + \
                        radius * m.cos((start_angle+delta)*m.pi/180)
                    wpose.position.z = circular_center[2] - \
                        radius * m.sin((start_angle+delta)*m.pi/180)
                    waypoints.append(copy.deepcopy(wpose))
            elif direction == "CCW":
                delta = (j*(end_angle-start_angle))/interp_num
                for j in range(interp_num):
                    wpose.position.y = circular_center[1] + \
                        radius * m.cos((start_angle+delta)*m.pi/180)
                    wpose.position.z = circular_center[2] + \
                        radius * m.sin((start_angle+delta)*m.pi/180)
                    waypoints.append(copy.deepcopy(wpose))
            wpose.position.y = circular_center[1]
            wpose.position.z = circular_center[2]
            waypoints.append(copy.deepcopy(wpose))

        elif normal_direction == "Y":
            if direction == "CW":
                for j in range(interp_num):
                    delta = (j*(end_angle-start_angle))/interp_num
                    wpose.position.z = circular_center[2] + \
                        radius * m.cos((start_angle+delta)*m.pi/180)
                    wpose.position.x = circular_center[0] - \
                        radius * m.sin((start_angle+delta)*m.pi/180)
                    waypoints.append(copy.deepcopy(wpose))
            elif direction == "CCW":
                for j in range(interp_num):
                    delta = (j*(end_angle-start_angle))/interp_num
                    wpose.position.z = circular_center[2] + \
                        radius * m.cos((start_angle+delta)*m.pi/180)
                    wpose.position.x = circular_center[0] + \
                        radius * m.sin((start_angle+delta)*m.pi/180)
                    waypoints.append(copy.deepcopy(wpose))
            wpose.position.z = circular_center[2]
            wpose.position.x = circular_center[0]
            waypoints.append(copy.deepcopy(wpose))

        # Visualize
        self.marker_array_pub.publish(marker_array_msg(waypoints))

        # Plan
        start = time.time()
        (plan, fraction) = move_group.compute_cartesian_path(waypoints,
                                                                0.02,
                                                                0.0,
                                                                avoid_collisions=avoid_collision)
        planning_time = time.time() - start

        if self.self_play:
            rospy.loginfo('circular_motion: {}'.format(fraction))
        else:
            raw_input('circular_motion: {}'.format(fraction))

        # Execute
        start = time.time()
        move_group.execute(plan, wait=True)
        execution_time = time.time() - start

        # info
        mp_info = dict()
        mp_info['planning_time'] = planning_time
        mp_info['execution_time'] = execution_time
        mp_info['fraction'] = fraction
        mp_info['success'] = True if fraction>0 else False

        return plan, mp_info

    def hold_object(self, object_list, grasp_size):
        try:
            robot = self.robot
            hand_group = self.hand_group
            eef_link = self.eef_link
            touch_links = robot.get_link_names(group=self.grasp_name)
            hand_group.set_joint_value_target([grasp_size, 0])
            hand_group.go()
            for object_name in object_list:
                hand_group.attach_object(
                    object_name, eef_link, touch_links=touch_links)
                time.sleep(0.1)
            self.grasp_state = True
            hold_status = True

            # info
            mp_info = dict()
            mp_info['planning_time'] = None
            mp_info['execution_time'] = None
            mp_info['success'] = hold_status

            return hold_status, mp_info

        except Exception as e:
            rospy.logerr(e)
            hold_status = False

            # info
            mp_info = dict()
            mp_info['planning_time'] = None
            mp_info['execution_time'] = None
            mp_info['success'] = hold_status

            return hold_status, mp_info

    def release_object(self, object_list):
        try:
            hand_group = self.hand_group
            for object_name in object_list:
                hand_group.detach_object(object_name)
                time.sleep(0.1)
            hand_group.set_joint_value_target([0.04, 0])
            hand_group.go()
            self.grasp_state = False
            release_status = True

            # info
            mp_info = dict()
            mp_info['planning_time'] = None
            mp_info['execution_time'] = None
            mp_info['success'] = release_status

            return release_status, mp_info

        except Exception as e:
            rospy.logerr(e)
            release_status = False

            # info
            mp_info = dict()
            mp_info['planning_time'] = None
            mp_info['execution_time'] = None
            mp_info['success'] = release_status

            return release_status, mp_info

    ### Back Up ###
    def _reciprocating_motion(self, distance, avoid_collision=True):
        try:
            move_group = self.move_group
            waypoints = []
            wpose = move_group.get_current_pose().pose

            wpose.position.z -= distance
            waypoints.append(copy.deepcopy(wpose))
            wpose.position.z += distance
            waypoints.append(copy.deepcopy(wpose))

            (plan, fraction) = move_group.compute_cartesian_path(waypoints,
                                                                 0.03,
                                                                 0.0,
                                                                 avoid_collisions=avoid_collision)
            move_group.execute(plan, wait=True)

            return plan

        except Exception as e:
            rospy.logerr(e)
            plan = []
            return plan

def main():
    pose_test = PoseLevelMotion(False)
    co = pose_test.scene.get_objects()
    rospy.loginfo("collision_objects", co.keys())

    for key, val in co.items():
        rospy.loginfo('['+key+']')
        rospy.loginfo(val.mesh_poses[0])
        rospy.loginfo('-'*10)
if __name__ == '__main__':
    main()