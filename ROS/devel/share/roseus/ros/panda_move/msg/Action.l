;; Auto-generated. Do not edit!


(when (boundp 'panda_move::Action)
  (if (not (find-package "PANDA_MOVE"))
    (make-package "PANDA_MOVE"))
  (shadow 'Action (find-package "PANDA_MOVE")))
(unless (find-package "PANDA_MOVE::ACTION")
  (make-package "PANDA_MOVE::ACTION"))

(in-package "ROS")
;;//! \htmlinclude Action.msg.html


(defclass panda_move::Action
  :super ros::object
  :slots (_name _params ))

(defmethod panda_move::Action
  (:init
   (&key
    ((:name __name) "")
    ((:params __params) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _params __params)
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:params
   (&optional __params)
   (if __params (setq _params __params)) _params)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; string[] _params
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _params)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; string[] _params
     (write-long (length _params) s)
     (dolist (elem _params)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string[] _params
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _params (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _params i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(setf (get panda_move::Action :md5sum-) "166bf98220d35af21b0a4502a84afab1")
(setf (get panda_move::Action :datatype-) "panda_move/Action")
(setf (get panda_move::Action :definition-)
      "string name
string[] params
")



(provide :panda_move/Action "166bf98220d35af21b0a4502a84afab1")


