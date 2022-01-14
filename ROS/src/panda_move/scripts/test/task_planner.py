#!/usr/bin/env python
import time
import rospy
from panda_moveit_function.msg import Action, Predicate
from panda_moveit_function.srv import ActionSequences, ActionSequencesRequest
from panda_moveit_function.srv import NewState, NewStateResponse

def make_action_sequences(path):
    request = ActionSequencesRequest()
    for p in path:
        action = Action()
        action.name = p[0]
        action.params = p[1:]
        request.action_sequences.append(action)
    return request

def get_new_state(req):
    for state in req.new_state:
        print("name", state.name)
        print("params", state.params)
    return NewStateResponse(True)

# ROS
rospy.init_node('task_planner')
# Service - client
rospy.wait_for_service('action_sequences')
action_sequences = rospy.ServiceProxy('action_sequences', ActionSequences)
# Service - service

# send
path = [["pick_up", "bacon"], ["place", "bacon", "table"]]
try:
    request = make_action_sequences(path)
    resp = action_sequences(request)
    print(resp)
except rospy.ServiceException as e:
    print("Service call failed: %s"%e)

# get trigger
s = rospy.Service('new_state', NewState, get_new_state)
print("before spin")
rospy.spin()
print("after spin")

# send again
try:
    request = make_action_sequences(path)
    resp = action_sequences(request)
    print(resp)
except rospy.ServiceException as e:
    print("Service call failed: %s"%e)