# Swagger\Client\UserApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userIdGet**](UserApi.md#userIdGet) | **GET** /user/{id} | Get User information
[**userIdPut**](UserApi.md#userIdPut) | **PUT** /user/{id} | Edit User information
[**userLoginPost**](UserApi.md#userLoginPost) | **POST** /user/login | User Login
[**userUserIdMetadataGet**](UserApi.md#userUserIdMetadataGet) | **GET** /user/{user_id}/metadata | Find User metadata
[**userUserIdMetadataPost**](UserApi.md#userUserIdMetadataPost) | **POST** /user/{user_id}/metadata | Add user metadata


# **userIdGet**
> \Swagger\Client\Model\User userIdGet($id)

Get User information

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\UserApi();
$id = 56; // int | User unique ID

try {
    $result = $api_instance->userIdGet($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UserApi->userIdGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User unique ID |

### Return type

[**\Swagger\Client\Model\User**](../Model/User.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **userIdPut**
> \Swagger\Client\Model\User userIdPut($id, $body)

Edit User information

<p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\UserApi();
$id = "id_example"; // string | ID of User to update.
$body = new \Swagger\Client\Model\UserUpdateBody(); // \Swagger\Client\Model\UserUpdateBody | Request body

try {
    $result = $api_instance->userIdPut($id, $body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UserApi->userIdPut: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string**| ID of User to update. |
 **body** | [**\Swagger\Client\Model\UserUpdateBody**](../Model/\Swagger\Client\Model\UserUpdateBody.md)| Request body |

### Return type

[**\Swagger\Client\Model\User**](../Model/User.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **userLoginPost**
> \Swagger\Client\Model\LoginResponse userLoginPost($body)

User Login

<p><strong>Permissions:</strong> No authorization is required</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\UserApi();
$body = new \Swagger\Client\Model\Login(); // \Swagger\Client\Model\Login | Request body

try {
    $result = $api_instance->userLoginPost($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UserApi->userLoginPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\Login**](../Model/\Swagger\Client\Model\Login.md)| Request body |

### Return type

[**\Swagger\Client\Model\LoginResponse**](../Model/LoginResponse.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **userUserIdMetadataGet**
> \Swagger\Client\Model\UserMetadataResponse userUserIdMetadataGet($user_id)

Find User metadata

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\UserApi();
$user_id = 56; // int | ID of User.

try {
    $result = $api_instance->userUserIdMetadataGet($user_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UserApi->userUserIdMetadataGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of User. |

### Return type

[**\Swagger\Client\Model\UserMetadataResponse**](../Model/UserMetadataResponse.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **userUserIdMetadataPost**
> \Swagger\Client\Model\UserMetadataResponse userUserIdMetadataPost($user_id, $body)

Add user metadata

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\UserApi();
$user_id = 56; // int | ID of User.
$body = new \Swagger\Client\Model\UserMetadata(); // \Swagger\Client\Model\UserMetadata | Request body

try {
    $result = $api_instance->userUserIdMetadataPost($user_id, $body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UserApi->userUserIdMetadataPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of User. |
 **body** | [**\Swagger\Client\Model\UserMetadata**](../Model/\Swagger\Client\Model\UserMetadata.md)| Request body |

### Return type

[**\Swagger\Client\Model\UserMetadataResponse**](../Model/UserMetadataResponse.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

