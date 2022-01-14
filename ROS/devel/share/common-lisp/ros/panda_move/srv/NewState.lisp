; Auto-generated. Do not edit!


(cl:in-package panda_move-srv)


;//! \htmlinclude NewState-request.msg.html

(cl:defclass <NewState-request> (roslisp-msg-protocol:ros-message)
  ((new_state
    :reader new_state
    :initarg :new_state
    :type (cl:vector panda_move-msg:Predicate)
   :initform (cl:make-array 0 :element-type 'panda_move-msg:Predicate :initial-element (cl:make-instance 'panda_move-msg:Predicate))))
)

(cl:defclass NewState-request (<NewState-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <NewState-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'NewState-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name panda_move-srv:<NewState-request> is deprecated: use panda_move-srv:NewState-request instead.")))

(cl:ensure-generic-function 'new_state-val :lambda-list '(m))
(cl:defmethod new_state-val ((m <NewState-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panda_move-srv:new_state-val is deprecated.  Use panda_move-srv:new_state instead.")
  (new_state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <NewState-request>) ostream)
  "Serializes a message object of type '<NewState-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'new_state))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'new_state))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <NewState-request>) istream)
  "Deserializes a message object of type '<NewState-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'new_state) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'new_state)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'panda_move-msg:Predicate))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<NewState-request>)))
  "Returns string type for a service object of type '<NewState-request>"
  "panda_move/NewStateRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'NewState-request)))
  "Returns string type for a service object of type 'NewState-request"
  "panda_move/NewStateRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<NewState-request>)))
  "Returns md5sum for a message object of type '<NewState-request>"
  "92d4a807a3e01f714a92618d52a8f78f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'NewState-request)))
  "Returns md5sum for a message object of type 'NewState-request"
  "92d4a807a3e01f714a92618d52a8f78f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<NewState-request>)))
  "Returns full string definition for message of type '<NewState-request>"
  (cl:format cl:nil "panda_move/Predicate[] new_state~%~%================================================================================~%MSG: panda_move/Predicate~%string name~%string[] params~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'NewState-request)))
  "Returns full string definition for message of type 'NewState-request"
  (cl:format cl:nil "panda_move/Predicate[] new_state~%~%================================================================================~%MSG: panda_move/Predicate~%string name~%string[] params~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <NewState-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'new_state) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <NewState-request>))
  "Converts a ROS message object to a list"
  (cl:list 'NewState-request
    (cl:cons ':new_state (new_state msg))
))
;//! \htmlinclude NewState-response.msg.html

(cl:defclass <NewState-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass NewState-response (<NewState-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <NewState-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'NewState-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name panda_move-srv:<NewState-response> is deprecated: use panda_move-srv:NewState-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <NewState-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panda_move-srv:result-val is deprecated.  Use panda_move-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <NewState-response>) ostream)
  "Serializes a message object of type '<NewState-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <NewState-response>) istream)
  "Deserializes a message object of type '<NewState-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<NewState-response>)))
  "Returns string type for a service object of type '<NewState-response>"
  "panda_move/NewStateResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'NewState-response)))
  "Returns string type for a service object of type 'NewState-response"
  "panda_move/NewStateResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<NewState-response>)))
  "Returns md5sum for a message object of type '<NewState-response>"
  "92d4a807a3e01f714a92618d52a8f78f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'NewState-response)))
  "Returns md5sum for a message object of type 'NewState-response"
  "92d4a807a3e01f714a92618d52a8f78f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<NewState-response>)))
  "Returns full string definition for message of type '<NewState-response>"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'NewState-response)))
  "Returns full string definition for message of type 'NewState-response"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <NewState-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <NewState-response>))
  "Converts a ROS message object to a list"
  (cl:list 'NewState-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'NewState)))
  'NewState-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'NewState)))
  'NewState-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'NewState)))
  "Returns string type for a service object of type '<NewState>"
  "panda_move/NewState")