# Swagger\Client\TimeseriesApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeseriesDelete**](TimeseriesApi.md#timeseriesDelete) | **DELETE** /timeseries | Delete a Timeseries
[**timeseriesGet**](TimeseriesApi.md#timeseriesGet) | **GET** /timeseries | Get all recorded timeseries for a Response


# **timeseriesDelete**
> string timeseriesDelete($response_id, $metric_id)

Delete a Timeseries

<p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\TimeseriesApi();
$response_id = 56; // int | ID of the Response associated to the TimeSeries.
$metric_id = 56; // int | ID of the Metric of the Timeseries to be deleted.

try {
    $result = $api_instance->timeseriesDelete($response_id, $metric_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TimeseriesApi->timeseriesDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| ID of the Response associated to the TimeSeries. |
 **metric_id** | **int**| ID of the Metric of the Timeseries to be deleted. | [optional]

### Return type

**string**

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **timeseriesGet**
> \Swagger\Client\Model\Timeseries[] timeseriesGet($response_id, $metric_id, $normalize, $format)

Get all recorded timeseries for a Response

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\TimeseriesApi();
$response_id = 56; // int | ID of the Response associated to the TimeSeries.
$metric_id = 56; // int | ID of the Metric associated to the TimeSeries.
$normalize = true; // bool | Return data beetwen 0 and 1. Default: false.
$format = "format_example"; // string | If value is 'csv' then data is passed back in CSV format insted of the default time-series format. Example: csv.

try {
    $result = $api_instance->timeseriesGet($response_id, $metric_id, $normalize, $format);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TimeseriesApi->timeseriesGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| ID of the Response associated to the TimeSeries. |
 **metric_id** | **int**| ID of the Metric associated to the TimeSeries. | [optional]
 **normalize** | **bool**| Return data beetwen 0 and 1. Default: false. | [optional]
 **format** | **string**| If value is &#39;csv&#39; then data is passed back in CSV format insted of the default time-series format. Example: csv. | [optional]

### Return type

[**\Swagger\Client\Model\Timeseries[]**](../Model/Timeseries.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

