
(cl:in-package :asdf)

(defsystem "panda_move-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :moveit_msgs-msg
               :panda_move-msg
)
  :components ((:file "_package")
    (:file "ActionSequences" :depends-on ("_package_ActionSequences"))
    (:file "_package_ActionSequences" :depends-on ("_package"))
    (:file "Hand" :depends-on ("_package_Hand"))
    (:file "_package_Hand" :depends-on ("_package"))
    (:file "Init" :depends-on ("_package_Init"))
    (:file "_package_Init" :depends-on ("_package"))
    (:file "MotionCheck" :depends-on ("_package_MotionCheck"))
    (:file "_package_MotionCheck" :depends-on ("_package"))
    (:file "NewState" :depends-on ("_package_NewState"))
    (:file "_package_NewState" :depends-on ("_package"))
    (:file "Plan" :depends-on ("_package_Plan"))
    (:file "_package_Plan" :depends-on ("_package"))
    (:file "Sync" :depends-on ("_package_Sync"))
    (:file "_package_Sync" :depends-on ("_package"))
  ))