# Swagger\Client\ResponseApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**responseGet**](ResponseApi.md#responseGet) | **GET** /response | Find all Responses
[**responsePost**](ResponseApi.md#responsePost) | **POST** /response | Create a Response
[**responseResponseIdDelete**](ResponseApi.md#responseResponseIdDelete) | **DELETE** /response/{response_id} | Delete a Response
[**responseResponseIdGet**](ResponseApi.md#responseResponseIdGet) | **GET** /response/{response_id} | Find a Response
[**responseResponseIdMetadataGet**](ResponseApi.md#responseResponseIdMetadataGet) | **GET** /response/{response_id}/metadata | Show Response Metadata
[**responseResponseIdMetadataPost**](ResponseApi.md#responseResponseIdMetadataPost) | **POST** /response/{response_id}/metadata | Add Response Metadata
[**responseResponseIdPut**](ResponseApi.md#responseResponseIdPut) | **PUT** /response/{response_id} | Update a Response


# **responseGet**
> \Swagger\Client\Model\Response[] responseGet($skip, $limit, $where, $sort)

Find all Responses

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\ResponseApi();
$skip = 56; // int | The number of results to skip.
$limit = 56; // int | The maximum number of results to return.
$where = "where_example"; // string | JSON formatted string.
$sort = "sort_example"; // string | Attribute used to sort results.

try {
    $result = $api_instance->responseGet($skip, $limit, $where, $sort);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResponseApi->responseGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| The number of results to skip. | [optional]
 **limit** | **int**| The maximum number of results to return. | [optional]
 **where** | **string**| JSON formatted string. | [optional]
 **sort** | **string**| Attribute used to sort results. | [optional]

### Return type

[**\Swagger\Client\Model\Response[]**](../Model/Response.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **responsePost**
> \Swagger\Client\Model\Response responsePost($body)

Create a Response

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\ResponseApi();
$body = new \Swagger\Client\Model\ResponseCreation(); // \Swagger\Client\Model\ResponseCreation | Request body

try {
    $result = $api_instance->responsePost($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResponseApi->responsePost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\ResponseCreation**](../Model/\Swagger\Client\Model\ResponseCreation.md)| Request body |

### Return type

[**\Swagger\Client\Model\Response**](../Model/Response.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **responseResponseIdDelete**
> string responseResponseIdDelete($response_id)

Delete a Response

<p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\ResponseApi();
$response_id = 56; // int | ID of Response to update.

try {
    $result = $api_instance->responseResponseIdDelete($response_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResponseApi->responseResponseIdDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| ID of Response to update. |

### Return type

**string**

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **responseResponseIdGet**
> \Swagger\Client\Model\Response responseResponseIdGet($response_id)

Find a Response

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\ResponseApi();
$response_id = 56; // int | ID of the Response

try {
    $result = $api_instance->responseResponseIdGet($response_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResponseApi->responseResponseIdGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| ID of the Response |

### Return type

[**\Swagger\Client\Model\Response**](../Model/Response.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **responseResponseIdMetadataGet**
> \Swagger\Client\Model\ResponseMetadataResponse responseResponseIdMetadataGet($response_id)

Show Response Metadata

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\ResponseApi();
$response_id = 56; // int | ID of the Response

try {
    $result = $api_instance->responseResponseIdMetadataGet($response_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResponseApi->responseResponseIdMetadataGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| ID of the Response |

### Return type

[**\Swagger\Client\Model\ResponseMetadataResponse**](../Model/ResponseMetadataResponse.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **responseResponseIdMetadataPost**
> \Swagger\Client\Model\ResponseMetadataResponse responseResponseIdMetadataPost($response_id, $body)

Add Response Metadata

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\ResponseApi();
$response_id = 56; // int | ID of the Response.
$body = new \Swagger\Client\Model\ResponseMetadata(); // \Swagger\Client\Model\ResponseMetadata | Request body

try {
    $result = $api_instance->responseResponseIdMetadataPost($response_id, $body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResponseApi->responseResponseIdMetadataPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| ID of the Response. |
 **body** | [**\Swagger\Client\Model\ResponseMetadata**](../Model/\Swagger\Client\Model\ResponseMetadata.md)| Request body |

### Return type

[**\Swagger\Client\Model\ResponseMetadataResponse**](../Model/ResponseMetadataResponse.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **responseResponseIdPut**
> \Swagger\Client\Model\Response responseResponseIdPut($response_id, $body)

Update a Response

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\ResponseApi();
$response_id = 56; // int | ID of Response to update.
$body = new \Swagger\Client\Model\ResponseCreation(); // \Swagger\Client\Model\ResponseCreation | Request body

try {
    $result = $api_instance->responseResponseIdPut($response_id, $body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResponseApi->responseResponseIdPut: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| ID of Response to update. |
 **body** | [**\Swagger\Client\Model\ResponseCreation**](../Model/\Swagger\Client\Model\ResponseCreation.md)| Request body |

### Return type

[**\Swagger\Client\Model\Response**](../Model/Response.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

