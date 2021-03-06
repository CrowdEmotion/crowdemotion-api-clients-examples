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
    define(['ApiClient', 'model/Media', 'model/MediaCreation'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('../model/Media'), require('../model/MediaCreation'));
  } else {
    // Browser globals (root is window)
    if (!root.CrowdemotionApiClientJs) {
      root.CrowdemotionApiClientJs = {};
    }
    root.CrowdemotionApiClientJs.MediaApi = factory(root.CrowdemotionApiClientJs.ApiClient, root.CrowdemotionApiClientJs.Media, root.CrowdemotionApiClientJs.MediaCreation);
  }
}(this, function(ApiClient, Media, MediaCreation) {
  'use strict';

  /**
   * Media service.
   * @module api/MediaApi
   * @version 1.1.0
   */

  /**
   * Constructs a new MediaApi. 
   * @alias module:api/MediaApi
   * @class
   * @param {module:ApiClient} apiClient Optional API client implementation to use,
   * default to {@link module:ApiClient#instance} if unspecified.
   */
  var exports = function(apiClient) {
    this.apiClient = apiClient || ApiClient.instance;


    /**
     * Callback function to receive the result of the mediaGet operation.
     * @callback module:api/MediaApi~mediaGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Media} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Find all registered Media
     * &lt;p&gt;&lt;strong&gt;Permissions:&lt;/strong&gt; ✓ Respondent ✗ Customer ✓ Manager&lt;/p&gt;
     * @param {Object} opts Optional parameters
     * @param {Integer} opts.skip The number of results to skip.
     * @param {Integer} opts.limit The maximum number of results to return.
     * @param {String} opts.where JSON formatted string condition.
     * @param {String} opts.sort Attribute used to sort results.
     * @param {module:api/MediaApi~mediaGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {module:model/Media}
     */
    this.mediaGet = function(opts, callback) {
      opts = opts || {};
      var postBody = null;


      var pathParams = {
      };
      var queryParams = {
        'skip': opts['skip'],
        'limit': opts['limit'],
        'where': opts['where'],
        'sort': opts['sort']
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['api_key'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = Media;

      return this.apiClient.callApi(
        '/media', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the mediaMediaIdDelete operation.
     * @callback module:api/MediaApi~mediaMediaIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {'String'} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete Media
     * &lt;p&gt;&lt;strong&gt;Permissions:&lt;/strong&gt; ✗ Respondent ✗ Customer ✓ Manager&lt;/p&gt;
     * @param {Integer} mediaId 
     * @param {module:api/MediaApi~mediaMediaIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {'String'}
     */
    this.mediaMediaIdDelete = function(mediaId, callback) {
      var postBody = null;

      // verify the required parameter 'mediaId' is set
      if (mediaId == undefined || mediaId == null) {
        throw "Missing the required parameter 'mediaId' when calling mediaMediaIdDelete";
      }


      var pathParams = {
        'media_id': mediaId
      };
      var queryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['api_key'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = 'String';

      return this.apiClient.callApi(
        '/media/{media_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the mediaMediaIdGet operation.
     * @callback module:api/MediaApi~mediaMediaIdGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Media>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Find a Media
     * &lt;p&gt;&lt;strong&gt;Permissions:&lt;/strong&gt; ✓ Respondent ✗ Customer ✓ Manager&lt;/p&gt;
     * @param {Integer} mediaId ID of Media to search.
     * @param {Object} opts Optional parameters
     * @param {Boolean} opts.presignedUrl Returns the presignedUrl whose value is a signed (protected) URL to hosted video on our premises.
     * @param {module:api/MediaApi~mediaMediaIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {Array.<module:model/Media>}
     */
    this.mediaMediaIdGet = function(mediaId, opts, callback) {
      opts = opts || {};
      var postBody = null;

      // verify the required parameter 'mediaId' is set
      if (mediaId == undefined || mediaId == null) {
        throw "Missing the required parameter 'mediaId' when calling mediaMediaIdGet";
      }


      var pathParams = {
        'media_id': mediaId
      };
      var queryParams = {
        'presignedUrl': opts['presignedUrl']
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['api_key'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = [Media];

      return this.apiClient.callApi(
        '/media/{media_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the mediaMediaIdPut operation.
     * @callback module:api/MediaApi~mediaMediaIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Media} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a Media
     * &lt;p&gt;&lt;strong&gt;Permissions:&lt;/strong&gt; ✗ Respondent ✗ Customer ✓ Manager&lt;/p&gt;
     * @param {Integer} mediaId 
     * @param {module:model/MediaCreation} body Request body
     * @param {module:api/MediaApi~mediaMediaIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {module:model/Media}
     */
    this.mediaMediaIdPut = function(mediaId, body, callback) {
      var postBody = body;

      // verify the required parameter 'mediaId' is set
      if (mediaId == undefined || mediaId == null) {
        throw "Missing the required parameter 'mediaId' when calling mediaMediaIdPut";
      }

      // verify the required parameter 'body' is set
      if (body == undefined || body == null) {
        throw "Missing the required parameter 'body' when calling mediaMediaIdPut";
      }


      var pathParams = {
        'media_id': mediaId
      };
      var queryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['api_key'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = Media;

      return this.apiClient.callApi(
        '/media/{media_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the mediaPost operation.
     * @callback module:api/MediaApi~mediaPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Media} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create new Media
     * &lt;p&gt;&lt;strong&gt;Permissions:&lt;/strong&gt; ✗ Respondent ✗ Customer ✓ Manager&lt;/p&gt;
     * @param {module:model/MediaCreation} body Request body
     * @param {module:api/MediaApi~mediaPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {module:model/Media}
     */
    this.mediaPost = function(body, callback) {
      var postBody = body;

      // verify the required parameter 'body' is set
      if (body == undefined || body == null) {
        throw "Missing the required parameter 'body' when calling mediaPost";
      }


      var pathParams = {
      };
      var queryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['api_key'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = Media;

      return this.apiClient.callApi(
        '/media', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }
  };

  return exports;
}));
