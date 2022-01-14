// Auto-generated. Do not edit!

// (in-package panda_move.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------


//-----------------------------------------------------------

class InitRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.activated_object = null;
      this.position = null;
      this.orientation = null;
      this.scale = null;
      this.joint_state = null;
    }
    else {
      if (initObj.hasOwnProperty('activated_object')) {
        this.activated_object = initObj.activated_object
      }
      else {
        this.activated_object = [];
      }
      if (initObj.hasOwnProperty('position')) {
        this.position = initObj.position
      }
      else {
        this.position = [];
      }
      if (initObj.hasOwnProperty('orientation')) {
        this.orientation = initObj.orientation
      }
      else {
        this.orientation = [];
      }
      if (initObj.hasOwnProperty('scale')) {
        this.scale = initObj.scale
      }
      else {
        this.scale = [];
      }
      if (initObj.hasOwnProperty('joint_state')) {
        this.joint_state = initObj.joint_state
      }
      else {
        this.joint_state = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type InitRequest
    // Serialize message field [activated_object]
    bufferOffset = _arraySerializer.string(obj.activated_object, buffer, bufferOffset, null);
    // Serialize message field [position]
    // Serialize the length for message field [position]
    bufferOffset = _serializer.uint32(obj.position.length, buffer, bufferOffset);
    obj.position.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Point.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [orientation]
    // Serialize the length for message field [orientation]
    bufferOffset = _serializer.uint32(obj.orientation.length, buffer, bufferOffset);
    obj.orientation.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Quaternion.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [scale]
    // Serialize the length for message field [scale]
    bufferOffset = _serializer.uint32(obj.scale.length, buffer, bufferOffset);
    obj.scale.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Vector3.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [joint_state]
    bufferOffset = _arraySerializer.float64(obj.joint_state, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type InitRequest
    let len;
    let data = new InitRequest(null);
    // Deserialize message field [activated_object]
    data.activated_object = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [position]
    // Deserialize array length for message field [position]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.position = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.position[i] = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [orientation]
    // Deserialize array length for message field [orientation]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.orientation = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.orientation[i] = geometry_msgs.msg.Quaternion.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [scale]
    // Deserialize array length for message field [scale]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.scale = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.scale[i] = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [joint_state]
    data.joint_state = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.activated_object.forEach((val) => {
      length += 4 + val.length;
    });
    length += 24 * object.position.length;
    length += 32 * object.orientation.length;
    length += 24 * object.scale.length;
    length += 8 * object.joint_state.length;
    return length + 20;
  }

  static datatype() {
    // Returns string type for a service object
    return 'panda_move/InitRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3ddc831ca2bee40010e5808350701489';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string[] activated_object
    geometry_msgs/Point[] position
    geometry_msgs/Quaternion[] orientation
    geometry_msgs/Vector3[] scale
    float64[] joint_state
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    ================================================================================
    MSG: geometry_msgs/Vector3
    # This represents a vector in free space. 
    # It is only meant to represent a direction. Therefore, it does not
    # make sense to apply a translation to it (e.g., when applying a 
    # generic rigid transformation to a Vector3, tf2 will only apply the
    # rotation). If you want your data to be translatable too, use the
    # geometry_msgs/Point message instead.
    
    float64 x
    float64 y
    float64 z
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new InitRequest(null);
    if (msg.activated_object !== undefined) {
      resolved.activated_object = msg.activated_object;
    }
    else {
      resolved.activated_object = []
    }

    if (msg.position !== undefined) {
      resolved.position = new Array(msg.position.length);
      for (let i = 0; i < resolved.position.length; ++i) {
        resolved.position[i] = geometry_msgs.msg.Point.Resolve(msg.position[i]);
      }
    }
    else {
      resolved.position = []
    }

    if (msg.orientation !== undefined) {
      resolved.orientation = new Array(msg.orientation.length);
      for (let i = 0; i < resolved.orientation.length; ++i) {
        resolved.orientation[i] = geometry_msgs.msg.Quaternion.Resolve(msg.orientation[i]);
      }
    }
    else {
      resolved.orientation = []
    }

    if (msg.scale !== undefined) {
      resolved.scale = new Array(msg.scale.length);
      for (let i = 0; i < resolved.scale.length; ++i) {
        resolved.scale[i] = geometry_msgs.msg.Vector3.Resolve(msg.scale[i]);
      }
    }
    else {
      resolved.scale = []
    }

    if (msg.joint_state !== undefined) {
      resolved.joint_state = msg.joint_state;
    }
    else {
      resolved.joint_state = []
    }

    return resolved;
    }
};

class InitResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.init_state = null;
    }
    else {
      if (initObj.hasOwnProperty('init_state')) {
        this.init_state = initObj.init_state
      }
      else {
        this.init_state = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type InitResponse
    // Serialize message field [init_state]
    bufferOffset = _serializer.int64(obj.init_state, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type InitResponse
    let len;
    let data = new InitResponse(null);
    // Deserialize message field [init_state]
    data.init_state = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'panda_move/InitResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a848b0441b20a5cbb45558b3d0978950';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 init_state
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new InitResponse(null);
    if (msg.init_state !== undefined) {
      resolved.init_state = msg.init_state;
    }
    else {
      resolved.init_state = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: InitRequest,
  Response: InitResponse,
  md5sum() { return '73f72d80c9600a1ec553e98d0e61c060'; },
  datatype() { return 'panda_move/Init'; }
};
