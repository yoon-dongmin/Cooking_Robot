// Auto-generated. Do not edit!

// (in-package panda_move.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Action = require('../msg/Action.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class ActionSequencesRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.action_sequences = null;
    }
    else {
      if (initObj.hasOwnProperty('action_sequences')) {
        this.action_sequences = initObj.action_sequences
      }
      else {
        this.action_sequences = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ActionSequencesRequest
    // Serialize message field [action_sequences]
    // Serialize the length for message field [action_sequences]
    bufferOffset = _serializer.uint32(obj.action_sequences.length, buffer, bufferOffset);
    obj.action_sequences.forEach((val) => {
      bufferOffset = Action.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ActionSequencesRequest
    let len;
    let data = new ActionSequencesRequest(null);
    // Deserialize message field [action_sequences]
    // Deserialize array length for message field [action_sequences]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.action_sequences = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.action_sequences[i] = Action.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.action_sequences.forEach((val) => {
      length += Action.getMessageSize(val);
    });
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'panda_move/ActionSequencesRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'aca026e1261af957e6a9d1e4f1f468ef';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    panda_move/Action[] action_sequences
    
    ================================================================================
    MSG: panda_move/Action
    string name
    string[] params
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ActionSequencesRequest(null);
    if (msg.action_sequences !== undefined) {
      resolved.action_sequences = new Array(msg.action_sequences.length);
      for (let i = 0; i < resolved.action_sequences.length; ++i) {
        resolved.action_sequences[i] = Action.Resolve(msg.action_sequences[i]);
      }
    }
    else {
      resolved.action_sequences = []
    }

    return resolved;
    }
};

class ActionSequencesResponse {
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
    // Serializes a message object of type ActionSequencesResponse
    // Serialize message field [result]
    bufferOffset = _serializer.bool(obj.result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ActionSequencesResponse
    let len;
    let data = new ActionSequencesResponse(null);
    // Deserialize message field [result]
    data.result = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'panda_move/ActionSequencesResponse';
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
    const resolved = new ActionSequencesResponse(null);
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
  Request: ActionSequencesRequest,
  Response: ActionSequencesResponse,
  md5sum() { return '078ea5c2edc52b36bc1237b7034dab03'; },
  datatype() { return 'panda_move/ActionSequences'; }
};
