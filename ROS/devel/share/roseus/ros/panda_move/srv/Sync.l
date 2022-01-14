;; Auto-generated. Do not edit!


(when (boundp 'panda_move::Sync)
  (if (not (find-package "PANDA_MOVE"))
    (make-package "PANDA_MOVE"))
  (shadow 'Sync (find-package "PANDA_MOVE")))
(unless (find-package "PANDA_MOVE::SYNC")
  (make-package "PANDA_MOVE::SYNC"))
(unless (find-package "PANDA_MOVE::SYNCREQUEST")
  (make-package "PANDA_MOVE::SYNCREQUEST"))
(unless (find-package "PANDA_MOVE::SYNCRESPONSE")
  (make-package "PANDA_MOVE::SYNCRESPONSE"))

(in-package "ROS")



(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass panda_move::SyncRequest
  :super ros::object
  :slots (_activated_object ))

(defmethod panda_move::SyncRequest
  (:init
   (&key
    ((:activated_object __activated_object) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _activated_object __activated_object)
   self)
  (:activated_object
   (&optional __activated_object)
   (if __activated_object (setq _activated_object __activated_object)) _activated_object)
  (:serialization-length
   ()
   (+
    ;; string[] _activated_object
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _activated_object)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _activated_object
     (write-long (length _activated_object) s)
     (dolist (elem _activated_object)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _activated_object
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _activated_object (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _activated_object i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(defclass panda_move::SyncResponse
  :super ros::object
  :slots (_object_name _position _orientation _joint_state ))

(defmethod panda_move::SyncResponse
  (:init
   (&key
    ((:object_name __object_name) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:position __position) (let (r) (dotimes (i 0) (push (instance geometry_msgs::Point :init) r)) r))
    ((:orientation __orientation) (let (r) (dotimes (i 0) (push (instance geometry_msgs::Quaternion :init) r)) r))
    ((:joint_state __joint_state) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _object_name __object_name)
   (setq _position __position)
   (setq _orientation __orientation)
   (setq _joint_state __joint_state)
   self)
  (:object_name
   (&optional __object_name)
   (if __object_name (setq _object_name __object_name)) _object_name)
  (:position
   (&rest __position)
   (if (keywordp (car __position))
       (send* _position __position)
     (progn
       (if __position (setq _position (car __position)))
       _position)))
  (:orientation
   (&rest __orientation)
   (if (keywordp (car __orientation))
       (send* _orientation __orientation)
     (progn
       (if __orientation (setq _orientation (car __orientation)))
       _orientation)))
  (:joint_state
   (&optional __joint_state)
   (if __joint_state (setq _joint_state __joint_state)) _joint_state)
  (:serialization-length
   ()
   (+
    ;; string[] _object_name
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _object_name)) 4
    ;; geometry_msgs/Point[] _position
    (apply #'+ (send-all _position :serialization-length)) 4
    ;; geometry_msgs/Quaternion[] _orientation
    (apply #'+ (send-all _orientation :serialization-length)) 4
    ;; float64[] _joint_state
    (* 8    (length _joint_state)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _object_name
     (write-long (length _object_name) s)
     (dolist (elem _object_name)
       (write-long (length elem) s) (princ elem s)
       )
     ;; geometry_msgs/Point[] _position
     (write-long (length _position) s)
     (dolist (elem _position)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Quaternion[] _orientation
     (write-long (length _orientation) s)
     (dolist (elem _orientation)
       (send elem :serialize s)
       )
     ;; float64[] _joint_state
     (write-long (length _joint_state) s)
     (dotimes (i (length _joint_state))
       (sys::poke (elt _joint_state i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _object_name
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _object_name (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _object_name i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; geometry_msgs/Point[] _position
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _position (let (r) (dotimes (i n) (push (instance geometry_msgs::Point :init) r)) r))
     (dolist (elem- _position)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Quaternion[] _orientation
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _orientation (let (r) (dotimes (i n) (push (instance geometry_msgs::Quaternion :init) r)) r))
     (dolist (elem- _orientation)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; float64[] _joint_state
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _joint_state (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _joint_state i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(defclass panda_move::Sync
  :super ros::object
  :slots ())

(setf (get panda_move::Sync :md5sum-) "d850a51077e21c58d4f7667e1676cebc")
(setf (get panda_move::Sync :datatype-) "panda_move/Sync")
(setf (get panda_move::Sync :request) panda_move::SyncRequest)
(setf (get panda_move::Sync :response) panda_move::SyncResponse)

(defmethod panda_move::SyncRequest
  (:response () (instance panda_move::SyncResponse :init)))

(setf (get panda_move::SyncRequest :md5sum-) "d850a51077e21c58d4f7667e1676cebc")
(setf (get panda_move::SyncRequest :datatype-) "panda_move/SyncRequest")
(setf (get panda_move::SyncRequest :definition-)
      "string[] activated_object
---
string[] object_name
geometry_msgs/Point[] position
geometry_msgs/Quaternion[] orientation
float64[] joint_state

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
")

(setf (get panda_move::SyncResponse :md5sum-) "d850a51077e21c58d4f7667e1676cebc")
(setf (get panda_move::SyncResponse :datatype-) "panda_move/SyncResponse")
(setf (get panda_move::SyncResponse :definition-)
      "string[] activated_object
---
string[] object_name
geometry_msgs/Point[] position
geometry_msgs/Quaternion[] orientation
float64[] joint_state

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
")



(provide :panda_move/Sync "d850a51077e21c58d4f7667e1676cebc")


