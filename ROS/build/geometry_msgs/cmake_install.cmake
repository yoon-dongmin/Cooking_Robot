# Install script for directory: /home/wng/unity_ws/ROS/src/geometry_msgs

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/geometry_msgs/msg" TYPE FILE FILES
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Accel.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/AccelStamped.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/AccelWithCovariance.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/AccelWithCovarianceStamped.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Inertia.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/InertiaStamped.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Point.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Point32.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/PointStamped.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Polygon.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/PolygonStamped.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Pose2D.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Pose.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/PoseArray.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/PoseStamped.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/PoseWithCovariance.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/PoseWithCovarianceStamped.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Quaternion.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/QuaternionStamped.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Transform.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/TransformStamped.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Twist.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/TwistStamped.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/TwistWithCovariance.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/TwistWithCovarianceStamped.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Vector3.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Vector3Stamped.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/Wrench.msg"
    "/home/wng/unity_ws/ROS/src/geometry_msgs/msg/WrenchStamped.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/geometry_msgs/cmake" TYPE FILE FILES "/home/wng/unity_ws/ROS/build/geometry_msgs/catkin_generated/installspace/geometry_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/wng/unity_ws/ROS/devel/include/geometry_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/wng/unity_ws/ROS/devel/share/roseus/ros/geometry_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/wng/unity_ws/ROS/devel/share/common-lisp/ros/geometry_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/wng/unity_ws/ROS/devel/share/gennodejs/ros/geometry_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/wng/unity_ws/ROS/devel/lib/python2.7/dist-packages/geometry_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/wng/unity_ws/ROS/devel/lib/python2.7/dist-packages/geometry_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/wng/unity_ws/ROS/build/geometry_msgs/catkin_generated/installspace/geometry_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/geometry_msgs/cmake" TYPE FILE FILES "/home/wng/unity_ws/ROS/build/geometry_msgs/catkin_generated/installspace/geometry_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/geometry_msgs/cmake" TYPE FILE FILES
    "/home/wng/unity_ws/ROS/build/geometry_msgs/catkin_generated/installspace/geometry_msgsConfig.cmake"
    "/home/wng/unity_ws/ROS/build/geometry_msgs/catkin_generated/installspace/geometry_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/geometry_msgs" TYPE FILE FILES "/home/wng/unity_ws/ROS/src/geometry_msgs/package.xml")
endif()

