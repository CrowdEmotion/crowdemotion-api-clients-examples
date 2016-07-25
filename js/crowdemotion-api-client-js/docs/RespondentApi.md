# CrowdemotionApiClientJs.RespondentApi

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


<a name="respondentGet"></a>
# **respondentGet**
> [Respondent] respondentGet(researchId, opts)

Find all Respondents of a Research

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

var apiInstance = new CrowdemotionApiClientJs.RespondentApi();

var researchId = 56; // Integer | Search by research id.

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
apiInstance.respondentGet(researchId, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **researchId** | **Integer**| Search by research id. | 
 **skip** | **Integer**| The number of results to skip. | [optional] 
 **limit** | **Integer**| The maximum number of results to return. | [optional] 
 **where** | **String**| JSON formatted string. | [optional] 
 **sort** | **String**| Attribute used to sort results. | [optional] 

### Return type

[**[Respondent]**](Respondent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="respondentPost"></a>
# **respondentPost**
> Respondent respondentPost(body)

Create a Respondent

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

var apiInstance = new CrowdemotionApiClientJs.RespondentApi();

var body = new CrowdemotionApiClientJs.Respondent(); // Respondent | Request body


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.respondentPost(body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Respondent**](Respondent.md)| Request body | 

### Return type

[**Respondent**](Respondent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="respondentRespondentIdDelete"></a>
# **respondentRespondentIdDelete**
> &#39;String&#39; respondentRespondentIdDelete(respondentId)

Delete a Respondent

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

var apiInstance = new CrowdemotionApiClientJs.RespondentApi();

var respondentId = 56; // Integer | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.respondentRespondentIdDelete(respondentId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **respondentId** | **Integer**|  | 

### Return type

**&#39;String&#39;**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="respondentRespondentIdGet"></a>
# **respondentRespondentIdGet**
> Respondent respondentRespondentIdGet(respondentId)

Find a Respondent

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

var apiInstance = new CrowdemotionApiClientJs.RespondentApi();

var respondentId = 56; // Integer | Search by research id.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.respondentRespondentIdGet(respondentId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **respondentId** | **Integer**| Search by research id. | 

### Return type

[**Respondent**](Respondent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="respondentRespondentIdMetadataGet"></a>
# **respondentRespondentIdMetadataGet**
> RespondentMetadataResponse respondentRespondentIdMetadataGet(respondentId)

Find Respondent Metadata

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

var apiInstance = new CrowdemotionApiClientJs.RespondentApi();

var respondentId = 56; // Integer | ID of the Respondent


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.respondentRespondentIdMetadataGet(respondentId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **respondentId** | **Integer**| ID of the Respondent | 

### Return type

[**RespondentMetadataResponse**](RespondentMetadataResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="respondentRespondentIdMetadataPost"></a>
# **respondentRespondentIdMetadataPost**
> RespondentMetadataResponse respondentRespondentIdMetadataPost(respondentId, body)

Add Respondent Metadata

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

var apiInstance = new CrowdemotionApiClientJs.RespondentApi();

var respondentId = 56; // Integer | 

var body = new CrowdemotionApiClientJs.RespondentMetadata(); // RespondentMetadata | Request body


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.respondentRespondentIdMetadataPost(respondentId, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **respondentId** | **Integer**|  | 
 **body** | [**RespondentMetadata**](RespondentMetadata.md)| Request body | 

### Return type

[**RespondentMetadataResponse**](RespondentMetadataResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="respondentRespondentIdPut"></a>
# **respondentRespondentIdPut**
> Respondent respondentRespondentIdPut(respondentId, body)

Update a Respondent

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

var apiInstance = new CrowdemotionApiClientJs.RespondentApi();

var respondentId = 56; // Integer | 

var body = new CrowdemotionApiClientJs.Respondent(); // Respondent | Request body


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.respondentRespondentIdPut(respondentId, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **respondentId** | **Integer**|  | 
 **body** | [**Respondent**](Respondent.md)| Request body | 

### Return type

[**Respondent**](Respondent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

