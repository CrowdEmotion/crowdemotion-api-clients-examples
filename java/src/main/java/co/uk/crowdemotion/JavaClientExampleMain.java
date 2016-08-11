package co.uk.crowdemotion;

import io.swagger.client.model.FaceVideo;
import io.swagger.client.model.Research;
import io.swagger.client.model.Timeseries;

import java.io.File;
import java.util.List;

/**
 * Created by ipeluffo on 7/21/16.
 */
public class JavaClientExampleMain {

    private static final String API_TOKEN = "YOUR_USER_API_TOKEN";

    public static void main(String[] args) {
        ApiClient apiClient = new ApiClient();

        apiClient.addDefaultHeader("Authorization", API_TOKEN);

//         It is not supported in the current implementation
//         apiClient.setApiKey(API_TOKEN);

        System.out.println("API BASE PATH: " + apiClient.getBasePath());

        ResearchApi researchApi = new ResearchApi(apiClient);

        try {
            List<Research> researchList = researchApi.researchGet(null, 10, null, null);

            System.out.println(researchList.size() + " research found");
            for (Research research : researchList) {
                System.out.println(research.toString());
            }
        } catch (ApiException exception) {
            printException(exception);
        }

        //////////////////////////////////////////////////////////////////////////////////////////

        System.out.println("\n\n>>> FaceVideo upload example: \n");

        FaceVideoApi faceVideoApi = new FaceVideoApi(apiClient);
        FaceVideo faceVideo = null;
        try {
            String facevideoPath = "path/to/video.mp4";
            faceVideo = faceVideoApi.facevideoPost(new File(facevideoPath), true, null, null, null, null, true);
            System.out.println(faceVideo);
        } catch (ApiException exception) {
            printException(exception);
        }

        //////////////////////////////////////////////////////////////////////////////////////////

        System.out.println("\n\n>>> Get auto-generated random time-series (since the 'sandbox' parameter was sent as True): \n");
        if (faceVideo != null) {
            try {
                TimeseriesApi timeseriesApi = new TimeseriesApi(apiClient);
                List<Timeseries> timeseries = null;
                boolean tsFound = false;
                while (!tsFound) {
                    timeseries = timeseriesApi.timeseriesGet(Integer.parseInt(faceVideo.getResponseId()), null, null, null);
                    if (timeseries.size() < 1) {
                        System.out.println("The random timeseries is not ready yet. Wait 10 seconds and retry...");
                        Thread.sleep(10000);
                    } else {
                        tsFound = true;
                    }
                }

                System.out.println("response_id: " + timeseries.get(0).getResponseId());
                System.out.println("metric_id: " + timeseries.get(0).getMetricId());
                System.out.println("metric_name: " + timeseries.get(0).getMetricName());
                System.out.println("start_index: " + timeseries.get(0).getStartIndex());
                System.out.println("end_index: " + timeseries.get(0).getEndIndex());
                System.out.println("step_size: " + timeseries.get(0).getStepSize());
                System.out.println("custom_message: " + timeseries.get(0).getCustomMessage());
                System.out.println("data amount: " + timeseries.get(0).getData().size());
            } catch (ApiException e) {
                printException(e);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        } else {
            System.out.println("The FaceVideo upload didn't finish successfully, then skip the search of the Time-series");
        }
    }

    private static void printException(ApiException exception) {
        System.out.println("EXCEPTION!: " + exception.getMessage());
        System.out.println("Response code: "+exception.getCode());
        System.out.println("Response body: "+exception.getResponseBody());
    }

}
