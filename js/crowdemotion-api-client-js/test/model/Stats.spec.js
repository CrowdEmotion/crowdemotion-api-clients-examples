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
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.CrowdemotionApiClientJs);
  }
}(this, function(expect, CrowdemotionApiClientJs) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CrowdemotionApiClientJs.Stats();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('Stats', function() {
    it('should create an instance of Stats', function() {
      // uncomment below and update the code to test Stats
      //var instane = new CrowdemotionApiClientJs.Stats();
      //expect(instance).to.be.a(CrowdemotionApiClientJs.Stats);
    });

    it('should have the property media (base name: "media")', function() {
      // uncomment below and update the code to test the property media
      //var instane = new CrowdemotionApiClientJs.Stats();
      //expect(instance).to.be();
    });

    it('should have the property visited (base name: "visited")', function() {
      // uncomment below and update the code to test the property visited
      //var instane = new CrowdemotionApiClientJs.Stats();
      //expect(instance).to.be();
    });

    it('should have the property started (base name: "started")', function() {
      // uncomment below and update the code to test the property started
      //var instane = new CrowdemotionApiClientJs.Stats();
      //expect(instance).to.be();
    });

    it('should have the property partial (base name: "partial")', function() {
      // uncomment below and update the code to test the property partial
      //var instane = new CrowdemotionApiClientJs.Stats();
      //expect(instance).to.be();
    });

    it('should have the property completes (base name: "completes")', function() {
      // uncomment below and update the code to test the property completes
      //var instane = new CrowdemotionApiClientJs.Stats();
      //expect(instance).to.be();
    });

    it('should have the property processed (base name: "processed")', function() {
      // uncomment below and update the code to test the property processed
      //var instane = new CrowdemotionApiClientJs.Stats();
      //expect(instance).to.be();
    });

    it('should have the property failed (base name: "failed")', function() {
      // uncomment below and update the code to test the property failed
      //var instane = new CrowdemotionApiClientJs.Stats();
      //expect(instance).to.be();
    });

    it('should have the property unprocessed (base name: "unprocessed")', function() {
      // uncomment below and update the code to test the property unprocessed
      //var instane = new CrowdemotionApiClientJs.Stats();
      //expect(instance).to.be();
    });

    it('should have the property lastUpdated (base name: "lastUpdated")', function() {
      // uncomment below and update the code to test the property lastUpdated
      //var instane = new CrowdemotionApiClientJs.Stats();
      //expect(instance).to.be();
    });

  });

}));
