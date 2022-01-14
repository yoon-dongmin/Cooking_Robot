;; Auto-generated. Do not edit!


(when (boundp 'panda_move::NewState)
  (if (not (find-package "PANDA_MOVE"))
    (make-package "PANDA_MOVE"))
  (shadow 'NewState (find-package "PANDA_MOVE")))
(unless (find-package "PANDA_MOVE::NEWSTATE")
  (make-package "PANDA_MOVE::NEWSTATE"))
(unless (find-package "PANDA_MOVE::NEWSTATEREQUEST")
  (make-package "PANDA_MOVE::NEWSTATEREQUEST"))
(unless (find-package "PANDA_MOVE::NEWSTATERESPONSE")
  (make-package "PANDA_MOVE::NEWSTATERESPONSE"))

(in-package "ROS")





(defclass panda_move::NewStateRequest
  :super ros::object
  :slots (_new_state ))

(defmethod panda_move::NewStateRequest
  (:init
   (&key
    ((:new_state __new_state) (let (r) (dotimes (i 0) (push (instance panda_move::Predicate :init) r)) r))
    )
   (send-super :init)
   (setq _new_state __new_state)
   self)
  (:new_state
   (&rest __new_state)
   (if (keywordp (car __new_state))
       (send* _new_state __new_state)
     (progn
       (if __new_state (setq _new_state (car __new_state)))
       _new_state)))
  (:serialization-length
   ()
   (+
    ;; panda_move/Predicate[] _new_state
    (apply #'+ (send-all _new_state :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; panda_move/Predicate[] _new_state
     (write-long (length _new_state) s)
     (dolist (elem _new_state)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; panda_move/Predicate[] _new_state
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _new_state (let (r) (dotimes (i n) (push (instance panda_move::Predicate :init) r)) r))
     (dolist (elem- _new_state)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(defclass panda_move::NewStateResponse
  :super ros::object
  :slots (_result ))

(defmethod panda_move::NewStateResponse
  (:init
   (&key
    ((:result __result) nil)
    )
   (send-super :init)
   (setq _result __result)
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; bool _result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _result
       (if _result (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _result
     (setq _result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass panda_move::NewState
  :super ros::object
  :slots ())

(setf (get panda_move::NewState :md5sum-) "92d4a807a3e01f714a92618d52a8f78f")
(setf (get panda_move::NewState :datatype-) "panda_move/NewState")
(setf (get panda_move::NewState :request) panda_move::NewStateRequest)
(setf (get panda_move::NewState :response) panda_move::NewStateResponse)

(defmethod panda_move::NewStateRequest
  (:response () (instance panda_move::NewStateResponse :init)))

(setf (get panda_move::NewStateRequest :md5sum-) "92d4a807a3e01f714a92618d52a8f78f")
(setf (get panda_move::NewStateRequest :datatype-) "panda_move/NewStateRequest")
(setf (get panda_move::NewStateRequest :definition-)
      "panda_move/Predicate[] new_state

================================================================================
MSG: panda_move/Predicate
string name
---
bool result
")

(setf (get panda_move::NewStateResponse :md5sum-) "92d4a807a3e01f714a92618d52a8f78f")
(setf (get panda_move::NewStateResponse :datatype-) "panda_move/NewStateResponse")
(setf (get panda_move::NewStateResponse :definition-)
      "panda_move/Predicate[] new_state

================================================================================
MSG: panda_move/Predicate
string name
---
bool result
")



(provide :panda_move/NewState "92d4a807a3e01f714a92618d52a8f78f")


