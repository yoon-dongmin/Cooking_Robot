# Install script for directory: /home/wng/unity_ws/ROS/src/moveit_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/wng/unity_ws/ROS/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_msgs/action" TYPE FILE FILES
    "/home/wng/unity_ws/ROS/src/moveit_msgs/action/ExecuteTrajectory.action"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/action/MoveGroup.action"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/action/MoveGroupSequence.action"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/action/Pickup.action"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/action/Place.action"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_msgs/msg" TYPE FILE FILES
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/ExecuteTrajectoryAction.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/ExecuteTrajectoryActionGoal.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/ExecuteTrajectoryActionResult.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/ExecuteTrajectoryActionFeedback.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/ExecuteTrajectoryGoal.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/ExecuteTrajectoryResult.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/ExecuteTrajectoryFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_msgs/msg" TYPE FILE FILES
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/MoveGroupAction.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/MoveGroupActionGoal.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/MoveGroupActionResult.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/MoveGroupActionFeedback.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/MoveGroupGoal.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/MoveGroupResult.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/MoveGroupFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_msgs/msg" TYPE FILE FILES
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/MoveGroupSequenceAction.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/MoveGroupSequenceActionGoal.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/MoveGroupSequenceActionResult.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/MoveGroupSequenceActionFeedback.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/MoveGroupSequenceGoal.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/MoveGroupSequenceResult.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/MoveGroupSequenceFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_msgs/msg" TYPE FILE FILES
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/PickupAction.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/PickupActionGoal.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/PickupActionResult.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/PickupActionFeedback.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/PickupGoal.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/PickupResult.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/PickupFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_msgs/msg" TYPE FILE FILES
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/PlaceAction.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/PlaceActionGoal.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/PlaceActionResult.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/PlaceActionFeedback.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/PlaceGoal.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/PlaceResult.msg"
    "/home/wng/unity_ws/ROS/devel/share/moveit_msgs/msg/PlaceFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_msgs/msg" TYPE FILE FILES
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/AllowedCollisionEntry.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/AllowedCollisionMatrix.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/AttachedCollisionObject.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/BoundingVolume.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/CollisionObject.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/ConstraintEvalResult.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/Constraints.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/CostSource.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/ContactInformation.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/DisplayTrajectory.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/DisplayRobotState.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/Grasp.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/GripperTranslation.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/JointConstraint.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/JointLimits.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/LinkPadding.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/LinkScale.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/MotionPlanRequest.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/MotionPlanResponse.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/MotionPlanDetailedResponse.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/MotionSequenceItem.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/MotionSequenceRequest.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/MotionSequenceResponse.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/MoveItErrorCodes.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/TrajectoryConstraints.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/ObjectColor.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/OrientationConstraint.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/OrientedBoundingBox.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/PlaceLocation.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/PlannerInterfaceDescription.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/PlannerParams.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/PlanningScene.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/PlanningSceneComponents.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/PlanningSceneWorld.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/PlanningOptions.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/PositionConstraint.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/RobotState.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/RobotTrajectory.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/VisibilityConstraint.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/WorkspaceParameters.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/KinematicSolverInfo.msg"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/msg/PositionIKRequest.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_msgs/srv" TYPE FILE FILES
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/GetMotionPlan.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/ExecuteKnownTrajectory.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/GetStateValidity.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/GetCartesianPath.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/GetPlanningScene.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/GraspPlanning.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/ApplyPlanningScene.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/QueryPlannerInterfaces.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/GetMotionSequence.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/GetPositionFK.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/GetPositionIK.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/GetPlannerParams.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/SetPlannerParams.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/SaveMap.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/LoadMap.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/SaveRobotStateToWarehouse.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/ListRobotStatesInWarehouse.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/GetRobotStateFromWarehouse.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/CheckIfRobotStateExistsInWarehouse.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/RenameRobotStateInWarehouse.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/DeleteRobotStateFromWarehouse.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/ChangeControlDimensions.srv"
    "/home/wng/unity_ws/ROS/src/moveit_msgs/srv/ChangeDriftDimensions.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_msgs/cmake" TYPE FILE FILES "/home/wng/unity_ws/ROS/build/moveit_msgs/catkin_generated/installspace/moveit_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/wng/unity_ws/ROS/devel/include/moveit_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/wng/unity_ws/ROS/devel/share/roseus/ros/moveit_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/wng/unity_ws/ROS/devel/share/common-lisp/ros/moveit_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/wng/unity_ws/ROS/devel/share/gennodejs/ros/moveit_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/wng/unity_ws/ROS/devel/lib/python2.7/dist-packages/moveit_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/wng/unity_ws/ROS/devel/lib/python2.7/dist-packages/moveit_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/wng/unity_ws/ROS/build/moveit_msgs/catkin_generated/installspace/moveit_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_msgs/cmake" TYPE FILE FILES "/home/wng/unity_ws/ROS/build/moveit_msgs/catkin_generated/installspace/moveit_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_msgs/cmake" TYPE FILE FILES
    "/home/wng/unity_ws/ROS/build/moveit_msgs/catkin_generated/installspace/moveit_msgsConfig.cmake"
    "/home/wng/unity_ws/ROS/build/moveit_msgs/catkin_generated/installspace/moveit_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_msgs" TYPE FILE FILES "/home/wng/unity_ws/ROS/src/moveit_msgs/package.xml")
endif()

