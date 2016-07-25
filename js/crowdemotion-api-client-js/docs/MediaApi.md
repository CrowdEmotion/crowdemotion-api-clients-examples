# CrowdemotionApiClientJs.MediaApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mediaGet**](MediaApi.md#mediaGet) | **GET** /media | Find all registered Media
[**mediaMediaIdDelete**](MediaApi.md#mediaMediaIdDelete) | **DELETE** /media/{media_id} | Delete Media
[**mediaMediaIdGet**](MediaApi.md#mediaMediaIdGet) | **GET** /media/{media_id} | Find a Media
[**mediaMediaIdPut**](MediaApi.md#mediaMediaIdPut) | **PUT** /media/{media_id} | Update a Media
[**mediaPost**](MediaApi.md#mediaPost) | **POST** /media | Create new Media


<a name="mediaGet"></a>
# **mediaGet**
> Media mediaGet(opts)

Find all registered Media

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

var apiInstance = new CrowdemotionApiClientJs.MediaApi();

var opts = { 
  'skip': 56, // Integer | The number of results to skip.
  'limit': 56, // Integer | The maximum number of results to return.
  'where': "where_example", // String | JSON formatted string condition.
  'sort': "sort_example" // String | Attribute used to sort results.
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.mediaGet(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **Integer**| The number of results to skip. | [optional] 
 **limit** | **Integer**| The maximum number of results to return. | [optional] 
 **where** | **String**| JSON formatted string condition. | [optional] 
 **sort** | **String**| Attribute used to sort results. | [optional] 

### Return type

[**Media**](Media.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="mediaMediaIdDelete"></a>
# **mediaMediaIdDelete**
> &#39;String&#39; mediaMediaIdDelete(mediaId)

Delete Media

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

var apiInstance = new CrowdemotionApiClientJs.MediaApi();

var mediaId = 56; // Integer | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.mediaMediaIdDelete(mediaId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediaId** | **Integer**|  | 

### Return type

**&#39;String&#39;**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="mediaMediaIdGet"></a>
# **mediaMediaIdGet**
> [Media] mediaMediaIdGet(mediaId, opts)

Find a Media

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

var apiInstance = new CrowdemotionApiClientJs.MediaApi();

var mediaId = 56; // Integer | ID of Media to search.

var opts = { 
  'presignedUrl': true // Boolean | Returns the presignedUrl whose value is a signed (protected) URL to hosted video on our premises.
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.mediaMediaIdGet(mediaId, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediaId** | **Integer**| ID of Media to search. | 
 **presignedUrl** | **Boolean**| Returns the presignedUrl whose value is a signed (protected) URL to hosted video on our premises. | [optional] 

### Return type

[**[Media]**](Media.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="mediaMediaIdPut"></a>
# **mediaMediaIdPut**
> Media mediaMediaIdPut(mediaId, body)

Update a Media

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

var apiInstance = new CrowdemotionApiClientJs.MediaApi();

var mediaId = 56; // Integer | 

var body = new CrowdemotionApiClientJs.MediaCreation(); // MediaCreation | Request body


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.mediaMediaIdPut(mediaId, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediaId** | **Integer**|  | 
 **body** | [**MediaCreation**](MediaCreation.md)| Request body | 

### Return type

[**Media**](Media.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="mediaPost"></a>
# **mediaPost**
> Media mediaPost(body)

Create new Media

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

var apiInstance = new CrowdemotionApiClientJs.MediaApi();

var body = new CrowdemotionApiClientJs.MediaCreation(); // MediaCreation | Request body


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.mediaPost(body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MediaCreation**](MediaCreation.md)| Request body | 

### Return type

[**Media**](Media.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

