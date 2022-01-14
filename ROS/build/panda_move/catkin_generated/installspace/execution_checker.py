#!/usr/bin/env python2
import rospy
import pyautogui
from panda_move.msg import ExecutionCheck

def pressEnter(msg):
    pyautogui.press('enter')
    print("Enter!")

def main():
    rospy.init_node("execution_check", anonymous=True)
    rospy.Subscriber("execution_check", ExecutionCheck, pressEnter)
    print("ON")
    rospy.spin()

if __name__ == "__main__":
    main()