# Swagger\Client\MediaApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mediaGet**](MediaApi.md#mediaGet) | **GET** /media | Find all registered Media
[**mediaMediaIdDelete**](MediaApi.md#mediaMediaIdDelete) | **DELETE** /media/{media_id} | Delete Media
[**mediaMediaIdGet**](MediaApi.md#mediaMediaIdGet) | **GET** /media/{media_id} | Find a Media
[**mediaMediaIdPut**](MediaApi.md#mediaMediaIdPut) | **PUT** /media/{media_id} | Update a Media
[**mediaPost**](MediaApi.md#mediaPost) | **POST** /media | Create new Media


# **mediaGet**
> \Swagger\Client\Model\Media mediaGet($skip, $limit, $where, $sort)

Find all registered Media

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\MediaApi();
$skip = 56; // int | The number of results to skip.
$limit = 56; // int | The maximum number of results to return.
$where = "where_example"; // string | JSON formatted string condition.
$sort = "sort_example"; // string | Attribute used to sort results.

try {
    $result = $api_instance->mediaGet($skip, $limit, $where, $sort);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MediaApi->mediaGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| The number of results to skip. | [optional]
 **limit** | **int**| The maximum number of results to return. | [optional]
 **where** | **string**| JSON formatted string condition. | [optional]
 **sort** | **string**| Attribute used to sort results. | [optional]

### Return type

[**\Swagger\Client\Model\Media**](../Model/Media.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **mediaMediaIdDelete**
> string mediaMediaIdDelete($media_id)

Delete Media

<p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\MediaApi();
$media_id = 56; // int | 

try {
    $result = $api_instance->mediaMediaIdDelete($media_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MediaApi->mediaMediaIdDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **int**|  |

### Return type

**string**

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **mediaMediaIdGet**
> \Swagger\Client\Model\Media[] mediaMediaIdGet($media_id, $presigned_url)

Find a Media

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\MediaApi();
$media_id = 56; // int | ID of Media to search.
$presigned_url = true; // bool | Returns the presignedUrl whose value is a signed (protected) URL to hosted video on our premises.

try {
    $result = $api_instance->mediaMediaIdGet($media_id, $presigned_url);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MediaApi->mediaMediaIdGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **int**| ID of Media to search. |
 **presigned_url** | **bool**| Returns the presignedUrl whose value is a signed (protected) URL to hosted video on our premises. | [optional]

### Return type

[**\Swagger\Client\Model\Media[]**](../Model/Media.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **mediaMediaIdPut**
> \Swagger\Client\Model\Media mediaMediaIdPut($media_id, $body)

Update a Media

<p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\MediaApi();
$media_id = 56; // int | 
$body = new \Swagger\Client\Model\MediaCreation(); // \Swagger\Client\Model\MediaCreation | Request body

try {
    $result = $api_instance->mediaMediaIdPut($media_id, $body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MediaApi->mediaMediaIdPut: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **int**|  |
 **body** | [**\Swagger\Client\Model\MediaCreation**](../Model/\Swagger\Client\Model\MediaCreation.md)| Request body |

### Return type

[**\Swagger\Client\Model\Media**](../Model/Media.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **mediaPost**
> \Swagger\Client\Model\Media mediaPost($body)

Create new Media

<p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\MediaApi();
$body = new \Swagger\Client\Model\MediaCreation(); // \Swagger\Client\Model\MediaCreation | Request body

try {
    $result = $api_instance->mediaPost($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MediaApi->mediaPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\MediaCreation**](../Model/\Swagger\Client\Model\MediaCreation.md)| Request body |

### Return type

[**\Swagger\Client\Model\Media**](../Model/Media.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

