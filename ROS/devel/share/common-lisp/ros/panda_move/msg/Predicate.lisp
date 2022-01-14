; Auto-generated. Do not edit!


(cl:in-package panda_move-msg)


;//! \htmlinclude Predicate.msg.html

(cl:defclass <Predicate> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (params
    :reader params
    :initarg :params
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element "")))
)

(cl:defclass Predicate (<Predicate>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Predicate>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Predicate)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name panda_move-msg:<Predicate> is deprecated: use panda_move-msg:Predicate instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <Predicate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panda_move-msg:name-val is deprecated.  Use panda_move-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'params-val :lambda-list '(m))
(cl:defmethod params-val ((m <Predicate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panda_move-msg:params-val is deprecated.  Use panda_move-msg:params instead.")
  (params m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Predicate>) ostream)
  "Serializes a message object of type '<Predicate>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'params))))
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
   (cl:slot-value msg 'params))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Predicate>) istream)
  "Deserializes a message object of type '<Predicate>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'params) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'params)))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Predicate>)))
  "Returns string type for a message object of type '<Predicate>"
  "panda_move/Predicate")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Predicate)))
  "Returns string type for a message object of type 'Predicate"
  "panda_move/Predicate")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Predicate>)))
  "Returns md5sum for a message object of type '<Predicate>"
  "166bf98220d35af21b0a4502a84afab1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Predicate)))
  "Returns md5sum for a message object of type 'Predicate"
  "166bf98220d35af21b0a4502a84afab1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Predicate>)))
  "Returns full string definition for message of type '<Predicate>"
  (cl:format cl:nil "string name~%string[] params~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Predicate)))
  "Returns full string definition for message of type 'Predicate"
  (cl:format cl:nil "string name~%string[] params~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Predicate>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'params) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Predicate>))
  "Converts a ROS message object to a list"
  (cl:list 'Predicate
    (cl:cons ':name (name msg))
    (cl:cons ':params (params msg))
))
