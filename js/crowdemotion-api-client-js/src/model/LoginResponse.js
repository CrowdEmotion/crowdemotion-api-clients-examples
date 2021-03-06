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
    root.CrowdemotionApiClientJs.LoginResponse = factory(root.CrowdemotionApiClientJs.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The LoginResponse model module.
   * @module model/LoginResponse
   * @version 1.1.0
   */

  /**
   * Constructs a new <code>LoginResponse</code>.
   * @alias module:model/LoginResponse
   * @class
   * @param userId {String} 
   * @param token {String} 
   * @param id {String} 
   * @param apiVersion {String} 
   */
  var exports = function(userId, token, id, apiVersion) {
    var _this = this;

    _this['userId'] = userId;
    _this['token'] = token;
    _this['id'] = id;
    _this['api_version'] = apiVersion;
  };

  /**
   * Constructs a <code>LoginResponse</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/LoginResponse} obj Optional instance to populate.
   * @return {module:model/LoginResponse} The populated <code>LoginResponse</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('userId')) {
        obj['userId'] = ApiClient.convertToType(data['userId'], 'String');
      }
      if (data.hasOwnProperty('token')) {
        obj['token'] = ApiClient.convertToType(data['token'], 'String');
      }
      if (data.hasOwnProperty('id')) {
        obj['id'] = ApiClient.convertToType(data['id'], 'String');
      }
      if (data.hasOwnProperty('api_version')) {
        obj['api_version'] = ApiClient.convertToType(data['api_version'], 'String');
      }
    }
    return obj;
  }

  /**
   * 
   * @member {String} userId
   */
  exports.prototype['userId'] = undefined;
  /**
   * 
   * @member {String} token
   */
  exports.prototype['token'] = undefined;
  /**
   * 
   * @member {String} id
   */
  exports.prototype['id'] = undefined;
  /**
   * 
   * @member {String} api_version
   */
  exports.prototype['api_version'] = undefined;



  return exports;
}));


