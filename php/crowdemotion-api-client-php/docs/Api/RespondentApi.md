# Swagger\Client\RespondentApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**respondentGet**](RespondentApi.md#respondentGet) | **GET** /respondent | Find all Respondents of a Research
[**respondentPost**](RespondentApi.md#respondentPost) | **POST** /respondent | Create a Respondent
[**respondentRespondentIdDelete**](RespondentApi.md#respondentRespondentIdDelete) | **DELETE** /respondent/{respondent_id} | Delete a Respondent
[**respondentRespondentIdGet**](RespondentApi.md#respondentRespondentIdGet) | **GET** /respondent/{respondent_id} | Find a Respondent
[**respondentRespondentIdMetadataGet**](RespondentApi.md#respondentRespondentIdMetadataGet) | **GET** /respondent/{respondent_id}/metadata | Find Respondent Metadata
[**respondentRespondentIdMetadataPost**](RespondentApi.md#respondentRespondentIdMetadataPost) | **POST** /respondent/{respondent_id}/metadata | Add Respondent Metadata
[**respondentRespondentIdPut**](RespondentApi.md#respondentRespondentIdPut) | **PUT** /respondent/{respondent_id} | Update a Respondent


# **respondentGet**
> \Swagger\Client\Model\Respondent[] respondentGet($research_id, $skip, $limit, $where, $sort)

Find all Respondents of a Research

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\RespondentApi();
$research_id = 56; // int | Search by research id.
$skip = 56; // int | The number of results to skip.
$limit = 56; // int | The maximum number of results to return.
$where = "where_example"; // string | JSON formatted string.
$sort = "sort_example"; // string | Attribute used to sort results.

try {
    $result = $api_instance->respondentGet($research_id, $skip, $limit, $where, $sort);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RespondentApi->respondentGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **research_id** | **int**| Search by research id. |
 **skip** | **int**| The number of results to skip. | [optional]
 **limit** | **int**| The maximum number of results to return. | [optional]
 **where** | **string**| JSON formatted string. | [optional]
 **sort** | **string**| Attribute used to sort results. | [optional]

### Return type

[**\Swagger\Client\Model\Respondent[]**](../Model/Respondent.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **respondentPost**
> \Swagger\Client\Model\Respondent respondentPost($body)

Create a Respondent

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\RespondentApi();
$body = new \Swagger\Client\Model\Respondent(); // \Swagger\Client\Model\Respondent | Request body

try {
    $result = $api_instance->respondentPost($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RespondentApi->respondentPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\Respondent**](../Model/\Swagger\Client\Model\Respondent.md)| Request body |

### Return type

[**\Swagger\Client\Model\Respondent**](../Model/Respondent.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **respondentRespondentIdDelete**
> string respondentRespondentIdDelete($respondent_id)

Delete a Respondent

<p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\RespondentApi();
$respondent_id = 56; // int | 

try {
    $result = $api_instance->respondentRespondentIdDelete($respondent_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RespondentApi->respondentRespondentIdDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **respondent_id** | **int**|  |

### Return type

**string**

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **respondentRespondentIdGet**
> \Swagger\Client\Model\Respondent respondentRespondentIdGet($respondent_id)

Find a Respondent

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\RespondentApi();
$respondent_id = 56; // int | Search by research id.

try {
    $result = $api_instance->respondentRespondentIdGet($respondent_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RespondentApi->respondentRespondentIdGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **respondent_id** | **int**| Search by research id. |

### Return type

[**\Swagger\Client\Model\Respondent**](../Model/Respondent.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **respondentRespondentIdMetadataGet**
> \Swagger\Client\Model\RespondentMetadataResponse respondentRespondentIdMetadataGet($respondent_id)

Find Respondent Metadata

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\RespondentApi();
$respondent_id = 56; // int | ID of the Respondent

try {
    $result = $api_instance->respondentRespondentIdMetadataGet($respondent_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RespondentApi->respondentRespondentIdMetadataGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **respondent_id** | **int**| ID of the Respondent |

### Return type

[**\Swagger\Client\Model\RespondentMetadataResponse**](../Model/RespondentMetadataResponse.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **respondentRespondentIdMetadataPost**
> \Swagger\Client\Model\RespondentMetadataResponse respondentRespondentIdMetadataPost($respondent_id, $body)

Add Respondent Metadata

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\RespondentApi();
$respondent_id = 56; // int | 
$body = new \Swagger\Client\Model\RespondentMetadata(); // \Swagger\Client\Model\RespondentMetadata | Request body

try {
    $result = $api_instance->respondentRespondentIdMetadataPost($respondent_id, $body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RespondentApi->respondentRespondentIdMetadataPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **respondent_id** | **int**|  |
 **body** | [**\Swagger\Client\Model\RespondentMetadata**](../Model/\Swagger\Client\Model\RespondentMetadata.md)| Request body |

### Return type

[**\Swagger\Client\Model\RespondentMetadataResponse**](../Model/RespondentMetadataResponse.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **respondentRespondentIdPut**
> \Swagger\Client\Model\Respondent respondentRespondentIdPut($respondent_id, $body)

Update a Respondent

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\RespondentApi();
$respondent_id = 56; // int | 
$body = new \Swagger\Client\Model\Respondent(); // \Swagger\Client\Model\Respondent | Request body

try {
    $result = $api_instance->respondentRespondentIdPut($respondent_id, $body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RespondentApi->respondentRespondentIdPut: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **respondent_id** | **int**|  |
 **body** | [**\Swagger\Client\Model\Respondent**](../Model/\Swagger\Client\Model\Respondent.md)| Request body |

### Return type

[**\Swagger\Client\Model\Respondent**](../Model/Respondent.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

