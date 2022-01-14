// Auto-generated. Do not edit!

// (in-package panda_move.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class SyncRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.activated_object = null;
    }
    else {
      if (initObj.hasOwnProperty('activated_object')) {
        this.activated_object = initObj.activated_object
      }
      else {
        this.activated_object = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SyncRequest
    // Serialize message field [activated_object]
    bufferOffset = _arraySerializer.string(obj.activated_object, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SyncRequest
    let len;
    let data = new SyncRequest(null);
    // Deserialize message field [activated_object]
    data.activated_object = _arrayDeserializer.string(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.activated_object.forEach((val) => {
      length += 4 + val.length;
    });
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'panda_move/SyncRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5ccce85bd5755620147c0f5ba89d5c03';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string[] activated_object
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SyncRequest(null);
    if (msg.activated_object !== undefined) {
      resolved.activated_object = msg.activated_object;
    }
    else {
      resolved.activated_object = []
    }

    return resolved;
    }
};

class SyncResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.object_name = null;
      this.position = null;
      this.orientation = null;
      this.joint_state = null;
    }
    else {
      if (initObj.hasOwnProperty('object_name')) {
        this.object_name = initObj.object_name
      }
      else {
        this.object_name = [];
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
      if (initObj.hasOwnProperty('joint_state')) {
        this.joint_state = initObj.joint_state
      }
      else {
        this.joint_state = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SyncResponse
    // Serialize message field [object_name]
    bufferOffset = _arraySerializer.string(obj.object_name, buffer, bufferOffset, null);
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
    // Serialize message field [joint_state]
    bufferOffset = _arraySerializer.float64(obj.joint_state, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SyncResponse
    let len;
    let data = new SyncResponse(null);
    // Deserialize message field [object_name]
    data.object_name = _arrayDeserializer.string(buffer, bufferOffset, null)
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
    // Deserialize message field [joint_state]
    data.joint_state = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.object_name.forEach((val) => {
      length += 4 + val.length;
    });
    length += 24 * object.position.length;
    length += 32 * object.orientation.length;
    length += 8 * object.joint_state.length;
    return length + 16;
  }

  static datatype() {
    // Returns string type for a service object
    return 'panda_move/SyncResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '118b22079c9a9e717f3c182246de032c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string[] object_name
    geometry_msgs/Point[] position
    geometry_msgs/Quaternion[] orientation
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SyncResponse(null);
    if (msg.object_name !== undefined) {
      resolved.object_name = msg.object_name;
    }
    else {
      resolved.object_name = []
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

    if (msg.joint_state !== undefined) {
      resolved.joint_state = msg.joint_state;
    }
    else {
      resolved.joint_state = []
    }

    return resolved;
    }
};

module.exports = {
  Request: SyncRequest,
  Response: SyncResponse,
  md5sum() { return 'd850a51077e21c58d4f7667e1676cebc'; },
  datatype() { return 'panda_move/Sync'; }
};
