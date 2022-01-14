; Auto-generated. Do not edit!


(cl:in-package panda_move-srv)


;//! \htmlinclude MotionCheck-request.msg.html

(cl:defclass <MotionCheck-request> (roslisp-msg-protocol:ros-message)
  ((motion_type
    :reader motion_type
    :initarg :motion_type
    :type cl:string
    :initform "")
   (object_1
    :reader object_1
    :initarg :object_1
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element ""))
   (object_2
    :reader object_2
    :initarg :object_2
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element "")))
)

(cl:defclass MotionCheck-request (<MotionCheck-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MotionCheck-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MotionCheck-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name panda_move-srv:<MotionCheck-request> is deprecated: use panda_move-srv:MotionCheck-request instead.")))

(cl:ensure-generic-function 'motion_type-val :lambda-list '(m))
(cl:defmethod motion_type-val ((m <MotionCheck-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panda_move-srv:motion_type-val is deprecated.  Use panda_move-srv:motion_type instead.")
  (motion_type m))

(cl:ensure-generic-function 'object_1-val :lambda-list '(m))
(cl:defmethod object_1-val ((m <MotionCheck-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panda_move-srv:object_1-val is deprecated.  Use panda_move-srv:object_1 instead.")
  (object_1 m))

(cl:ensure-generic-function 'object_2-val :lambda-list '(m))
(cl:defmethod object_2-val ((m <MotionCheck-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panda_move-srv:object_2-val is deprecated.  Use panda_move-srv:object_2 instead.")
  (object_2 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MotionCheck-request>) ostream)
  "Serializes a message object of type '<MotionCheck-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'motion_type))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'motion_type))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'object_1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'object_1))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'object_2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'object_2))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MotionCheck-request>) istream)
  "Deserializes a message object of type '<MotionCheck-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'motion_type) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'motion_type) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'object_1) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'object_1)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'object_2) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'object_2)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MotionCheck-request>)))
  "Returns string type for a service object of type '<MotionCheck-request>"
  "panda_move/MotionCheckRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MotionCheck-request)))
  "Returns string type for a service object of type 'MotionCheck-request"
  "panda_move/MotionCheckRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MotionCheck-request>)))
  "Returns md5sum for a message object of type '<MotionCheck-request>"
  "f3ead81734321a8717b9ae871d1b0fcb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MotionCheck-request)))
  "Returns md5sum for a message object of type 'MotionCheck-request"
  "f3ead81734321a8717b9ae871d1b0fcb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MotionCheck-request>)))
  "Returns full string definition for message of type '<MotionCheck-request>"
  (cl:format cl:nil "string motion_type~%string[] object_1~%string[] object_2~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MotionCheck-request)))
  "Returns full string definition for message of type 'MotionCheck-request"
  (cl:format cl:nil "string motion_type~%string[] object_1~%string[] object_2~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MotionCheck-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'motion_type))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'object_1) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'object_2) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MotionCheck-request>))
  "Converts a ROS message object to a list"
  (cl:list 'MotionCheck-request
    (cl:cons ':motion_type (motion_type msg))
    (cl:cons ':object_1 (object_1 msg))
    (cl:cons ':object_2 (object_2 msg))
))
;//! \htmlinclude MotionCheck-response.msg.html

(cl:defclass <MotionCheck-response> (roslisp-msg-protocol:ros-message)
  ((execute_state
    :reader execute_state
    :initarg :execute_state
    :type cl:integer
    :initform 0))
)

(cl:defclass MotionCheck-response (<MotionCheck-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MotionCheck-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MotionCheck-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name panda_move-srv:<MotionCheck-response> is deprecated: use panda_move-srv:MotionCheck-response instead.")))

(cl:ensure-generic-function 'execute_state-val :lambda-list '(m))
(cl:defmethod execute_state-val ((m <MotionCheck-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panda_move-srv:execute_state-val is deprecated.  Use panda_move-srv:execute_state instead.")
  (execute_state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MotionCheck-response>) ostream)
  "Serializes a message object of type '<MotionCheck-response>"
  (cl:let* ((signed (cl:slot-value msg 'execute_state)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MotionCheck-response>) istream)
  "Deserializes a message object of type '<MotionCheck-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'execute_state) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MotionCheck-response>)))
  "Returns string type for a service object of type '<MotionCheck-response>"
  "panda_move/MotionCheckResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MotionCheck-response)))
  "Returns string type for a service object of type 'MotionCheck-response"
  "panda_move/MotionCheckResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MotionCheck-response>)))
  "Returns md5sum for a message object of type '<MotionCheck-response>"
  "f3ead81734321a8717b9ae871d1b0fcb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MotionCheck-response)))
  "Returns md5sum for a message object of type 'MotionCheck-response"
  "f3ead81734321a8717b9ae871d1b0fcb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MotionCheck-response>)))
  "Returns full string definition for message of type '<MotionCheck-response>"
  (cl:format cl:nil "int64 execute_state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MotionCheck-response)))
  "Returns full string definition for message of type 'MotionCheck-response"
  (cl:format cl:nil "int64 execute_state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MotionCheck-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MotionCheck-response>))
  "Converts a ROS message object to a list"
  (cl:list 'MotionCheck-response
    (cl:cons ':execute_state (execute_state msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'MotionCheck)))
  'MotionCheck-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'MotionCheck)))
  'MotionCheck-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MotionCheck)))
  "Returns string type for a service object of type '<MotionCheck>"
  "panda_move/MotionCheck")