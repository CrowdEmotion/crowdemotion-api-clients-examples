# Swagger\Client\FaceVideoApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**facevideoFacevideoIdDelete**](FaceVideoApi.md#facevideoFacevideoIdDelete) | **DELETE** /facevideo/{facevideo_id} | Delete a FaceVideo
[**facevideoGet**](FaceVideoApi.md#facevideoGet) | **GET** /facevideo | Find a FaceVideo
[**facevideoPost**](FaceVideoApi.md#facevideoPost) | **POST** /facevideo | Analyse FaceVideo
[**facevideoPut**](FaceVideoApi.md#facevideoPut) | **PUT** /facevideo | Analyse FaceVideo


# **facevideoFacevideoIdDelete**
> string facevideoFacevideoIdDelete($facevideo_id)

Delete a FaceVideo

<p>Use this operation to delete a FaceVideo.</p> <p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\FaceVideoApi();
$facevideo_id = 56; // int | ID of FaceVideo to be deleted.

try {
    $result = $api_instance->facevideoFacevideoIdDelete($facevideo_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FaceVideoApi->facevideoFacevideoIdDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facevideo_id** | **int**| ID of FaceVideo to be deleted. |

### Return type

**string**

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **facevideoGet**
> \Swagger\Client\Model\FaceVideo facevideoGet($facevideo_id, $response_id)

Find a FaceVideo

<p>Use this operation to access information about the FaceVideo analysis.</p> <p><i>Any one of the two parameters must be specified.</i></p> <p>To discover if the video has been analyzed, check the meaning of status field in the following table:</p> <table>   <tr><td>Value</td> <td>Description</td></tr>   <tr><td>0</td> <td>Not started</td></tr>   <tr><td>1</td> <td>Processing started</td></tr>   <tr><td>2</td> <td>Processing completed</td></tr>   <tr><td>-1</td> <td>Error</td></tr> </table> <p><strong>Permissions:</strong> ✓ Respondent ✓ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\FaceVideoApi();
$facevideo_id = 56; // int | FaceVideo ID. NOTE: Only this parameter is considered if both are specified.
$response_id = 56; // int | Response ID corresponding to the FaceVideo.

try {
    $result = $api_instance->facevideoGet($facevideo_id, $response_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FaceVideoApi->facevideoGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facevideo_id** | **int**| FaceVideo ID. NOTE: Only this parameter is considered if both are specified. | [optional]
 **response_id** | **int**| Response ID corresponding to the FaceVideo. | [optional]

### Return type

[**\Swagger\Client\Model\FaceVideo**](../Model/FaceVideo.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **facevideoPost**
> \Swagger\Client\Model\FaceVideo facevideoPost($filename, $sandbox, $response_id, $research_id, $media_id, $respondent_id, $process_video)

Analyse FaceVideo

<p>Starts the analysis of a single FaceVideo (in the supported formats) through either:</p> <ol>   <li>a video URL pointing to a resource accessible through the Internet without authentication</li>   <li>the binary contents of the video in the request's body, encoded as <code>multipart/form-data</code> content type</li> </ol> <p>The third option is a <code>PUT</code> call to <code>/v1/facevideo/{filename}</code> (<code>filename</code> required string e.g. <code>facevideo1.mp4</code>) which supports all the URL parameters as above with a body encoding <code>application/octet-stream</code> and the file contents as plain binary: this call makes uploads more efficient but it does not respect HTTP/RESTful standards so it may be not supported in future.</p> <p><strong>Permissions:</strong> ✓ Respondent ✓ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\FaceVideoApi();
$filename = "/path/to/file.txt"; // \SplFileObject | FaceVideo to be analysed.
$sandbox = true; // bool | Generates random data for testing, at no cost. Default: false.
$response_id = 56; // int | Associates this Facevideo to a previously generated Response.
$research_id = 56; // int | Associates this Facevideo to a previously generated Research.
$media_id = 56; // int | Associates this Facevideo to a previously generated Media.
$respondent_id = 56; // int | Associates this Facevideo to a previously generated Respondent.
$process_video = true; // bool | Actually processes the video. Default: true.

try {
    $result = $api_instance->facevideoPost($filename, $sandbox, $response_id, $research_id, $media_id, $respondent_id, $process_video);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FaceVideoApi->facevideoPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **\SplFileObject**| FaceVideo to be analysed. | [optional]
 **sandbox** | **bool**| Generates random data for testing, at no cost. Default: false. | [optional]
 **response_id** | **int**| Associates this Facevideo to a previously generated Response. | [optional]
 **research_id** | **int**| Associates this Facevideo to a previously generated Research. | [optional]
 **media_id** | **int**| Associates this Facevideo to a previously generated Media. | [optional]
 **respondent_id** | **int**| Associates this Facevideo to a previously generated Respondent. | [optional]
 **process_video** | **bool**| Actually processes the video. Default: true. | [optional]

### Return type

[**\Swagger\Client\Model\FaceVideo**](../Model/FaceVideo.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **facevideoPut**
> \Swagger\Client\Model\FaceVideo facevideoPut($sandbox, $response_id, $research_id, $media_id, $respondent_id, $process_video, $body)

Analyse FaceVideo

<p>Starts the analysis of a single FaceVideo (in the supported formats) through either:</p> <ol>   <li>a video URL pointing to a resource accessible through the Internet without authentication</li>   <li>the binary contents of the video in the request's body, encoded as <code>multipart/form-data</code> content type</li> </ol> <p>The third option is a <code>PUT</code> call to <code>/v1/facevideo/{filename}</code> (<code>filename</code> required string e.g. <code>facevideo1.mp4</code>) which supports all the URL parameters as above with a body encoding <code>application/octet-stream</code> and the file contents as plain binary: this call makes uploads more efficient but it does not respect HTTP/RESTful standards so it may be not supported in future.</p> <p><strong>Permissions:</strong> ✓ Respondent ✓ Customer ✓ Manager</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');

$api_instance = new Swagger\Client\Api\FaceVideoApi();
$sandbox = true; // bool | Generates random data for testing, at no cost. Default: false.
$response_id = 56; // int | Associates this Facevideo to a previously generated Response.
$research_id = 56; // int | Associates this Facevideo to a previously generated Research.
$media_id = 56; // int | Associates this Facevideo to a previously generated Media.
$respondent_id = 56; // int | Associates this Facevideo to a previously generated Respondent.
$process_video = true; // bool | Actually processes the video. Default: true.
$body = new \Swagger\Client\Model\FaceVideoUpload(); // \Swagger\Client\Model\FaceVideoUpload | Request body

try {
    $result = $api_instance->facevideoPut($sandbox, $response_id, $research_id, $media_id, $respondent_id, $process_video, $body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FaceVideoApi->facevideoPut: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox** | **bool**| Generates random data for testing, at no cost. Default: false. | [optional]
 **response_id** | **int**| Associates this Facevideo to a previously generated Response. | [optional]
 **research_id** | **int**| Associates this Facevideo to a previously generated Research. | [optional]
 **media_id** | **int**| Associates this Facevideo to a previously generated Media. | [optional]
 **respondent_id** | **int**| Associates this Facevideo to a previously generated Respondent. | [optional]
 **process_video** | **bool**| Actually processes the video. Default: true. | [optional]
 **body** | [**\Swagger\Client\Model\FaceVideoUpload**](../Model/\Swagger\Client\Model\FaceVideoUpload.md)| Request body | [optional]

### Return type

[**\Swagger\Client\Model\FaceVideo**](../Model/FaceVideo.md)

### Authorization

[api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

