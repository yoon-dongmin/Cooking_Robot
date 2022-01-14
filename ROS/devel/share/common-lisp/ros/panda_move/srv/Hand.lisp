; Auto-generated. Do not edit!


(cl:in-package panda_move-srv)


;//! \htmlinclude Hand-request.msg.html

(cl:defclass <Hand-request> (roslisp-msg-protocol:ros-message)
  ((grasp_state
    :reader grasp_state
    :initarg :grasp_state
    :type cl:boolean
    :initform cl:nil)
   (object_name
    :reader object_name
    :initarg :object_name
    :type cl:string
    :initform "")
   (grasp_size
    :reader grasp_size
    :initarg :grasp_size
    :type cl:float
    :initform 0.0))
)

(cl:defclass Hand-request (<Hand-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Hand-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Hand-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name panda_move-srv:<Hand-request> is deprecated: use panda_move-srv:Hand-request instead.")))

(cl:ensure-generic-function 'grasp_state-val :lambda-list '(m))
(cl:defmethod grasp_state-val ((m <Hand-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panda_move-srv:grasp_state-val is deprecated.  Use panda_move-srv:grasp_state instead.")
  (grasp_state m))

(cl:ensure-generic-function 'object_name-val :lambda-list '(m))
(cl:defmethod object_name-val ((m <Hand-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panda_move-srv:object_name-val is deprecated.  Use panda_move-srv:object_name instead.")
  (object_name m))

(cl:ensure-generic-function 'grasp_size-val :lambda-list '(m))
(cl:defmethod grasp_size-val ((m <Hand-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panda_move-srv:grasp_size-val is deprecated.  Use panda_move-srv:grasp_size instead.")
  (grasp_size m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Hand-request>) ostream)
  "Serializes a message object of type '<Hand-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'grasp_state) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'object_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'object_name))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'grasp_size))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Hand-request>) istream)
  "Deserializes a message object of type '<Hand-request>"
    (cl:setf (cl:slot-value msg 'grasp_state) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'object_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'object_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'grasp_size) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Hand-request>)))
  "Returns string type for a service object of type '<Hand-request>"
  "panda_move/HandRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Hand-request)))
  "Returns string type for a service object of type 'Hand-request"
  "panda_move/HandRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Hand-request>)))
  "Returns md5sum for a message object of type '<Hand-request>"
  "90c7acc194a7a7121ca85308c4242240")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Hand-request)))
  "Returns md5sum for a message object of type 'Hand-request"
  "90c7acc194a7a7121ca85308c4242240")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Hand-request>)))
  "Returns full string definition for message of type '<Hand-request>"
  (cl:format cl:nil "bool grasp_state~%string object_name~%float64 grasp_size~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Hand-request)))
  "Returns full string definition for message of type 'Hand-request"
  (cl:format cl:nil "bool grasp_state~%string object_name~%float64 grasp_size~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Hand-request>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'object_name))
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Hand-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Hand-request
    (cl:cons ':grasp_state (grasp_state msg))
    (cl:cons ':object_name (object_name msg))
    (cl:cons ':grasp_size (grasp_size msg))
))
;//! \htmlinclude Hand-response.msg.html

(cl:defclass <Hand-response> (roslisp-msg-protocol:ros-message)
  ((execute_state
    :reader execute_state
    :initarg :execute_state
    :type cl:integer
    :initform 0))
)

(cl:defclass Hand-response (<Hand-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Hand-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Hand-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name panda_move-srv:<Hand-response> is deprecated: use panda_move-srv:Hand-response instead.")))

(cl:ensure-generic-function 'execute_state-val :lambda-list '(m))
(cl:defmethod execute_state-val ((m <Hand-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panda_move-srv:execute_state-val is deprecated.  Use panda_move-srv:execute_state instead.")
  (execute_state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Hand-response>) ostream)
  "Serializes a message object of type '<Hand-response>"
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Hand-response>) istream)
  "Deserializes a message object of type '<Hand-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Hand-response>)))
  "Returns string type for a service object of type '<Hand-response>"
  "panda_move/HandResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Hand-response)))
  "Returns string type for a service object of type 'Hand-response"
  "panda_move/HandResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Hand-response>)))
  "Returns md5sum for a message object of type '<Hand-response>"
  "90c7acc194a7a7121ca85308c4242240")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Hand-response)))
  "Returns md5sum for a message object of type 'Hand-response"
  "90c7acc194a7a7121ca85308c4242240")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Hand-response>)))
  "Returns full string definition for message of type '<Hand-response>"
  (cl:format cl:nil "int64 execute_state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Hand-response)))
  "Returns full string definition for message of type 'Hand-response"
  (cl:format cl:nil "int64 execute_state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Hand-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Hand-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Hand-response
    (cl:cons ':execute_state (execute_state msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Hand)))
  'Hand-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Hand)))
  'Hand-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Hand)))
  "Returns string type for a service object of type '<Hand>"
  "panda_move/Hand")