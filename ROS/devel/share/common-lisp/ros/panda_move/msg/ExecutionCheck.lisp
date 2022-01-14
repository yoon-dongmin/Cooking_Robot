; Auto-generated. Do not edit!


(cl:in-package panda_move-msg)


;//! \htmlinclude ExecutionCheck.msg.html

(cl:defclass <ExecutionCheck> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:integer
    :initform 0))
)

(cl:defclass ExecutionCheck (<ExecutionCheck>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ExecutionCheck>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ExecutionCheck)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name panda_move-msg:<ExecutionCheck> is deprecated: use panda_move-msg:ExecutionCheck instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <ExecutionCheck>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panda_move-msg:status-val is deprecated.  Use panda_move-msg:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ExecutionCheck>) ostream)
  "Serializes a message object of type '<ExecutionCheck>"
  (cl:let* ((signed (cl:slot-value msg 'status)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ExecutionCheck>) istream)
  "Deserializes a message object of type '<ExecutionCheck>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'status) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ExecutionCheck>)))
  "Returns string type for a message object of type '<ExecutionCheck>"
  "panda_move/ExecutionCheck")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExecutionCheck)))
  "Returns string type for a message object of type 'ExecutionCheck"
  "panda_move/ExecutionCheck")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ExecutionCheck>)))
  "Returns md5sum for a message object of type '<ExecutionCheck>"
  "4107476a6271fc2684d94be17d33f854")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ExecutionCheck)))
  "Returns md5sum for a message object of type 'ExecutionCheck"
  "4107476a6271fc2684d94be17d33f854")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ExecutionCheck>)))
  "Returns full string definition for message of type '<ExecutionCheck>"
  (cl:format cl:nil "int64 status~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ExecutionCheck)))
  "Returns full string definition for message of type 'ExecutionCheck"
  (cl:format cl:nil "int64 status~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ExecutionCheck>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ExecutionCheck>))
  "Converts a ROS message object to a list"
  (cl:list 'ExecutionCheck
    (cl:cons ':status (status msg))
))
