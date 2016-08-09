<?php

require_once(__DIR__ . '/crowdemotion-api-client-php/autoload.php');

date_default_timezone_set('Europe/London');

$API_KEY = 'YOU_API_KEY';
$PATH_TO_VIDEO_FILE = 'path/to/videofile.mp4';

// Configure API key authorization: api_key
Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', $API_KEY);

$api_instance = new Swagger\Client\Api\ResearchApi();

try {
    $result = $api_instance->researchGet();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ResearchApi->researchGet: ', $e->getMessage(), PHP_EOL;
}


$facevideo_api_instance = new Swagger\Client\Api\FaceVideoApi();

$facevideo_api_result = null;
try {
    $filename = $PATH_TO_VIDEO_FILE;
    $facevideo_api_result = $facevideo_api_instance->facevideoPost($filename, true, null, null, null, null, true);
    print_r($facevideo_api_result);
} catch (Exception $e) {
    echo 'Exception when calling FaceVideoApi->facevideoPost: ', $e->getMessage(), PHP_EOL;
}

echo '>>> Get auto-generated random time-series (since the "sandbox" parameter was sent as True):', PHP_EOL;

if ($facevideo_api_result != null) {
    $timeseries_api_instance = new Swagger\Client\Api\TimeseriesApi();
    $ts_api_response = array();
    try {
        $ts_found = false;
        while (!$ts_found) {
            $ts_api_response = $timeseries_api_instance->timeseriesGet($facevideo_api_result->getResponseId());
            if (count($ts_api_response) == 0) {
                echo "The random timeseries is not ready yet. Wait 10 seconds and retry...", PHP_EOL;
                sleep(10);
            } else {
                $ts_found = true;
            }
        }

        # Take the first random metric
        echo "response_id: " . $ts_api_response[0]->getResponseId(), PHP_EOL;
        echo "metric_id: " . $ts_api_response[0]->getMetricId(), PHP_EOL;
        echo "metric_name: " . $ts_api_response[0]->getMetricName(), PHP_EOL;
        echo "start_index: " . $ts_api_response[0]->getStartIndex(), PHP_EOL;
        echo "end_index: " . $ts_api_response[0]->getEndIndex(), PHP_EOL;
        echo "step_size: " . $ts_api_response[0]->getStepSize(), PHP_EOL;
        echo "custom_message: " . $ts_api_response[0]->getCustomMessage(), PHP_EOL;
        echo "data amount: " . count($ts_api_response[0]->getData()), PHP_EOL;

    } catch (Exception $e) {
        echo("Exception when calling TimeSeriesAPI");
        echo("Exception detail: " . $e);
    }
} else {
    echo("The FaceVideo upload didn't finish successfully, then skip the search of the Time-series");
}


?>

