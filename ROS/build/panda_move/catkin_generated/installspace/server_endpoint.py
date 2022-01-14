#!/usr/bin/env python2
import rospy
import time
import pyautogui

from ros_tcp_endpoint import TcpServer, RosPublisher, RosSubscriber, RosService, UnityService
from panda_move.srv import Init
from panda_move.srv import Sync
from panda_move.srv import Plan
from panda_move.srv import Hand
from panda_move.srv import MotionCheck
from panda_move.msg import ExecutionCheck


def pressEnter(msg):
    time.sleep(0.5)
    pyautogui.press('enter')
    print("Enter!")

def main():
    ros_node_name = rospy.get_param('/TCP_NODE_NAME', 'TCPServer')
    tcp_server = TcpServer(ros_node_name)
    rospy.init_node(ros_node_name, anonymous=True)

    tcp_server.start({
        # 'SourceDestination': RosPublisher('SourceDestination', PandaMoveitJoints, queue_size=10),
        # 'PandaTrajectory': RosSubscriber('PandaTrajectory', PandaTrajectory, tcp_server),
        # 'panda_moveit': RosService('panda_moveit', Init, tcp_server)
        # 'panda_moveit': UnityService('panda_moveit', Init, tcp_server)
        'init_sync': UnityService('init_sync', Init, tcp_server),
        'scene_sync': UnityService('scene_sync', Sync, tcp_server),
        'panda_plan': UnityService('panda_plan', Plan, tcp_server),
        'hand_sync': UnityService('hand_sync', Hand, tcp_server),
        'motion_check': UnityService('motion_check', MotionCheck, tcp_server),
        'execution_check' : RosSubscriber('execution_check', ExecutionCheck, tcp_server)
        # 'execution_check' : UnityPublisher('execution_check', ExecutionCheck, tcp_server)
    })
    # rospy.init_node("execution_check", anonymous=True)
    rospy.Subscriber("execution_check", ExecutionCheck, pressEnter)
    rospy.spin()


if __name__ == '__main__':
    main()
