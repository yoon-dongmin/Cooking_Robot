;; Auto-generated. Do not edit!


(when (boundp 'panda_move::Hand)
  (if (not (find-package "PANDA_MOVE"))
    (make-package "PANDA_MOVE"))
  (shadow 'Hand (find-package "PANDA_MOVE")))
(unless (find-package "PANDA_MOVE::HAND")
  (make-package "PANDA_MOVE::HAND"))
(unless (find-package "PANDA_MOVE::HANDREQUEST")
  (make-package "PANDA_MOVE::HANDREQUEST"))
(unless (find-package "PANDA_MOVE::HANDRESPONSE")
  (make-package "PANDA_MOVE::HANDRESPONSE"))

(in-package "ROS")





(defclass panda_move::HandRequest
  :super ros::object
  :slots (_grasp_state _object_name _grasp_size ))

(defmethod panda_move::HandRequest
  (:init
   (&key
    ((:grasp_state __grasp_state) nil)
    ((:object_name __object_name) "")
    ((:grasp_size __grasp_size) 0.0)
    )
   (send-super :init)
   (setq _grasp_state __grasp_state)
   (setq _object_name (string __object_name))
   (setq _grasp_size (float __grasp_size))
   self)
  (:grasp_state
   (&optional __grasp_state)
   (if __grasp_state (setq _grasp_state __grasp_state)) _grasp_state)
  (:object_name
   (&optional __object_name)
   (if __object_name (setq _object_name __object_name)) _object_name)
  (:grasp_size
   (&optional __grasp_size)
   (if __grasp_size (setq _grasp_size __grasp_size)) _grasp_size)
  (:serialization-length
   ()
   (+
    ;; bool _grasp_state
    1
    ;; string _object_name
    4 (length _object_name)
    ;; float64 _grasp_size
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _grasp_state
       (if _grasp_state (write-byte -1 s) (write-byte 0 s))
     ;; string _object_name
       (write-long (length _object_name) s) (princ _object_name s)
     ;; float64 _grasp_size
       (sys::poke _grasp_size (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _grasp_state
     (setq _grasp_state (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _object_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _object_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _grasp_size
     (setq _grasp_size (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass panda_move::HandResponse
  :super ros::object
  :slots (_execute_state ))

(defmethod panda_move::HandResponse
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

(defclass panda_move::Hand
  :super ros::object
  :slots ())

(setf (get panda_move::Hand :md5sum-) "90c7acc194a7a7121ca85308c4242240")
(setf (get panda_move::Hand :datatype-) "panda_move/Hand")
(setf (get panda_move::Hand :request) panda_move::HandRequest)
(setf (get panda_move::Hand :response) panda_move::HandResponse)

(defmethod panda_move::HandRequest
  (:response () (instance panda_move::HandResponse :init)))

(setf (get panda_move::HandRequest :md5sum-) "90c7acc194a7a7121ca85308c4242240")
(setf (get panda_move::HandRequest :datatype-) "panda_move/HandRequest")
(setf (get panda_move::HandRequest :definition-)
      "bool grasp_state
string object_name
float64 grasp_size
---
int64 execute_state
")

(setf (get panda_move::HandResponse :md5sum-) "90c7acc194a7a7121ca85308c4242240")
(setf (get panda_move::HandResponse :datatype-) "panda_move/HandResponse")
(setf (get panda_move::HandResponse :definition-)
      "bool grasp_state
string object_name
float64 grasp_size
---
int64 execute_state
")



(provide :panda_move/Hand "90c7acc194a7a7121ca85308c4242240")


