#!/usr/bin/env python
import rospy
from panda_moveit_function.msg import Action, Predicate
from panda_moveit_function.srv import ActionSequences, ActionSequencesResponse
from panda_moveit_function.srv import NewState, NewStateRequest

is_called = False

def get_action_sequences(req):
    global is_called
    is_called = True
    print("response action_sequences")
    for action in req.action_sequences:
        print("name", action.name)
        print("params", action.params)
    return ActionSequencesResponse(True)


def make_new_state(predicates):
    request = NewStateRequest()
    for p in predicates:
        predicate = Predicate()
        predicate.name = p[0]
        predicate.params = p[1:]
        request.new_state.append(predicate)
    return request

# ROS init
rospy.init_node('motion_planner')
# Service(service)
s = rospy.Service('action_sequences', ActionSequences, get_action_sequences)
# Service(client)
rospy.wait_for_service('new_state')
new_state = rospy.ServiceProxy('new_state', NewState)


while True:
    # get action_sequences
    print("Ready to get action_sequences.")
    # rospy.spin()
    # print("after spin")
    while True:
        rospy.sleep(0.5)
        print(is_called)
        if is_called:
            is_called = False
            break

    # motion plan & execute
    rospy.sleep(3)

    # send new_state
    # raw_input('send new_state')
    test_state = [['holding', 'A'], ['on', 'B', 'C'], ['on', 'C', 'D'], ['in', 'E', 'F']]
    try:
        print("try")
        request = make_new_state(test_state)
        resp = new_state(request)
        print("Service call: {}".format(resp))
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)