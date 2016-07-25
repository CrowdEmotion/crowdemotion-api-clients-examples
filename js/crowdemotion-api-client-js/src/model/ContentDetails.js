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
    root.CrowdemotionApiClientJs.ContentDetails = factory(root.CrowdemotionApiClientJs.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The ContentDetails model module.
   * @module model/ContentDetails
   * @version 1.1.0
   */

  /**
   * Constructs a new <code>ContentDetails</code>.
   * @alias module:model/ContentDetails
   * @class
   * @param duration {String} 
   * @param dimension {String} 
   * @param definition {String} 
   * @param caption {Boolean} 
   * @param licensedContent {Boolean} 
   */
  var exports = function(duration, dimension, definition, caption, licensedContent) {
    var _this = this;

    _this['duration'] = duration;
    _this['dimension'] = dimension;
    _this['definition'] = definition;
    _this['caption'] = caption;
    _this['licensedContent'] = licensedContent;
  };

  /**
   * Constructs a <code>ContentDetails</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/ContentDetails} obj Optional instance to populate.
   * @return {module:model/ContentDetails} The populated <code>ContentDetails</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('duration')) {
        obj['duration'] = ApiClient.convertToType(data['duration'], 'String');
      }
      if (data.hasOwnProperty('dimension')) {
        obj['dimension'] = ApiClient.convertToType(data['dimension'], 'String');
      }
      if (data.hasOwnProperty('definition')) {
        obj['definition'] = ApiClient.convertToType(data['definition'], 'String');
      }
      if (data.hasOwnProperty('caption')) {
        obj['caption'] = ApiClient.convertToType(data['caption'], 'Boolean');
      }
      if (data.hasOwnProperty('licensedContent')) {
        obj['licensedContent'] = ApiClient.convertToType(data['licensedContent'], 'Boolean');
      }
    }
    return obj;
  }

  /**
   * 
   * @member {String} duration
   */
  exports.prototype['duration'] = undefined;
  /**
   * 
   * @member {String} dimension
   */
  exports.prototype['dimension'] = undefined;
  /**
   * 
   * @member {String} definition
   */
  exports.prototype['definition'] = undefined;
  /**
   * 
   * @member {Boolean} caption
   */
  exports.prototype['caption'] = undefined;
  /**
   * 
   * @member {Boolean} licensedContent
   */
  exports.prototype['licensedContent'] = undefined;



  return exports;
}));

