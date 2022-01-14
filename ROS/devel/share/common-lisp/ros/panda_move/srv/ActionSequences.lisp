; Auto-generated. Do not edit!


(cl:in-package panda_move-srv)


;//! \htmlinclude ActionSequences-request.msg.html

(cl:defclass <ActionSequences-request> (roslisp-msg-protocol:ros-message)
  ((action_sequences
    :reader action_sequences
    :initarg :action_sequences
    :type (cl:vector panda_move-msg:Action)
   :initform (cl:make-array 0 :element-type 'panda_move-msg:Action :initial-element (cl:make-instance 'panda_move-msg:Action))))
)

(cl:defclass ActionSequences-request (<ActionSequences-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ActionSequences-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ActionSequences-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name panda_move-srv:<ActionSequences-request> is deprecated: use panda_move-srv:ActionSequences-request instead.")))

(cl:ensure-generic-function 'action_sequences-val :lambda-list '(m))
(cl:defmethod action_sequences-val ((m <ActionSequences-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panda_move-srv:action_sequences-val is deprecated.  Use panda_move-srv:action_sequences instead.")
  (action_sequences m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ActionSequences-request>) ostream)
  "Serializes a message object of type '<ActionSequences-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'action_sequences))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'action_sequences))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ActionSequences-request>) istream)
  "Deserializes a message object of type '<ActionSequences-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'action_sequences) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'action_sequences)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'panda_move-msg:Action))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ActionSequences-request>)))
  "Returns string type for a service object of type '<ActionSequences-request>"
  "panda_move/ActionSequencesRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActionSequences-request)))
  "Returns string type for a service object of type 'ActionSequences-request"
  "panda_move/ActionSequencesRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ActionSequences-request>)))
  "Returns md5sum for a message object of type '<ActionSequences-request>"
  "078ea5c2edc52b36bc1237b7034dab03")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ActionSequences-request)))
  "Returns md5sum for a message object of type 'ActionSequences-request"
  "078ea5c2edc52b36bc1237b7034dab03")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ActionSequences-request>)))
  "Returns full string definition for message of type '<ActionSequences-request>"
  (cl:format cl:nil "panda_move/Action[] action_sequences~%~%================================================================================~%MSG: panda_move/Action~%string name~%string[] params~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ActionSequences-request)))
  "Returns full string definition for message of type 'ActionSequences-request"
  (cl:format cl:nil "panda_move/Action[] action_sequences~%~%================================================================================~%MSG: panda_move/Action~%string name~%string[] params~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ActionSequences-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'action_sequences) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ActionSequences-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ActionSequences-request
    (cl:cons ':action_sequences (action_sequences msg))
))
;//! \htmlinclude ActionSequences-response.msg.html

(cl:defclass <ActionSequences-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass ActionSequences-response (<ActionSequences-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ActionSequences-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ActionSequences-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name panda_move-srv:<ActionSequences-response> is deprecated: use panda_move-srv:ActionSequences-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <ActionSequences-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panda_move-srv:result-val is deprecated.  Use panda_move-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ActionSequences-response>) ostream)
  "Serializes a message object of type '<ActionSequences-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ActionSequences-response>) istream)
  "Deserializes a message object of type '<ActionSequences-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ActionSequences-response>)))
  "Returns string type for a service object of type '<ActionSequences-response>"
  "panda_move/ActionSequencesResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActionSequences-response)))
  "Returns string type for a service object of type 'ActionSequences-response"
  "panda_move/ActionSequencesResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ActionSequences-response>)))
  "Returns md5sum for a message object of type '<ActionSequences-response>"
  "078ea5c2edc52b36bc1237b7034dab03")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ActionSequences-response)))
  "Returns md5sum for a message object of type 'ActionSequences-response"
  "078ea5c2edc52b36bc1237b7034dab03")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ActionSequences-response>)))
  "Returns full string definition for message of type '<ActionSequences-response>"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ActionSequences-response)))
  "Returns full string definition for message of type 'ActionSequences-response"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ActionSequences-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ActionSequences-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ActionSequences-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ActionSequences)))
  'ActionSequences-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ActionSequences)))
  'ActionSequences-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActionSequences)))
  "Returns string type for a service object of type '<ActionSequences>"
  "panda_move/ActionSequences")