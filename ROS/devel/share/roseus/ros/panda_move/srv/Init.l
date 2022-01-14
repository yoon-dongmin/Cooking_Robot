;; Auto-generated. Do not edit!


(when (boundp 'panda_move::Init)
  (if (not (find-package "PANDA_MOVE"))
    (make-package "PANDA_MOVE"))
  (shadow 'Init (find-package "PANDA_MOVE")))
(unless (find-package "PANDA_MOVE::INIT")
  (make-package "PANDA_MOVE::INIT"))
(unless (find-package "PANDA_MOVE::INITREQUEST")
  (make-package "PANDA_MOVE::INITREQUEST"))
(unless (find-package "PANDA_MOVE::INITRESPONSE")
  (make-package "PANDA_MOVE::INITRESPONSE"))

(in-package "ROS")

(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))




(defclass panda_move::InitRequest
  :super ros::object
  :slots (_activated_object _position _orientation _scale _joint_state ))

(defmethod panda_move::InitRequest
  (:init
   (&key
    ((:activated_object __activated_object) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:position __position) (let (r) (dotimes (i 0) (push (instance geometry_msgs::Point :init) r)) r))
    ((:orientation __orientation) (let (r) (dotimes (i 0) (push (instance geometry_msgs::Quaternion :init) r)) r))
    ((:scale __scale) (let (r) (dotimes (i 0) (push (instance geometry_msgs::Vector3 :init) r)) r))
    ((:joint_state __joint_state) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _activated_object __activated_object)
   (setq _position __position)
   (setq _orientation __orientation)
   (setq _scale __scale)
   (setq _joint_state __joint_state)
   self)
  (:activated_object
   (&optional __activated_object)
   (if __activated_object (setq _activated_object __activated_object)) _activated_object)
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
  (:scale
   (&rest __scale)
   (if (keywordp (car __scale))
       (send* _scale __scale)
     (progn
       (if __scale (setq _scale (car __scale)))
       _scale)))
  (:joint_state
   (&optional __joint_state)
   (if __joint_state (setq _joint_state __joint_state)) _joint_state)
  (:serialization-length
   ()
   (+
    ;; string[] _activated_object
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _activated_object)) 4
    ;; geometry_msgs/Point[] _position
    (apply #'+ (send-all _position :serialization-length)) 4
    ;; geometry_msgs/Quaternion[] _orientation
    (apply #'+ (send-all _orientation :serialization-length)) 4
    ;; geometry_msgs/Vector3[] _scale
    (apply #'+ (send-all _scale :serialization-length)) 4
    ;; float64[] _joint_state
    (* 8    (length _joint_state)) 4
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
     ;; geometry_msgs/Vector3[] _scale
     (write-long (length _scale) s)
     (dolist (elem _scale)
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
   ;; string[] _activated_object
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _activated_object (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _activated_object i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
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
   ;; geometry_msgs/Vector3[] _scale
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _scale (let (r) (dotimes (i n) (push (instance geometry_msgs::Vector3 :init) r)) r))
     (dolist (elem- _scale)
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

(defclass panda_move::InitResponse
  :super ros::object
  :slots (_init_state ))

(defmethod panda_move::InitResponse
  (:init
   (&key
    ((:init_state __init_state) 0)
    )
   (send-super :init)
   (setq _init_state (round __init_state))
   self)
  (:init_state
   (&optional __init_state)
   (if __init_state (setq _init_state __init_state)) _init_state)
  (:serialization-length
   ()
   (+
    ;; int64 _init_state
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _init_state
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _init_state (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _init_state) (= (length (_init_state . bv)) 2)) ;; bignum
              (write-long (ash (elt (_init_state . bv) 0) 0) s)
              (write-long (ash (elt (_init_state . bv) 1) -1) s))
             ((and (class _init_state) (= (length (_init_state . bv)) 1)) ;; big1
              (write-long (elt (_init_state . bv) 0) s)
              (write-long (if (>= _init_state 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _init_state s)(write-long (if (>= _init_state 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _init_state
#+(or :alpha :irix6 :x86_64)
      (setf _init_state (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _init_state (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass panda_move::Init
  :super ros::object
  :slots ())

(setf (get panda_move::Init :md5sum-) "73f72d80c9600a1ec553e98d0e61c060")
(setf (get panda_move::Init :datatype-) "panda_move/Init")
(setf (get panda_move::Init :request) panda_move::InitRequest)
(setf (get panda_move::Init :response) panda_move::InitResponse)

(defmethod panda_move::InitRequest
  (:response () (instance panda_move::InitResponse :init)))

(setf (get panda_move::InitRequest :md5sum-) "73f72d80c9600a1ec553e98d0e61c060")
(setf (get panda_move::InitRequest :datatype-) "panda_move/InitRequest")
(setf (get panda_move::InitRequest :definition-)
      "string[] activated_object
geometry_msgs/Point[] position
geometry_msgs/Quaternion[] orientation
geometry_msgs/Vector3[] scale
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

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
---
int64 init_state
")

(setf (get panda_move::InitResponse :md5sum-) "73f72d80c9600a1ec553e98d0e61c060")
(setf (get panda_move::InitResponse :datatype-) "panda_move/InitResponse")
(setf (get panda_move::InitResponse :definition-)
      "string[] activated_object
geometry_msgs/Point[] position
geometry_msgs/Quaternion[] orientation
geometry_msgs/Vector3[] scale
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

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
---
int64 init_state
")



(provide :panda_move/Init "73f72d80c9600a1ec553e98d0e61c060")


