# CrowdemotionApiClientJs.ResponseApi

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


<a name="responseGet"></a>
# **responseGet**
> [Response] responseGet(opts)

Find all Responses

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

var apiInstance = new CrowdemotionApiClientJs.ResponseApi();

var opts = { 
  'skip': 56, // Integer | The number of results to skip.
  'limit': 56, // Integer | The maximum number of results to return.
  'where': "where_example", // String | JSON formatted string.
  'sort': "sort_example" // String | Attribute used to sort results.
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.responseGet(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **Integer**| The number of results to skip. | [optional] 
 **limit** | **Integer**| The maximum number of results to return. | [optional] 
 **where** | **String**| JSON formatted string. | [optional] 
 **sort** | **String**| Attribute used to sort results. | [optional] 

### Return type

[**[Response]**](Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="responsePost"></a>
# **responsePost**
> Response responsePost(body)

Create a Response

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

var apiInstance = new CrowdemotionApiClientJs.ResponseApi();

var body = new CrowdemotionApiClientJs.ResponseCreation(); // ResponseCreation | Request body


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.responsePost(body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResponseCreation**](ResponseCreation.md)| Request body | 

### Return type

[**Response**](Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="responseResponseIdDelete"></a>
# **responseResponseIdDelete**
> &#39;String&#39; responseResponseIdDelete(responseId)

Delete a Response

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

var apiInstance = new CrowdemotionApiClientJs.ResponseApi();

var responseId = 56; // Integer | ID of Response to update.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.responseResponseIdDelete(responseId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **responseId** | **Integer**| ID of Response to update. | 

### Return type

**&#39;String&#39;**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="responseResponseIdGet"></a>
# **responseResponseIdGet**
> Response responseResponseIdGet(responseId)

Find a Response

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

var apiInstance = new CrowdemotionApiClientJs.ResponseApi();

var responseId = 56; // Integer | ID of the Response


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.responseResponseIdGet(responseId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **responseId** | **Integer**| ID of the Response | 

### Return type

[**Response**](Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="responseResponseIdMetadataGet"></a>
# **responseResponseIdMetadataGet**
> ResponseMetadataResponse responseResponseIdMetadataGet(responseId)

Show Response Metadata

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

var apiInstance = new CrowdemotionApiClientJs.ResponseApi();

var responseId = 56; // Integer | ID of the Response


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.responseResponseIdMetadataGet(responseId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **responseId** | **Integer**| ID of the Response | 

### Return type

[**ResponseMetadataResponse**](ResponseMetadataResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="responseResponseIdMetadataPost"></a>
# **responseResponseIdMetadataPost**
> ResponseMetadataResponse responseResponseIdMetadataPost(responseId, body)

Add Response Metadata

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

var apiInstance = new CrowdemotionApiClientJs.ResponseApi();

var responseId = 56; // Integer | ID of the Response.

var body = new CrowdemotionApiClientJs.ResponseMetadata(); // ResponseMetadata | Request body


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.responseResponseIdMetadataPost(responseId, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **responseId** | **Integer**| ID of the Response. | 
 **body** | [**ResponseMetadata**](ResponseMetadata.md)| Request body | 

### Return type

[**ResponseMetadataResponse**](ResponseMetadataResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="responseResponseIdPut"></a>
# **responseResponseIdPut**
> Response responseResponseIdPut(responseId, body)

Update a Response

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

var apiInstance = new CrowdemotionApiClientJs.ResponseApi();

var responseId = 56; // Integer | ID of Response to update.

var body = new CrowdemotionApiClientJs.ResponseCreation(); // ResponseCreation | Request body


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.responseResponseIdPut(responseId, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **responseId** | **Integer**| ID of Response to update. | 
 **body** | [**ResponseCreation**](ResponseCreation.md)| Request body | 

### Return type

[**Response**](Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

