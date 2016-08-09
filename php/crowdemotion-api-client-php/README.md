# crowdemotion-api-client-php
CrowdEmotion API

This PHP package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.1.0
- Build date: 2016-08-09T14:25:17.592+01:00
- Build package: class io.swagger.codegen.languages.PhpClientCodegen

## Requirements

PHP 5.4.0 and later

## Installation & Usage
### Composer

To install the bindings via [Composer](http://getcomposer.org/), add the following to `composer.json`:

```
{
  "repositories": [
    {
      "type": "git",
      "url": "https://github.com/GIT_USER_ID/GIT_REPO_ID.git"
    }
  ],
  "require": {
    "GIT_USER_ID/GIT_REPO_ID": "*@dev"
  }
}
```

Then run `composer install`

### Manual Installation

Download the files and include `autoload.php`:

```php
    require_once('/path/to/crowdemotion-api-client-php/autoload.php');
```

## Tests

To run the unit tests:

```
composer install
./vendor/bin/phpunit lib/Tests
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FaceVideoApi* | [**facevideoFacevideoIdDelete**](docs/Api/FaceVideoApi.md#facevideofacevideoiddelete) | **DELETE** /facevideo/{facevideo_id} | Delete a FaceVideo
*FaceVideoApi* | [**facevideoGet**](docs/Api/FaceVideoApi.md#facevideoget) | **GET** /facevideo | Find a FaceVideo
*FaceVideoApi* | [**facevideoPost**](docs/Api/FaceVideoApi.md#facevideopost) | **POST** /facevideo | Analyse FaceVideo
*FaceVideoApi* | [**facevideoPut**](docs/Api/FaceVideoApi.md#facevideoput) | **PUT** /facevideo | Analyse FaceVideo
*MediaApi* | [**mediaGet**](docs/Api/MediaApi.md#mediaget) | **GET** /media | Find all registered Media
*MediaApi* | [**mediaMediaIdDelete**](docs/Api/MediaApi.md#mediamediaiddelete) | **DELETE** /media/{media_id} | Delete Media
*MediaApi* | [**mediaMediaIdGet**](docs/Api/MediaApi.md#mediamediaidget) | **GET** /media/{media_id} | Find a Media
*MediaApi* | [**mediaMediaIdPut**](docs/Api/MediaApi.md#mediamediaidput) | **PUT** /media/{media_id} | Update a Media
*MediaApi* | [**mediaPost**](docs/Api/MediaApi.md#mediapost) | **POST** /media | Create new Media
*MetricApi* | [**metricGet**](docs/Api/MetricApi.md#metricget) | **GET** /metric | List all registered metrics
*MetricApi* | [**metricMetricIdDelete**](docs/Api/MetricApi.md#metricmetriciddelete) | **DELETE** /metric/{metric_id} | Delete a Metric
*MetricApi* | [**metricMetricIdGet**](docs/Api/MetricApi.md#metricmetricidget) | **GET** /metric/{metric_id} | Find a Metric
*MetricApi* | [**metricPost**](docs/Api/MetricApi.md#metricpost) | **POST** /metric | Create Metric
*ResearchApi* | [**researchGet**](docs/Api/ResearchApi.md#researchget) | **GET** /research | Find all Research
*ResearchApi* | [**researchPost**](docs/Api/ResearchApi.md#researchpost) | **POST** /research | Create a Research Project
*ResearchApi* | [**researchResearchIdDelete**](docs/Api/ResearchApi.md#researchresearchiddelete) | **DELETE** /research/{research_id} | Delete Research Project
*ResearchApi* | [**researchResearchIdGet**](docs/Api/ResearchApi.md#researchresearchidget) | **GET** /research/{research_id} | Find a Research Project
*ResearchApi* | [**researchResearchIdPut**](docs/Api/ResearchApi.md#researchresearchidput) | **PUT** /research/{research_id} | Edit Research Project details
*RespondentApi* | [**respondentGet**](docs/Api/RespondentApi.md#respondentget) | **GET** /respondent | Find all Respondents of a Research
*RespondentApi* | [**respondentPost**](docs/Api/RespondentApi.md#respondentpost) | **POST** /respondent | Create a Respondent
*RespondentApi* | [**respondentRespondentIdDelete**](docs/Api/RespondentApi.md#respondentrespondentiddelete) | **DELETE** /respondent/{respondent_id} | Delete a Respondent
*RespondentApi* | [**respondentRespondentIdGet**](docs/Api/RespondentApi.md#respondentrespondentidget) | **GET** /respondent/{respondent_id} | Find a Respondent
*RespondentApi* | [**respondentRespondentIdMetadataGet**](docs/Api/RespondentApi.md#respondentrespondentidmetadataget) | **GET** /respondent/{respondent_id}/metadata | Find Respondent Metadata
*RespondentApi* | [**respondentRespondentIdMetadataPost**](docs/Api/RespondentApi.md#respondentrespondentidmetadatapost) | **POST** /respondent/{respondent_id}/metadata | Add Respondent Metadata
*RespondentApi* | [**respondentRespondentIdPut**](docs/Api/RespondentApi.md#respondentrespondentidput) | **PUT** /respondent/{respondent_id} | Update a Respondent
*ResponseApi* | [**responseGet**](docs/Api/ResponseApi.md#responseget) | **GET** /response | Find all Responses
*ResponseApi* | [**responsePost**](docs/Api/ResponseApi.md#responsepost) | **POST** /response | Create a Response
*ResponseApi* | [**responseResponseIdDelete**](docs/Api/ResponseApi.md#responseresponseiddelete) | **DELETE** /response/{response_id} | Delete a Response
*ResponseApi* | [**responseResponseIdGet**](docs/Api/ResponseApi.md#responseresponseidget) | **GET** /response/{response_id} | Find a Response
*ResponseApi* | [**responseResponseIdMetadataGet**](docs/Api/ResponseApi.md#responseresponseidmetadataget) | **GET** /response/{response_id}/metadata | Show Response Metadata
*ResponseApi* | [**responseResponseIdMetadataPost**](docs/Api/ResponseApi.md#responseresponseidmetadatapost) | **POST** /response/{response_id}/metadata | Add Response Metadata
*ResponseApi* | [**responseResponseIdPut**](docs/Api/ResponseApi.md#responseresponseidput) | **PUT** /response/{response_id} | Update a Response
*TimeseriesApi* | [**timeseriesDelete**](docs/Api/TimeseriesApi.md#timeseriesdelete) | **DELETE** /timeseries | Delete a Timeseries
*TimeseriesApi* | [**timeseriesGet**](docs/Api/TimeseriesApi.md#timeseriesget) | **GET** /timeseries | Get all recorded timeseries for a Response
*UserApi* | [**userIdGet**](docs/Api/UserApi.md#useridget) | **GET** /user/{id} | Get User information
*UserApi* | [**userIdPut**](docs/Api/UserApi.md#useridput) | **PUT** /user/{id} | Edit User information
*UserApi* | [**userLoginPost**](docs/Api/UserApi.md#userloginpost) | **POST** /user/login | User Login
*UserApi* | [**userUserIdMetadataGet**](docs/Api/UserApi.md#useruseridmetadataget) | **GET** /user/{user_id}/metadata | Find User metadata
*UserApi* | [**userUserIdMetadataPost**](docs/Api/UserApi.md#useruseridmetadatapost) | **POST** /user/{user_id}/metadata | Add user metadata


## Documentation For Models

 - [ContentDetails](docs/Model/ContentDetails.md)
 - [Data](docs/Model/Data.md)
 - [FaceVideo](docs/Model/FaceVideo.md)
 - [FaceVideoUpload](docs/Model/FaceVideoUpload.md)
 - [Login](docs/Model/Login.md)
 - [LoginResponse](docs/Model/LoginResponse.md)
 - [Media](docs/Model/Media.md)
 - [MediaCreation](docs/Model/MediaCreation.md)
 - [Metric](docs/Model/Metric.md)
 - [MetricCreation](docs/Model/MetricCreation.md)
 - [Research](docs/Model/Research.md)
 - [ResearchCreation](docs/Model/ResearchCreation.md)
 - [Respondent](docs/Model/Respondent.md)
 - [RespondentMetadata](docs/Model/RespondentMetadata.md)
 - [RespondentMetadataResponse](docs/Model/RespondentMetadataResponse.md)
 - [Response](docs/Model/Response.md)
 - [ResponseCreation](docs/Model/ResponseCreation.md)
 - [ResponseMetadata](docs/Model/ResponseMetadata.md)
 - [ResponseMetadataResponse](docs/Model/ResponseMetadataResponse.md)
 - [Statistics](docs/Model/Statistics.md)
 - [Stats](docs/Model/Stats.md)
 - [Status](docs/Model/Status.md)
 - [Tags](docs/Model/Tags.md)
 - [Timeseries](docs/Model/Timeseries.md)
 - [User](docs/Model/User.md)
 - [UserMetadata](docs/Model/UserMetadata.md)
 - [UserMetadataResponse](docs/Model/UserMetadataResponse.md)
 - [UserUpdateBody](docs/Model/UserUpdateBody.md)
 - [Videodetails](docs/Model/Videodetails.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



