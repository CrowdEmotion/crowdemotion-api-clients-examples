# CrowdemotionApiClientJs.ResearchApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**researchGet**](ResearchApi.md#researchGet) | **GET** /research | Find all Research
[**researchPost**](ResearchApi.md#researchPost) | **POST** /research | Create a Research Project
[**researchResearchIdDelete**](ResearchApi.md#researchResearchIdDelete) | **DELETE** /research/{research_id} | Delete Research Project
[**researchResearchIdGet**](ResearchApi.md#researchResearchIdGet) | **GET** /research/{research_id} | Find a Research Project
[**researchResearchIdPut**](ResearchApi.md#researchResearchIdPut) | **PUT** /research/{research_id} | Edit Research Project details


<a name="researchGet"></a>
# **researchGet**
> [Research] researchGet(opts)

Find all Research

&lt;p&gt;Returns all the Research created by an admin user.&lt;/p&gt; &lt;p&gt;&lt;strong&gt;Permissions:&lt;/strong&gt; ✓ Respondent ✗ Customer ✓ Manager&lt;/p&gt;

### Example
```javascript
var CrowdemotionApiClientJs = require('crowdemotion-api-client-js');
var defaultClient = CrowdemotionApiClientJs.ApiClient.default;

// Configure API key authorization: api_key
var api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

var apiInstance = new CrowdemotionApiClientJs.ResearchApi();

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
apiInstance.researchGet(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **Integer**| The number of results to skip. | [optional] 
 **limit** | **Integer**| The maximum number of results to return. | [optional] 
 **where** | **String**| JSON formatted string condition. | [optional] 
 **sort** | **String**| Attribute used to sort results. | [optional] 

### Return type

[**[Research]**](Research.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="researchPost"></a>
# **researchPost**
> Research researchPost(body)

Create a Research Project

&lt;p&gt;New research projects can only be created with an admin account.&lt;/p&gt; &lt;p&gt;&lt;strong&gt;Permissions:&lt;/strong&gt; ✗ Respondent ✗ Customer ✓ Manager&lt;/p&gt;

### Example
```javascript
var CrowdemotionApiClientJs = require('crowdemotion-api-client-js');
var defaultClient = CrowdemotionApiClientJs.ApiClient.default;

// Configure API key authorization: api_key
var api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

var apiInstance = new CrowdemotionApiClientJs.ResearchApi();

var body = new CrowdemotionApiClientJs.ResearchCreation(); // ResearchCreation | Request body


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.researchPost(body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResearchCreation**](ResearchCreation.md)| Request body | 

### Return type

[**Research**](Research.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="researchResearchIdDelete"></a>
# **researchResearchIdDelete**
> &#39;String&#39; researchResearchIdDelete(researchId)

Delete Research Project

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

var apiInstance = new CrowdemotionApiClientJs.ResearchApi();

var researchId = 56; // Integer | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.researchResearchIdDelete(researchId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **researchId** | **Integer**|  | 

### Return type

**&#39;String&#39;**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="researchResearchIdGet"></a>
# **researchResearchIdGet**
> Research researchResearchIdGet(researchId)

Find a Research Project

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

var apiInstance = new CrowdemotionApiClientJs.ResearchApi();

var researchId = 56; // Integer | ID of Research Project to be found.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.researchResearchIdGet(researchId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **researchId** | **Integer**| ID of Research Project to be found. | 

### Return type

[**Research**](Research.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="researchResearchIdPut"></a>
# **researchResearchIdPut**
> Research researchResearchIdPut(researchId, body)

Edit Research Project details

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

var apiInstance = new CrowdemotionApiClientJs.ResearchApi();

var researchId = 56; // Integer | 

var body = new CrowdemotionApiClientJs.ResearchCreation(); // ResearchCreation | Request body


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.researchResearchIdPut(researchId, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **researchId** | **Integer**|  | 
 **body** | [**ResearchCreation**](ResearchCreation.md)| Request body | 

### Return type

[**Research**](Research.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

