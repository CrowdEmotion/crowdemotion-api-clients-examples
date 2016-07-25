# CrowdemotionApiClientJs.UserApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userIdGet**](UserApi.md#userIdGet) | **GET** /user/{id} | Get User information
[**userIdPut**](UserApi.md#userIdPut) | **PUT** /user/{id} | Edit User information
[**userLoginPost**](UserApi.md#userLoginPost) | **POST** /user/login | User Login
[**userUserIdMetadataGet**](UserApi.md#userUserIdMetadataGet) | **GET** /user/{user_id}/metadata | Find User metadata
[**userUserIdMetadataPost**](UserApi.md#userUserIdMetadataPost) | **POST** /user/{user_id}/metadata | Add user metadata


<a name="userIdGet"></a>
# **userIdGet**
> User userIdGet(id)

Get User information

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

var apiInstance = new CrowdemotionApiClientJs.UserApi();

var id = 56; // Integer | User unique ID


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.userIdGet(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| User unique ID | 

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="userIdPut"></a>
# **userIdPut**
> User userIdPut(id, body)

Edit User information

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

var apiInstance = new CrowdemotionApiClientJs.UserApi();

var id = "id_example"; // String | ID of User to update.

var body = new CrowdemotionApiClientJs.UserUpdateBody(); // UserUpdateBody | Request body


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.userIdPut(id, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of User to update. | 
 **body** | [**UserUpdateBody**](UserUpdateBody.md)| Request body | 

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="userLoginPost"></a>
# **userLoginPost**
> LoginResponse userLoginPost(body)

User Login

&lt;p&gt;&lt;strong&gt;Permissions:&lt;/strong&gt; No authorization is required&lt;/p&gt;

### Example
```javascript
var CrowdemotionApiClientJs = require('crowdemotion-api-client-js');
var defaultClient = CrowdemotionApiClientJs.ApiClient.default;

// Configure API key authorization: api_key
var api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

var apiInstance = new CrowdemotionApiClientJs.UserApi();

var body = new CrowdemotionApiClientJs.Login(); // Login | Request body


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.userLoginPost(body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Login**](Login.md)| Request body | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="userUserIdMetadataGet"></a>
# **userUserIdMetadataGet**
> UserMetadataResponse userUserIdMetadataGet(userId)

Find User metadata

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

var apiInstance = new CrowdemotionApiClientJs.UserApi();

var userId = 56; // Integer | ID of User.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.userUserIdMetadataGet(userId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **Integer**| ID of User. | 

### Return type

[**UserMetadataResponse**](UserMetadataResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="userUserIdMetadataPost"></a>
# **userUserIdMetadataPost**
> UserMetadataResponse userUserIdMetadataPost(userId, body)

Add user metadata

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

var apiInstance = new CrowdemotionApiClientJs.UserApi();

var userId = 56; // Integer | ID of User.

var body = new CrowdemotionApiClientJs.UserMetadata(); // UserMetadata | Request body


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.userUserIdMetadataPost(userId, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **Integer**| ID of User. | 
 **body** | [**UserMetadata**](UserMetadata.md)| Request body | 

### Return type

[**UserMetadataResponse**](UserMetadataResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

