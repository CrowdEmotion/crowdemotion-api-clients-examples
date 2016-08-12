/**
 * Created by ipeluffo on 7/25/16.

 */

var CrowdemotionApiClient = require('crowdemotion-api-client-js');

var defaultClient = CrowdemotionApiClient.ApiClient.instance;
defaultClient.authentications['api_key'].apiKey = "YOUR_API_KEY";

console.log("\n\n>>> Found Research example: \n");

var api = new CrowdemotionApiClient.ResearchApi();

api.researchGet({}, function (error, data, response) {
  if (error) {
    console.log(error.response.error);
    return;
  }

  console.log("API called successfully.\n\n");

  console.log("First Research found");
  console.log(data[0]);

});

////////////////////////////////////////////////////////////////////////////////

console.log("\n\n>>> FaceVideo upload example: \n");

var faceVideoApi = new CrowdemotionApiClient.FaceVideoApi();
var faceVideoPostOpts = {
  'filename' : new require('fs').ReadStream('/path/to/video.mp4'),
  'sandbox' : true,
  'processVideo': true
};

faceVideoApi.facevideoPost(faceVideoPostOpts, function (error, faceVideo, response) {
  if (error) {
    console.log(error);
    return;
  }

  console.log(faceVideo);

  if (faceVideo != null) {
    var timeseriesApi = new CrowdemotionApiClient.TimeseriesApi();

    function findFacevideoTimeseries() {
      console.log('\n\n>>> Get auto-generated random time-series (since the "sandbox" parameter was sent as True): \n');

      timeseriesApi.timeseriesGet(faceVideo.responseId, {}, function (err, timeseries, response) {
        if (!timeseries || timeseries.length == 0) {
          console.log("The random timeseries is not ready yet. Wait 10 seconds and retry...");
          setTimeout(findFacevideoTimeseries, 10000);
        } else {
          // Take the first random metric
          console.log("response_id: " + timeseries[0].responseId);
          console.log("metric_id: " + timeseries[0].metricId);
          console.log("metric_name: " + timeseries[0].metricName);
          console.log("start_index: " + timeseries[0].startIndex);
          console.log("end_index: " + timeseries[0].endIndex);
          console.log("step_size: " + timeseries[0].stepSize);
          console.log("custom_message: " + timeseries[0].customMessage);
          console.log("data amount: " + timeseries[0].data.length);
        }
      });
    }

    findFacevideoTimeseries();

  } else {
    console.log("The FaceVideo upload didn't finish successfully, then skip the search of the Time-series");
  }

});