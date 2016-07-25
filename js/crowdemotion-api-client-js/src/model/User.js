/**
 * CloudEmotion API v1
 * CrowdEmotion API
 *
 * OpenAPI spec version: 1.1.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.CrowdemotionApiClientJs) {
      root.CrowdemotionApiClientJs = {};
    }
    root.CrowdemotionApiClientJs.User = factory(root.CrowdemotionApiClientJs.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The User model module.
   * @module model/User
   * @version 1.1.0
   */

  /**
   * Constructs a new <code>User</code>.
   * @alias module:model/User
   * @class
   * @param id {Integer} 
   * @param numId {Integer} 
   * @param uuid {String} 
   * @param emailAddress {String} 
   * @param firstName {String} 
   * @param lastName {String} 
   * @param role {String} 
   * @param username {String} 
   * @param groupId {Integer} 
   * @param companyId {Integer} 
   * @param verified {Boolean} 
   * @param enabled {Boolean} 
   */
  var exports = function(id, numId, uuid, emailAddress, firstName, lastName, role, username, groupId, companyId, verified, enabled) {
    var _this = this;

    _this['id'] = id;
    _this['numId'] = numId;
    _this['uuid'] = uuid;
    _this['emailAddress'] = emailAddress;
    _this['firstName'] = firstName;
    _this['lastName'] = lastName;
    _this['role'] = role;
    _this['username'] = username;
    _this['group_id'] = groupId;
    _this['company_id'] = companyId;
    _this['verified'] = verified;
    _this['enabled'] = enabled;
  };

  /**
   * Constructs a <code>User</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/User} obj Optional instance to populate.
   * @return {module:model/User} The populated <code>User</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('id')) {
        obj['id'] = ApiClient.convertToType(data['id'], 'Integer');
      }
      if (data.hasOwnProperty('numId')) {
        obj['numId'] = ApiClient.convertToType(data['numId'], 'Integer');
      }
      if (data.hasOwnProperty('uuid')) {
        obj['uuid'] = ApiClient.convertToType(data['uuid'], 'String');
      }
      if (data.hasOwnProperty('emailAddress')) {
        obj['emailAddress'] = ApiClient.convertToType(data['emailAddress'], 'String');
      }
      if (data.hasOwnProperty('firstName')) {
        obj['firstName'] = ApiClient.convertToType(data['firstName'], 'String');
      }
      if (data.hasOwnProperty('lastName')) {
        obj['lastName'] = ApiClient.convertToType(data['lastName'], 'String');
      }
      if (data.hasOwnProperty('role')) {
        obj['role'] = ApiClient.convertToType(data['role'], 'String');
      }
      if (data.hasOwnProperty('username')) {
        obj['username'] = ApiClient.convertToType(data['username'], 'String');
      }
      if (data.hasOwnProperty('group_id')) {
        obj['group_id'] = ApiClient.convertToType(data['group_id'], 'Integer');
      }
      if (data.hasOwnProperty('company_id')) {
        obj['company_id'] = ApiClient.convertToType(data['company_id'], 'Integer');
      }
      if (data.hasOwnProperty('verified')) {
        obj['verified'] = ApiClient.convertToType(data['verified'], 'Boolean');
      }
      if (data.hasOwnProperty('enabled')) {
        obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
      }
    }
    return obj;
  }

  /**
   * 
   * @member {Integer} id
   */
  exports.prototype['id'] = undefined;
  /**
   * 
   * @member {Integer} numId
   */
  exports.prototype['numId'] = undefined;
  /**
   * 
   * @member {String} uuid
   */
  exports.prototype['uuid'] = undefined;
  /**
   * 
   * @member {String} emailAddress
   */
  exports.prototype['emailAddress'] = undefined;
  /**
   * 
   * @member {String} firstName
   */
  exports.prototype['firstName'] = undefined;
  /**
   * 
   * @member {String} lastName
   */
  exports.prototype['lastName'] = undefined;
  /**
   * 
   * @member {String} role
   */
  exports.prototype['role'] = undefined;
  /**
   * 
   * @member {String} username
   */
  exports.prototype['username'] = undefined;
  /**
   * 
   * @member {Integer} group_id
   */
  exports.prototype['group_id'] = undefined;
  /**
   * 
   * @member {Integer} company_id
   */
  exports.prototype['company_id'] = undefined;
  /**
   * 
   * @member {Boolean} verified
   */
  exports.prototype['verified'] = undefined;
  /**
   * 
   * @member {Boolean} enabled
   */
  exports.prototype['enabled'] = undefined;



  return exports;
}));

