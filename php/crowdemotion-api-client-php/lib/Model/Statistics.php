<?php
/**
 * Statistics
 *
 * PHP version 5
 *
 * @category Class
 * @package  Swagger\Client
 * @author   http://github.com/swagger-api/swagger-codegen
 * @license  http://www.apache.org/licenses/LICENSE-2.0 Apache Licene v2
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * CloudEmotion API v1
 *
 * CrowdEmotion API
 *
 * OpenAPI spec version: 1.1.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

namespace Swagger\Client\Model;

use \ArrayAccess;

/**
 * Statistics Class Doc Comment
 *
 * @category    Class */
/** 
 * @package     Swagger\Client
 * @author      http://github.com/swagger-api/swagger-codegen
 * @license     http://www.apache.org/licenses/LICENSE-2.0 Apache Licene v2
 * @link        https://github.com/swagger-api/swagger-codegen
 */
class Statistics implements ArrayAccess
{
    /**
      * The original name of the model.
      * @var string
      */
    protected static $swaggerModelName = 'statistics';

    /**
      * Array of property to type mappings. Used for (de)serialization
      * @var string[]
      */
    protected static $swaggerTypes = array(
        'view_count' => 'int',
        'like_count' => 'int',
        'dislike_count' => 'int',
        'favorite_count' => 'int',
        'comment_count' => 'int'
    );

    public static function swaggerTypes()
    {
        return self::$swaggerTypes;
    }

    /**
     * Array of attributes where the key is the local name, and the value is the original name
     * @var string[]
     */
    protected static $attributeMap = array(
        'view_count' => 'viewCount',
        'like_count' => 'likeCount',
        'dislike_count' => 'dislikeCount',
        'favorite_count' => 'favoriteCount',
        'comment_count' => 'commentCount'
    );

    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     * @var string[]
     */
    protected static $setters = array(
        'view_count' => 'setViewCount',
        'like_count' => 'setLikeCount',
        'dislike_count' => 'setDislikeCount',
        'favorite_count' => 'setFavoriteCount',
        'comment_count' => 'setCommentCount'
    );

    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     * @var string[]
     */
    protected static $getters = array(
        'view_count' => 'getViewCount',
        'like_count' => 'getLikeCount',
        'dislike_count' => 'getDislikeCount',
        'favorite_count' => 'getFavoriteCount',
        'comment_count' => 'getCommentCount'
    );

    public static function getters()
    {
        return self::$getters;
    }

    

    

    /**
     * Associative array for storing property values
     * @var mixed[]
     */
    protected $container = array();

    /**
     * Constructor
     * @param mixed[] $data Associated array of property value initalizing the model
     */
    public function __construct(array $data = null)
    {
        $this->container['view_count'] = isset($data['view_count']) ? $data['view_count'] : null;
        $this->container['like_count'] = isset($data['like_count']) ? $data['like_count'] : null;
        $this->container['dislike_count'] = isset($data['dislike_count']) ? $data['dislike_count'] : null;
        $this->container['favorite_count'] = isset($data['favorite_count']) ? $data['favorite_count'] : null;
        $this->container['comment_count'] = isset($data['comment_count']) ? $data['comment_count'] : null;
    }

    /**
     * show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalid_properties = array();
        if ($this->container['view_count'] === null) {
            $invalid_properties[] = "'view_count' can't be null";
        }
        if ($this->container['like_count'] === null) {
            $invalid_properties[] = "'like_count' can't be null";
        }
        if ($this->container['dislike_count'] === null) {
            $invalid_properties[] = "'dislike_count' can't be null";
        }
        if ($this->container['favorite_count'] === null) {
            $invalid_properties[] = "'favorite_count' can't be null";
        }
        if ($this->container['comment_count'] === null) {
            $invalid_properties[] = "'comment_count' can't be null";
        }
        return $invalid_properties;
    }

    /**
     * validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properteis are valid
     */
    public function valid()
    {
        if ($this->container['view_count'] === null) {
            return false;
        }
        if ($this->container['like_count'] === null) {
            return false;
        }
        if ($this->container['dislike_count'] === null) {
            return false;
        }
        if ($this->container['favorite_count'] === null) {
            return false;
        }
        if ($this->container['comment_count'] === null) {
            return false;
        }
        return true;
    }


    /**
     * Gets view_count
     * @return int
     */
    public function getViewCount()
    {
        return $this->container['view_count'];
    }

    /**
     * Sets view_count
     * @param int $view_count 
     * @return $this
     */
    public function setViewCount($view_count)
    {
        $this->container['view_count'] = $view_count;

        return $this;
    }

    /**
     * Gets like_count
     * @return int
     */
    public function getLikeCount()
    {
        return $this->container['like_count'];
    }

    /**
     * Sets like_count
     * @param int $like_count 
     * @return $this
     */
    public function setLikeCount($like_count)
    {
        $this->container['like_count'] = $like_count;

        return $this;
    }

    /**
     * Gets dislike_count
     * @return int
     */
    public function getDislikeCount()
    {
        return $this->container['dislike_count'];
    }

    /**
     * Sets dislike_count
     * @param int $dislike_count 
     * @return $this
     */
    public function setDislikeCount($dislike_count)
    {
        $this->container['dislike_count'] = $dislike_count;

        return $this;
    }

    /**
     * Gets favorite_count
     * @return int
     */
    public function getFavoriteCount()
    {
        return $this->container['favorite_count'];
    }

    /**
     * Sets favorite_count
     * @param int $favorite_count 
     * @return $this
     */
    public function setFavoriteCount($favorite_count)
    {
        $this->container['favorite_count'] = $favorite_count;

        return $this;
    }

    /**
     * Gets comment_count
     * @return int
     */
    public function getCommentCount()
    {
        return $this->container['comment_count'];
    }

    /**
     * Sets comment_count
     * @param int $comment_count 
     * @return $this
     */
    public function setCommentCount($comment_count)
    {
        $this->container['comment_count'] = $comment_count;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     * @param  integer $offset Offset
     * @return boolean
     */
    public function offsetExists($offset)
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     * @param  integer $offset Offset
     * @return mixed
     */
    public function offsetGet($offset)
    {
        return isset($this->container[$offset]) ? $this->container[$offset] : null;
    }

    /**
     * Sets value based on offset.
     * @param  integer $offset Offset
     * @param  mixed   $value  Value to be set
     * @return void
     */
    public function offsetSet($offset, $value)
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     * @param  integer $offset Offset
     * @return void
     */
    public function offsetUnset($offset)
    {
        unset($this->container[$offset]);
    }

    /**
     * Gets the string presentation of the object
     * @return string
     */
    public function __toString()
    {
        if (defined('JSON_PRETTY_PRINT')) { // use JSON pretty print
            return json_encode(\Swagger\Client\ObjectSerializer::sanitizeForSerialization($this), JSON_PRETTY_PRINT);
        }

        return json_encode(\Swagger\Client\ObjectSerializer::sanitizeForSerialization($this));
    }
}


