# Swagger\Client\ResearchApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**researchGet**](ResearchApi.md#researchGet) | **GET** /research | Find all Research
[**researchPost**](ResearchApi.md#researchPost) | **POST** /research | Create a Research Project
[**researchResearchIdDelete**](ResearchApi.md#researchResearchIdDelete) | **DELETE** /research/{research_id} | Delete Research Project
[**researchResearchIdGet**](ResearchApi.md#researchResearchIdGet) | **GET** /research/{research_id} | Find a Research Project
[**researchResearchIdPut**](ResearchApi.md#researchResearchIdPut) | **PUT** /research/{research_id} | Edit Research Project details


# **researchGet**
> \Swagger\Client\Model\Research[] researchGet($skip, $limit, $where, $sort)

Find all Research

<p>Returns all the Research created by an admin user.</p> <p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\ResearchApi();
$skip = 56; // int | The number of results to skip.
$limit = 56; // int | The maximum number of results to return.
$where = "where_example"; // string | JSON formatted string condition.
$sort = "sort_example"; // string | Attribute used to sort results.

try {
    $result = $api_instance->researchGet($skip, $limit, $where, $sort);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResearchApi->researchGet: ', $e->getMessage(), PHP_EOL;
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

[**\Swagger\Client\Model\Research[]**](../Model/Research.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **researchPost**
> \Swagger\Client\Model\Research researchPost($body)

Create a Research Project

<p>New research projects can only be created with an admin account.</p> <p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\ResearchApi();
$body = new \Swagger\Client\Model\ResearchCreation(); // \Swagger\Client\Model\ResearchCreation | Request body

try {
    $result = $api_instance->researchPost($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResearchApi->researchPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\ResearchCreation**](../Model/\Swagger\Client\Model\ResearchCreation.md)| Request body |

### Return type

[**\Swagger\Client\Model\Research**](../Model/Research.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **researchResearchIdDelete**
> string researchResearchIdDelete($research_id)

Delete Research Project

<p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\ResearchApi();
$research_id = 56; // int | 

try {
    $result = $api_instance->researchResearchIdDelete($research_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResearchApi->researchResearchIdDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **research_id** | **int**|  |

### Return type

**string**

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **researchResearchIdGet**
> \Swagger\Client\Model\Research researchResearchIdGet($research_id)

Find a Research Project

<p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\ResearchApi();
$research_id = 56; // int | ID of Research Project to be found.

try {
    $result = $api_instance->researchResearchIdGet($research_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResearchApi->researchResearchIdGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **research_id** | **int**| ID of Research Project to be found. |

### Return type

[**\Swagger\Client\Model\Research**](../Model/Research.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **researchResearchIdPut**
> \Swagger\Client\Model\Research researchResearchIdPut($research_id, $body)

Edit Research Project details

<p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\ResearchApi();
$research_id = 56; // int | 
$body = new \Swagger\Client\Model\ResearchCreation(); // \Swagger\Client\Model\ResearchCreation | Request body

try {
    $result = $api_instance->researchResearchIdPut($research_id, $body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResearchApi->researchResearchIdPut: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **research_id** | **int**|  |
 **body** | [**\Swagger\Client\Model\ResearchCreation**](../Model/\Swagger\Client\Model\ResearchCreation.md)| Request body |

### Return type

[**\Swagger\Client\Model\Research**](../Model/Research.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

