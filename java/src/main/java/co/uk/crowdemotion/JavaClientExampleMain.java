package co.uk.crowdemotion;

import io.swagger.client.model.Research;

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
            System.out.println("EXCEPTION!: " + exception.getMessage());
            System.out.println("Response code: "+exception.getCode());
            System.out.println("Response body: "+exception.getResponseBody());
        }
    }

}
