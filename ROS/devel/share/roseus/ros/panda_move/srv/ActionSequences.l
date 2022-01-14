;; Auto-generated. Do not edit!


(when (boundp 'panda_move::ActionSequences)
  (if (not (find-package "PANDA_MOVE"))
    (make-package "PANDA_MOVE"))
  (shadow 'ActionSequences (find-package "PANDA_MOVE")))
(unless (find-package "PANDA_MOVE::ACTIONSEQUENCES")
  (make-package "PANDA_MOVE::ACTIONSEQUENCES"))
(unless (find-package "PANDA_MOVE::ACTIONSEQUENCESREQUEST")
  (make-package "PANDA_MOVE::ACTIONSEQUENCESREQUEST"))
(unless (find-package "PANDA_MOVE::ACTIONSEQUENCESRESPONSE")
  (make-package "PANDA_MOVE::ACTIONSEQUENCESRESPONSE"))

(in-package "ROS")





(defclass panda_move::ActionSequencesRequest
  :super ros::object
  :slots (_action_sequences ))

(defmethod panda_move::ActionSequencesRequest
  (:init
   (&key
    ((:action_sequences __action_sequences) (let (r) (dotimes (i 0) (push (instance panda_move::Action :init) r)) r))
    )
   (send-super :init)
   (setq _action_sequences __action_sequences)
   self)
  (:action_sequences
   (&rest __action_sequences)
   (if (keywordp (car __action_sequences))
       (send* _action_sequences __action_sequences)
     (progn
       (if __action_sequences (setq _action_sequences (car __action_sequences)))
       _action_sequences)))
  (:serialization-length
   ()
   (+
    ;; panda_move/Action[] _action_sequences
    (apply #'+ (send-all _action_sequences :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; panda_move/Action[] _action_sequences
     (write-long (length _action_sequences) s)
     (dolist (elem _action_sequences)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; panda_move/Action[] _action_sequences
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _action_sequences (let (r) (dotimes (i n) (push (instance panda_move::Action :init) r)) r))
     (dolist (elem- _action_sequences)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(defclass panda_move::ActionSequencesResponse
  :super ros::object
  :slots (_result ))

(defmethod panda_move::ActionSequencesResponse
  (:init
   (&key
    ((:result __result) nil)
    )
   (send-super :init)
   (setq _result __result)
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; bool _result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _result
       (if _result (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _result
     (setq _result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass panda_move::ActionSequences
  :super ros::object
  :slots ())

(setf (get panda_move::ActionSequences :md5sum-) "078ea5c2edc52b36bc1237b7034dab03")
(setf (get panda_move::ActionSequences :datatype-) "panda_move/ActionSequences")
(setf (get panda_move::ActionSequences :request) panda_move::ActionSequencesRequest)
(setf (get panda_move::ActionSequences :response) panda_move::ActionSequencesResponse)

(defmethod panda_move::ActionSequencesRequest
  (:response () (instance panda_move::ActionSequencesResponse :init)))

(setf (get panda_move::ActionSequencesRequest :md5sum-) "078ea5c2edc52b36bc1237b7034dab03")
(setf (get panda_move::ActionSequencesRequest :datatype-) "panda_move/ActionSequencesRequest")
(setf (get panda_move::ActionSequencesRequest :definition-)
      "panda_move/Action[] action_sequences

================================================================================
MSG: panda_move/Action
string name
---
bool result
")

(setf (get panda_move::ActionSequencesResponse :md5sum-) "078ea5c2edc52b36bc1237b7034dab03")
(setf (get panda_move::ActionSequencesResponse :datatype-) "panda_move/ActionSequencesResponse")
(setf (get panda_move::ActionSequencesResponse :definition-)
      "panda_move/Action[] action_sequences

================================================================================
MSG: panda_move/Action
string name
---
bool result
")



(provide :panda_move/ActionSequences "078ea5c2edc52b36bc1237b7034dab03")


