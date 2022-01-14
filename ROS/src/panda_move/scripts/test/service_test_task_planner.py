#!/usr/bin/env python
import time
import rospy
from panda_moveit_function.msg import Action, Predicate
from panda_moveit_function.srv import ActionSequences, ActionSequencesRequest
from panda_moveit_function.srv import NewState, NewStateResponse

is_called = False

def make_action_sequences(path):
    request = ActionSequencesRequest()
    for p in path:
        action = Action()
        action.name = p[0]
        action.params = p[1:]
        request.action_sequences.append(action)
    return request

def get_new_state(req):
    global is_called
    is_called = True
    print("response new state")
    for state in req.new_state:
        print("name", state.name)
        print("params", state.params)
    return NewStateResponse(True)

# ROS init
rospy.init_node('task_planner')
# Service(service)
s = rospy.Service('new_state', NewState, get_new_state)
# Service(client)
rospy.wait_for_service('action_sequences')
action_sequences = rospy.ServiceProxy('action_sequences', ActionSequences)

while True:
    # task plan
    rospy.sleep(3)

    # send action sequence
    # raw_input('send action sequence')
    path = [["pick_up", "bacon"], ["place", "bacon", "table"]]
    try:
        print("try")
        request = make_action_sequences(path)
        resp = action_sequences(request)
        print("Service call: {}".format(resp))
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

    # get current state
    print("Ready to get new_state.")
    # rospy.spin()
    # print("after spin")
    while True:
        rospy.sleep(0.5)
        print(is_called)
        if is_called:
            is_called = False
            break