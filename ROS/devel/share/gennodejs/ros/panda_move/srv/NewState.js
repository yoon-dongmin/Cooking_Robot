// Auto-generated. Do not edit!

// (in-package panda_move.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Predicate = require('../msg/Predicate.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class NewStateRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.new_state = null;
    }
    else {
      if (initObj.hasOwnProperty('new_state')) {
        this.new_state = initObj.new_state
      }
      else {
        this.new_state = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type NewStateRequest
    // Serialize message field [new_state]
    // Serialize the length for message field [new_state]
    bufferOffset = _serializer.uint32(obj.new_state.length, buffer, bufferOffset);
    obj.new_state.forEach((val) => {
      bufferOffset = Predicate.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type NewStateRequest
    let len;
    let data = new NewStateRequest(null);
    // Deserialize message field [new_state]
    // Deserialize array length for message field [new_state]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.new_state = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.new_state[i] = Predicate.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.new_state.forEach((val) => {
      length += Predicate.getMessageSize(val);
    });
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'panda_move/NewStateRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd9923c8d2a4b7b22cd97fde815a9ab05';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    panda_move/Predicate[] new_state
    
    ================================================================================
    MSG: panda_move/Predicate
    string name
    string[] params
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new NewStateRequest(null);
    if (msg.new_state !== undefined) {
      resolved.new_state = new Array(msg.new_state.length);
      for (let i = 0; i < resolved.new_state.length; ++i) {
        resolved.new_state[i] = Predicate.Resolve(msg.new_state[i]);
      }
    }
    else {
      resolved.new_state = []
    }

    return resolved;
    }
};

class NewStateResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.result = null;
    }
    else {
      if (initObj.hasOwnProperty('result')) {
        this.result = initObj.result
      }
      else {
        this.result = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type NewStateResponse
    // Serialize message field [result]
    bufferOffset = _serializer.bool(obj.result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type NewStateResponse
    let len;
    let data = new NewStateResponse(null);
    // Deserialize message field [result]
    data.result = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'panda_move/NewStateResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'eb13ac1f1354ccecb7941ee8fa2192e8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool result
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new NewStateResponse(null);
    if (msg.result !== undefined) {
      resolved.result = msg.result;
    }
    else {
      resolved.result = false
    }

    return resolved;
    }
};

module.exports = {
  Request: NewStateRequest,
  Response: NewStateResponse,
  md5sum() { return '92d4a807a3e01f714a92618d52a8f78f'; },
  datatype() { return 'panda_move/NewState'; }
};
