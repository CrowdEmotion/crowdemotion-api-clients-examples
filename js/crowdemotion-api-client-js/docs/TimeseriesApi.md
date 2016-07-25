# CrowdemotionApiClientJs.TimeseriesApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeseriesDelete**](TimeseriesApi.md#timeseriesDelete) | **DELETE** /timeseries | Delete a Timeseries
[**timeseriesGet**](TimeseriesApi.md#timeseriesGet) | **GET** /timeseries | Get all recorded timeseries for a Response


<a name="timeseriesDelete"></a>
# **timeseriesDelete**
> &#39;String&#39; timeseriesDelete(responseId, opts)

Delete a Timeseries

&lt;p&gt;&lt;strong&gt;Permissions:&lt;/strong&gt; ✗ Respondent ✗ Customer ✓ Manager&lt;/p&gt;

### Example
```javascript
var CrowdemotionApiClientJs = require('crowdemotion-api-client-js');
var defaultClient = CrowdemotionApiClientJs.ApiClient.default;

// Configure API key authorization: api_key
var api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

var apiInstance = new CrowdemotionApiClientJs.TimeseriesApi();

var responseId = 56; // Integer | ID of the Response associated to the TimeSeries.

var opts = { 
  'metricId': 56 // Integer | ID of the Metric of the Timeseries to be deleted.
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.timeseriesDelete(responseId, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **responseId** | **Integer**| ID of the Response associated to the TimeSeries. | 
 **metricId** | **Integer**| ID of the Metric of the Timeseries to be deleted. | [optional] 

### Return type

**&#39;String&#39;**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="timeseriesGet"></a>
# **timeseriesGet**
> [Timeseries] timeseriesGet(responseId, opts)

Get all recorded timeseries for a Response

&lt;p&gt;&lt;strong&gt;Permissions:&lt;/strong&gt; ✓ Respondent ✗ Customer ✓ Manager&lt;/p&gt;

### Example
```javascript
var CrowdemotionApiClientJs = require('crowdemotion-api-client-js');
var defaultClient = CrowdemotionApiClientJs.ApiClient.default;

// Configure API key authorization: api_key
var api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

var apiInstance = new CrowdemotionApiClientJs.TimeseriesApi();

var responseId = 56; // Integer | ID of the Response associated to the TimeSeries.

var opts = { 
  'metricId': 56, // Integer | ID of the Metric associated to the TimeSeries.
  'normalize': true, // Boolean | Return data beetwen 0 and 1. Default: false.
  'format': "format_example" // String | If value is 'csv' then data is passed back in CSV format insted of the default time-series format. Example: csv.
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.timeseriesGet(responseId, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **responseId** | **Integer**| ID of the Response associated to the TimeSeries. | 
 **metricId** | **Integer**| ID of the Metric associated to the TimeSeries. | [optional] 
 **normalize** | **Boolean**| Return data beetwen 0 and 1. Default: false. | [optional] 
 **format** | **String**| If value is &#39;csv&#39; then data is passed back in CSV format insted of the default time-series format. Example: csv. | [optional] 

### Return type

[**[Timeseries]**](Timeseries.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

