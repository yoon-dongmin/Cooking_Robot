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

class HandRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.grasp_state = null;
      this.object_name = null;
      this.grasp_size = null;
    }
    else {
      if (initObj.hasOwnProperty('grasp_state')) {
        this.grasp_state = initObj.grasp_state
      }
      else {
        this.grasp_state = false;
      }
      if (initObj.hasOwnProperty('object_name')) {
        this.object_name = initObj.object_name
      }
      else {
        this.object_name = '';
      }
      if (initObj.hasOwnProperty('grasp_size')) {
        this.grasp_size = initObj.grasp_size
      }
      else {
        this.grasp_size = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type HandRequest
    // Serialize message field [grasp_state]
    bufferOffset = _serializer.bool(obj.grasp_state, buffer, bufferOffset);
    // Serialize message field [object_name]
    bufferOffset = _serializer.string(obj.object_name, buffer, bufferOffset);
    // Serialize message field [grasp_size]
    bufferOffset = _serializer.float64(obj.grasp_size, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type HandRequest
    let len;
    let data = new HandRequest(null);
    // Deserialize message field [grasp_state]
    data.grasp_state = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [object_name]
    data.object_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [grasp_size]
    data.grasp_size = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.object_name.length;
    return length + 13;
  }

  static datatype() {
    // Returns string type for a service object
    return 'panda_move/HandRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3bca6d146ab3600c7e3fb19e63f1ad58';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool grasp_state
    string object_name
    float64 grasp_size
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new HandRequest(null);
    if (msg.grasp_state !== undefined) {
      resolved.grasp_state = msg.grasp_state;
    }
    else {
      resolved.grasp_state = false
    }

    if (msg.object_name !== undefined) {
      resolved.object_name = msg.object_name;
    }
    else {
      resolved.object_name = ''
    }

    if (msg.grasp_size !== undefined) {
      resolved.grasp_size = msg.grasp_size;
    }
    else {
      resolved.grasp_size = 0.0
    }

    return resolved;
    }
};

class HandResponse {
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
    // Serializes a message object of type HandResponse
    // Serialize message field [execute_state]
    bufferOffset = _serializer.int64(obj.execute_state, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type HandResponse
    let len;
    let data = new HandResponse(null);
    // Deserialize message field [execute_state]
    data.execute_state = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'panda_move/HandResponse';
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
    const resolved = new HandResponse(null);
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
  Request: HandRequest,
  Response: HandResponse,
  md5sum() { return '90c7acc194a7a7121ca85308c4242240'; },
  datatype() { return 'panda_move/Hand'; }
};
