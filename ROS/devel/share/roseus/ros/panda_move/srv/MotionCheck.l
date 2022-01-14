;; Auto-generated. Do not edit!


(when (boundp 'panda_move::MotionCheck)
  (if (not (find-package "PANDA_MOVE"))
    (make-package "PANDA_MOVE"))
  (shadow 'MotionCheck (find-package "PANDA_MOVE")))
(unless (find-package "PANDA_MOVE::MOTIONCHECK")
  (make-package "PANDA_MOVE::MOTIONCHECK"))
(unless (find-package "PANDA_MOVE::MOTIONCHECKREQUEST")
  (make-package "PANDA_MOVE::MOTIONCHECKREQUEST"))
(unless (find-package "PANDA_MOVE::MOTIONCHECKRESPONSE")
  (make-package "PANDA_MOVE::MOTIONCHECKRESPONSE"))

(in-package "ROS")





(defclass panda_move::MotionCheckRequest
  :super ros::object
  :slots (_motion_type _object_1 _object_2 ))

(defmethod panda_move::MotionCheckRequest
  (:init
   (&key
    ((:motion_type __motion_type) "")
    ((:object_1 __object_1) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:object_2 __object_2) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _motion_type (string __motion_type))
   (setq _object_1 __object_1)
   (setq _object_2 __object_2)
   self)
  (:motion_type
   (&optional __motion_type)
   (if __motion_type (setq _motion_type __motion_type)) _motion_type)
  (:object_1
   (&optional __object_1)
   (if __object_1 (setq _object_1 __object_1)) _object_1)
  (:object_2
   (&optional __object_2)
   (if __object_2 (setq _object_2 __object_2)) _object_2)
  (:serialization-length
   ()
   (+
    ;; string _motion_type
    4 (length _motion_type)
    ;; string[] _object_1
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _object_1)) 4
    ;; string[] _object_2
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _object_2)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _motion_type
       (write-long (length _motion_type) s) (princ _motion_type s)
     ;; string[] _object_1
     (write-long (length _object_1) s)
     (dolist (elem _object_1)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string[] _object_2
     (write-long (length _object_2) s)
     (dolist (elem _object_2)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _motion_type
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _motion_type (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string[] _object_1
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _object_1 (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _object_1 i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string[] _object_2
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _object_2 (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _object_2 i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(defclass panda_move::MotionCheckResponse
  :super ros::object
  :slots (_execute_state ))

(defmethod panda_move::MotionCheckResponse
  (:init
   (&key
    ((:execute_state __execute_state) 0)
    )
   (send-super :init)
   (setq _execute_state (round __execute_state))
   self)
  (:execute_state
   (&optional __execute_state)
   (if __execute_state (setq _execute_state __execute_state)) _execute_state)
  (:serialization-length
   ()
   (+
    ;; int64 _execute_state
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _execute_state
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _execute_state (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _execute_state) (= (length (_execute_state . bv)) 2)) ;; bignum
              (write-long (ash (elt (_execute_state . bv) 0) 0) s)
              (write-long (ash (elt (_execute_state . bv) 1) -1) s))
             ((and (class _execute_state) (= (length (_execute_state . bv)) 1)) ;; big1
              (write-long (elt (_execute_state . bv) 0) s)
              (write-long (if (>= _execute_state 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _execute_state s)(write-long (if (>= _execute_state 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _execute_state
#+(or :alpha :irix6 :x86_64)
      (setf _execute_state (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _execute_state (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
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

(defclass panda_move::MotionCheck
  :super ros::object
  :slots ())

(setf (get panda_move::MotionCheck :md5sum-) "f3ead81734321a8717b9ae871d1b0fcb")
(setf (get panda_move::MotionCheck :datatype-) "panda_move/MotionCheck")
(setf (get panda_move::MotionCheck :request) panda_move::MotionCheckRequest)
(setf (get panda_move::MotionCheck :response) panda_move::MotionCheckResponse)

(defmethod panda_move::MotionCheckRequest
  (:response () (instance panda_move::MotionCheckResponse :init)))

(setf (get panda_move::MotionCheckRequest :md5sum-) "f3ead81734321a8717b9ae871d1b0fcb")
(setf (get panda_move::MotionCheckRequest :datatype-) "panda_move/MotionCheckRequest")
(setf (get panda_move::MotionCheckRequest :definition-)
      "string motion_type
string[] object_1
string[] object_2
---
int64 execute_state
")

(setf (get panda_move::MotionCheckResponse :md5sum-) "f3ead81734321a8717b9ae871d1b0fcb")
(setf (get panda_move::MotionCheckResponse :datatype-) "panda_move/MotionCheckResponse")
(setf (get panda_move::MotionCheckResponse :definition-)
      "string motion_type
string[] object_1
string[] object_2
---
int64 execute_state
")



(provide :panda_move/MotionCheck "f3ead81734321a8717b9ae871d1b0fcb")


