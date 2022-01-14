
(cl:in-package :asdf)

(defsystem "panda_move-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :moveit_msgs-msg
)
  :components ((:file "_package")
    (:file "Action" :depends-on ("_package_Action"))
    (:file "_package_Action" :depends-on ("_package"))
    (:file "ExecutionCheck" :depends-on ("_package_ExecutionCheck"))
    (:file "_package_ExecutionCheck" :depends-on ("_package"))
    (:file "PandaMoveitJoints" :depends-on ("_package_PandaMoveitJoints"))
    (:file "_package_PandaMoveitJoints" :depends-on ("_package"))
    (:file "PandaTrajectory" :depends-on ("_package_PandaTrajectory"))
    (:file "_package_PandaTrajectory" :depends-on ("_package"))
    (:file "Predicate" :depends-on ("_package_Predicate"))
    (:file "_package_Predicate" :depends-on ("_package"))
    (:file "TrajectoryPoint" :depends-on ("_package_TrajectoryPoint"))
    (:file "_package_TrajectoryPoint" :depends-on ("_package"))
    (:file "orientation" :depends-on ("_package_orientation"))
    (:file "_package_orientation" :depends-on ("_package"))
    (:file "position" :depends-on ("_package_position"))
    (:file "_package_position" :depends-on ("_package"))
  ))