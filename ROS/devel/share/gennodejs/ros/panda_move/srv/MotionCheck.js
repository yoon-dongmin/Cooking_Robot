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


//-----------------------------------------------------------

class MotionCheckRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.motion_type = null;
      this.object_1 = null;
      this.object_2 = null;
    }
    else {
      if (initObj.hasOwnProperty('motion_type')) {
        this.motion_type = initObj.motion_type
      }
      else {
        this.motion_type = '';
      }
      if (initObj.hasOwnProperty('object_1')) {
        this.object_1 = initObj.object_1
      }
      else {
        this.object_1 = [];
      }
      if (initObj.hasOwnProperty('object_2')) {
        this.object_2 = initObj.object_2
      }
      else {
        this.object_2 = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MotionCheckRequest
    // Serialize message field [motion_type]
    bufferOffset = _serializer.string(obj.motion_type, buffer, bufferOffset);
    // Serialize message field [object_1]
    bufferOffset = _arraySerializer.string(obj.object_1, buffer, bufferOffset, null);
    // Serialize message field [object_2]
    bufferOffset = _arraySerializer.string(obj.object_2, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MotionCheckRequest
    let len;
    let data = new MotionCheckRequest(null);
    // Deserialize message field [motion_type]
    data.motion_type = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [object_1]
    data.object_1 = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [object_2]
    data.object_2 = _arrayDeserializer.string(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.motion_type.length;
    object.object_1.forEach((val) => {
      length += 4 + val.length;
    });
    object.object_2.forEach((val) => {
      length += 4 + val.length;
    });
    return length + 12;
  }

  static datatype() {
    // Returns string type for a service object
    return 'panda_move/MotionCheckRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0baa49dd0a199f18dcbca155877942b7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string motion_type
    string[] object_1
    string[] object_2
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MotionCheckRequest(null);
    if (msg.motion_type !== undefined) {
      resolved.motion_type = msg.motion_type;
    }
    else {
      resolved.motion_type = ''
    }

    if (msg.object_1 !== undefined) {
      resolved.object_1 = msg.object_1;
    }
    else {
      resolved.object_1 = []
    }

    if (msg.object_2 !== undefined) {
      resolved.object_2 = msg.object_2;
    }
    else {
      resolved.object_2 = []
    }

    return resolved;
    }
};

class MotionCheckResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.execute_state = null;
    }
    else {
      if (initObj.hasOwnProperty('execute_state')) {
        this.execute_state = initObj.execute_state
      }
      else {
        this.execute_state = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MotionCheckResponse
    // Serialize message field [execute_state]
    bufferOffset = _serializer.int64(obj.execute_state, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MotionCheckResponse
    let len;
    let data = new MotionCheckResponse(null);
    // Deserialize message field [execute_state]
    data.execute_state = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'panda_move/MotionCheckResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '9e5da242623a66ea9b9fa2f917d3d039';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 execute_state
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MotionCheckResponse(null);
    if (msg.execute_state !== undefined) {
      resolved.execute_state = msg.execute_state;
    }
    else {
      resolved.execute_state = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: MotionCheckRequest,
  Response: MotionCheckResponse,
  md5sum() { return 'f3ead81734321a8717b9ae871d1b0fcb'; },
  datatype() { return 'panda_move/MotionCheck'; }
};
