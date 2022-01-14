# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "panda_move: 3 messages, 7 services")

set(MSG_I_FLAGS "-Ipanda_move:/home/wng/unity_ws/ROS/src/panda_move/msg;-Igeometry_msgs:/home/wng/unity_ws/ROS/src/geometry_msgs/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Imoveit_msgs:/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg;-Imoveit_msgs:/home/wng/unity_ws/ROS/src/moveit_msgs/msg;-Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/melodic/share/actionlib_msgs/cmake/../msg;-Itrajectory_msgs:/opt/ros/melodic/share/trajectory_msgs/cmake/../msg;-Ishape_msgs:/opt/ros/melodic/share/shape_msgs/cmake/../msg;-Iobject_recognition_msgs:/opt/ros/melodic/share/object_recognition_msgs/cmake/../msg;-Ioctomap_msgs:/opt/ros/melodic/share/octomap_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(panda_move_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Sync.srv" NAME_WE)
add_custom_target(_panda_move_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "panda_move" "/home/wng/unity_ws/ROS/src/panda_move/srv/Sync.srv" "geometry_msgs/Quaternion:geometry_msgs/Point"
)

get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg" NAME_WE)
add_custom_target(_panda_move_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "panda_move" "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg" ""
)

get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Init.srv" NAME_WE)
add_custom_target(_panda_move_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "panda_move" "/home/wng/unity_ws/ROS/src/panda_move/srv/Init.srv" "geometry_msgs/Quaternion:geometry_msgs/Point:geometry_msgs/Vector3"
)

get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg" NAME_WE)
add_custom_target(_panda_move_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "panda_move" "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg" ""
)

get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Plan.srv" NAME_WE)
add_custom_target(_panda_move_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "panda_move" "/home/wng/unity_ws/ROS/src/panda_move/srv/Plan.srv" "trajectory_msgs/JointTrajectory:trajectory_msgs/MultiDOFJointTrajectoryPoint:moveit_msgs/RobotTrajectory:trajectory_msgs/MultiDOFJointTrajectory:geometry_msgs/Quaternion:geometry_msgs/Vector3:std_msgs/Header:geometry_msgs/Twist:geometry_msgs/Transform:trajectory_msgs/JointTrajectoryPoint"
)

get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/ExecutionCheck.msg" NAME_WE)
add_custom_target(_panda_move_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "panda_move" "/home/wng/unity_ws/ROS/src/panda_move/msg/ExecutionCheck.msg" ""
)

get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/ActionSequences.srv" NAME_WE)
add_custom_target(_panda_move_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "panda_move" "/home/wng/unity_ws/ROS/src/panda_move/srv/ActionSequences.srv" "panda_move/Action"
)

get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/NewState.srv" NAME_WE)
add_custom_target(_panda_move_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "panda_move" "/home/wng/unity_ws/ROS/src/panda_move/srv/NewState.srv" "panda_move/Predicate"
)

get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/MotionCheck.srv" NAME_WE)
add_custom_target(_panda_move_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "panda_move" "/home/wng/unity_ws/ROS/src/panda_move/srv/MotionCheck.srv" ""
)

get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Hand.srv" NAME_WE)
add_custom_target(_panda_move_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "panda_move" "/home/wng/unity_ws/ROS/src/panda_move/srv/Hand.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/msg/ExecutionCheck.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/panda_move
)
_generate_msg_cpp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/panda_move
)
_generate_msg_cpp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/panda_move
)

### Generating Services
_generate_srv_cpp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Sync.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Quaternion.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/panda_move
)
_generate_srv_cpp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Init.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Quaternion.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Point.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/panda_move
)
_generate_srv_cpp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Plan.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/MultiDOFJointTrajectoryPoint.msg;/home/wng/unity_ws/ROS/src/moveit_msgs/msg/RobotTrajectory.msg;/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/MultiDOFJointTrajectory.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Quaternion.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Vector3.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Twist.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Transform.msg;/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/panda_move
)
_generate_srv_cpp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/ActionSequences.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/panda_move
)
_generate_srv_cpp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/NewState.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/panda_move
)
_generate_srv_cpp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/MotionCheck.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/panda_move
)
_generate_srv_cpp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Hand.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/panda_move
)

### Generating Module File
_generate_module_cpp(panda_move
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/panda_move
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(panda_move_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(panda_move_generate_messages panda_move_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Sync.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_cpp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg" NAME_WE)
add_dependencies(panda_move_generate_messages_cpp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Init.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_cpp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg" NAME_WE)
add_dependencies(panda_move_generate_messages_cpp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Plan.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_cpp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/ExecutionCheck.msg" NAME_WE)
add_dependencies(panda_move_generate_messages_cpp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/ActionSequences.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_cpp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/NewState.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_cpp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/MotionCheck.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_cpp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Hand.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_cpp _panda_move_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(panda_move_gencpp)
add_dependencies(panda_move_gencpp panda_move_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS panda_move_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/msg/ExecutionCheck.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/panda_move
)
_generate_msg_eus(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/panda_move
)
_generate_msg_eus(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/panda_move
)

### Generating Services
_generate_srv_eus(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Sync.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Quaternion.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/panda_move
)
_generate_srv_eus(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Init.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Quaternion.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Point.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/panda_move
)
_generate_srv_eus(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Plan.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/MultiDOFJointTrajectoryPoint.msg;/home/wng/unity_ws/ROS/src/moveit_msgs/msg/RobotTrajectory.msg;/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/MultiDOFJointTrajectory.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Quaternion.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Vector3.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Twist.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Transform.msg;/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/panda_move
)
_generate_srv_eus(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/ActionSequences.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/panda_move
)
_generate_srv_eus(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/NewState.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/panda_move
)
_generate_srv_eus(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/MotionCheck.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/panda_move
)
_generate_srv_eus(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Hand.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/panda_move
)

### Generating Module File
_generate_module_eus(panda_move
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/panda_move
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(panda_move_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(panda_move_generate_messages panda_move_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Sync.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_eus _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg" NAME_WE)
add_dependencies(panda_move_generate_messages_eus _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Init.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_eus _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg" NAME_WE)
add_dependencies(panda_move_generate_messages_eus _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Plan.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_eus _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/ExecutionCheck.msg" NAME_WE)
add_dependencies(panda_move_generate_messages_eus _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/ActionSequences.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_eus _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/NewState.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_eus _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/MotionCheck.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_eus _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Hand.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_eus _panda_move_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(panda_move_geneus)
add_dependencies(panda_move_geneus panda_move_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS panda_move_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/msg/ExecutionCheck.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/panda_move
)
_generate_msg_lisp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/panda_move
)
_generate_msg_lisp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/panda_move
)

### Generating Services
_generate_srv_lisp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Sync.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Quaternion.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/panda_move
)
_generate_srv_lisp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Init.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Quaternion.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Point.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/panda_move
)
_generate_srv_lisp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Plan.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/MultiDOFJointTrajectoryPoint.msg;/home/wng/unity_ws/ROS/src/moveit_msgs/msg/RobotTrajectory.msg;/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/MultiDOFJointTrajectory.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Quaternion.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Vector3.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Twist.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Transform.msg;/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/panda_move
)
_generate_srv_lisp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/ActionSequences.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/panda_move
)
_generate_srv_lisp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/NewState.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/panda_move
)
_generate_srv_lisp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/MotionCheck.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/panda_move
)
_generate_srv_lisp(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Hand.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/panda_move
)

### Generating Module File
_generate_module_lisp(panda_move
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/panda_move
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(panda_move_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(panda_move_generate_messages panda_move_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Sync.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_lisp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg" NAME_WE)
add_dependencies(panda_move_generate_messages_lisp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Init.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_lisp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg" NAME_WE)
add_dependencies(panda_move_generate_messages_lisp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Plan.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_lisp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/ExecutionCheck.msg" NAME_WE)
add_dependencies(panda_move_generate_messages_lisp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/ActionSequences.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_lisp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/NewState.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_lisp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/MotionCheck.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_lisp _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Hand.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_lisp _panda_move_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(panda_move_genlisp)
add_dependencies(panda_move_genlisp panda_move_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS panda_move_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/msg/ExecutionCheck.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/panda_move
)
_generate_msg_nodejs(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/panda_move
)
_generate_msg_nodejs(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/panda_move
)

### Generating Services
_generate_srv_nodejs(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Sync.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Quaternion.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/panda_move
)
_generate_srv_nodejs(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Init.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Quaternion.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Point.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/panda_move
)
_generate_srv_nodejs(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Plan.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/MultiDOFJointTrajectoryPoint.msg;/home/wng/unity_ws/ROS/src/moveit_msgs/msg/RobotTrajectory.msg;/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/MultiDOFJointTrajectory.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Quaternion.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Vector3.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Twist.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Transform.msg;/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/panda_move
)
_generate_srv_nodejs(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/ActionSequences.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/panda_move
)
_generate_srv_nodejs(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/NewState.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/panda_move
)
_generate_srv_nodejs(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/MotionCheck.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/panda_move
)
_generate_srv_nodejs(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Hand.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/panda_move
)

### Generating Module File
_generate_module_nodejs(panda_move
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/panda_move
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(panda_move_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(panda_move_generate_messages panda_move_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Sync.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_nodejs _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg" NAME_WE)
add_dependencies(panda_move_generate_messages_nodejs _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Init.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_nodejs _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg" NAME_WE)
add_dependencies(panda_move_generate_messages_nodejs _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Plan.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_nodejs _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/ExecutionCheck.msg" NAME_WE)
add_dependencies(panda_move_generate_messages_nodejs _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/ActionSequences.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_nodejs _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/NewState.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_nodejs _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/MotionCheck.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_nodejs _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Hand.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_nodejs _panda_move_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(panda_move_gennodejs)
add_dependencies(panda_move_gennodejs panda_move_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS panda_move_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/msg/ExecutionCheck.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/panda_move
)
_generate_msg_py(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/panda_move
)
_generate_msg_py(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/panda_move
)

### Generating Services
_generate_srv_py(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Sync.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Quaternion.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/panda_move
)
_generate_srv_py(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Init.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Quaternion.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Point.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/panda_move
)
_generate_srv_py(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Plan.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/MultiDOFJointTrajectoryPoint.msg;/home/wng/unity_ws/ROS/src/moveit_msgs/msg/RobotTrajectory.msg;/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/MultiDOFJointTrajectory.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Quaternion.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Vector3.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Twist.msg;/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Transform.msg;/opt/ros/melodic/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/panda_move
)
_generate_srv_py(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/ActionSequences.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/panda_move
)
_generate_srv_py(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/NewState.srv"
  "${MSG_I_FLAGS}"
  "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/panda_move
)
_generate_srv_py(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/MotionCheck.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/panda_move
)
_generate_srv_py(panda_move
  "/home/wng/unity_ws/ROS/src/panda_move/srv/Hand.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/panda_move
)

### Generating Module File
_generate_module_py(panda_move
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/panda_move
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(panda_move_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(panda_move_generate_messages panda_move_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Sync.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_py _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/Action.msg" NAME_WE)
add_dependencies(panda_move_generate_messages_py _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Init.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_py _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/Predicate.msg" NAME_WE)
add_dependencies(panda_move_generate_messages_py _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Plan.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_py _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/msg/ExecutionCheck.msg" NAME_WE)
add_dependencies(panda_move_generate_messages_py _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/ActionSequences.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_py _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/NewState.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_py _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/MotionCheck.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_py _panda_move_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wng/unity_ws/ROS/src/panda_move/srv/Hand.srv" NAME_WE)
add_dependencies(panda_move_generate_messages_py _panda_move_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(panda_move_genpy)
add_dependencies(panda_move_genpy panda_move_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS panda_move_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/panda_move)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/panda_move
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(panda_move_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(panda_move_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET moveit_msgs_generate_messages_cpp)
  add_dependencies(panda_move_generate_messages_cpp moveit_msgs_generate_messages_cpp)
endif()
if(TARGET sensor_msgs_generate_messages_cpp)
  add_dependencies(panda_move_generate_messages_cpp sensor_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/panda_move)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/panda_move
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(panda_move_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(panda_move_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET moveit_msgs_generate_messages_eus)
  add_dependencies(panda_move_generate_messages_eus moveit_msgs_generate_messages_eus)
endif()
if(TARGET sensor_msgs_generate_messages_eus)
  add_dependencies(panda_move_generate_messages_eus sensor_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/panda_move)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/panda_move
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(panda_move_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(panda_move_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET moveit_msgs_generate_messages_lisp)
  add_dependencies(panda_move_generate_messages_lisp moveit_msgs_generate_messages_lisp)
endif()
if(TARGET sensor_msgs_generate_messages_lisp)
  add_dependencies(panda_move_generate_messages_lisp sensor_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/panda_move)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/panda_move
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(panda_move_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(panda_move_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET moveit_msgs_generate_messages_nodejs)
  add_dependencies(panda_move_generate_messages_nodejs moveit_msgs_generate_messages_nodejs)
endif()
if(TARGET sensor_msgs_generate_messages_nodejs)
  add_dependencies(panda_move_generate_messages_nodejs sensor_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/panda_move)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/panda_move\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/panda_move
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(panda_move_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(panda_move_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET moveit_msgs_generate_messages_py)
  add_dependencies(panda_move_generate_messages_py moveit_msgs_generate_messages_py)
endif()
if(TARGET sensor_msgs_generate_messages_py)
  add_dependencies(panda_move_generate_messages_py sensor_msgs_generate_messages_py)
endif()
