/**
 * Created by ipeluffo on 7/25/16.

 */

var CrowdemotionApiClient = require('crowdemotion-api-client-js');

var defaultClient = CrowdemotionApiClient.ApiClient.instance;

var apiKey = defaultClient.authentications['api_key'];
apiKey.apiKey = "YOUR API KEY";

var api = new CrowdemotionApiClient.ResearchApi();

api.researchGet({}, function (error, data, response) {
  if (error) {
    console.log(error.response.error);
    return;
  }

  console.log("API called successfully.\n\n");

  for (var i = 0; i < data.length; i++) {
    console.log(data[i]);
  }

});
