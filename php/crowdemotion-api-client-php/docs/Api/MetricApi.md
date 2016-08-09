# Swagger\Client\MetricApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metricGet**](MetricApi.md#metricGet) | **GET** /metric | List all registered metrics
[**metricMetricIdDelete**](MetricApi.md#metricMetricIdDelete) | **DELETE** /metric/{metric_id} | Delete a Metric
[**metricMetricIdGet**](MetricApi.md#metricMetricIdGet) | **GET** /metric/{metric_id} | Find a Metric
[**metricPost**](MetricApi.md#metricPost) | **POST** /metric | Create Metric


# **metricGet**
> \Swagger\Client\Model\Metric[] metricGet($skip, $limit, $where, $sort)

List all registered metrics

<p>Metrics are linked to time-series and define their meaning.</p> <p>Common metric ID are listed below:</p> <table>   <tr><td>id</td><td>Value</td></tr>   <tr><td>1</td><td>Timestamp</td></tr>   <tr><td>2</td><td>Neutral</td></tr>   <tr><td>3</td><td>Happiness</td></tr>   <tr><td>4</td><td>Surprise</td></tr>   <tr><td>5</td><td>Puzzlement</td></tr>   <tr><td>6</td><td>Disgust</td></tr>   <tr><td>7</td><td>Fear</td></tr>   <tr><td>8</td><td>Sadness</td></tr> </table> <p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\MetricApi();
$skip = 56; // int | The number of results to skip.
$limit = 56; // int | The maximum number of results to return.
$where = "where_example"; // string | JSON formatted string condition.
$sort = "sort_example"; // string | Attribute used to sort results.

try {
    $result = $api_instance->metricGet($skip, $limit, $where, $sort);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MetricApi->metricGet: ', $e->getMessage(), PHP_EOL;
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

[**\Swagger\Client\Model\Metric[]**](../Model/Metric.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **metricMetricIdDelete**
> \Swagger\Client\Model\Metric metricMetricIdDelete($metric_id)

Delete a Metric

<p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\MetricApi();
$metric_id = 56; // int | ID of Metric to be deleted.

try {
    $result = $api_instance->metricMetricIdDelete($metric_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MetricApi->metricMetricIdDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **int**| ID of Metric to be deleted. |

### Return type

[**\Swagger\Client\Model\Metric**](../Model/Metric.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **metricMetricIdGet**
> \Swagger\Client\Model\Metric metricMetricIdGet($metric_id)

Find a Metric

<p>Metrics are linked to time-series and define their meaning.</p> <p>Common metric ID are listed below:</p> <table>   <tr><td>id</td><td>Value</td></tr>   <tr><td>1</td><td>Timestamp</td></tr>   <tr><td>2</td><td>Neutral</td></tr>   <tr><td>3</td><td>Happiness</td></tr>   <tr><td>4</td><td>Surprise</td></tr>   <tr><td>5</td><td>Puzzlement</td></tr>   <tr><td>6</td><td>Disgust</td></tr>   <tr><td>7</td><td>Fear</td></tr>   <tr><td>8</td><td>Sadness</td></tr> </table> <p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\MetricApi();
$metric_id = 56; // int | ID of Metric to find.

try {
    $result = $api_instance->metricMetricIdGet($metric_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MetricApi->metricMetricIdGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **int**| ID of Metric to find. |

### Return type

[**\Swagger\Client\Model\Metric**](../Model/Metric.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **metricPost**
> \Swagger\Client\Model\Metric metricPost($body)

Create Metric

<p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\MetricApi();
$body = new \Swagger\Client\Model\MetricCreation(); // \Swagger\Client\Model\MetricCreation | Request body

try {
    $result = $api_instance->metricPost($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MetricApi->metricPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\MetricCreation**](../Model/\Swagger\Client\Model\MetricCreation.md)| Request body |

### Return type

[**\Swagger\Client\Model\Metric**](../Model/Metric.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

