import crowdemotion_api_client_python
from crowdemotion_api_client_python.rest import ApiException
from pprint import pprint
import time

API_KEY = "USER_API_KEY"

crowdemotion_api_client_python.configuration.api_key['Authorization'] = API_KEY

print("\n\n>>> Found Research example: \n")

research_api_instance = crowdemotion_api_client_python.ResearchApi()
try:
    api_response = research_api_instance.research_get()
    if len(api_response) > 0:
        pprint(api_response[0])
    else:
        pprint("No Research found!")

except ApiException as e:
    print("Exception when calling ResearchAPI")
    print(e)


print("\n\n>>> FaceVideo upload example: \n")

facevideo_api = crowdemotion_api_client_python.FaceVideoApi()
facevideo_api_response = None
try:
    facevideo_path = '/Users/ipeluffo/Development/crowdemotion/docs/misc/video.mp4'
    facevideo_api_response = facevideo_api.facevideo_post(filename=facevideo_path, sandbox=True, process_video=True)
    pprint(facevideo_api_response)
except ApiException as e:
    print("Exception when calling FaceVideoAPI")
    print("Exception detail: {}".format(e))


print('\n\n>>> Get auto-generated random time-series (since the "sandbox" parameter was sent as True): \n')

if facevideo_api_response is not None:
    timeseries_api = crowdemotion_api_client_python.TimeseriesApi()
    try:
        ts_found = False
        while not ts_found:
            ts_api_response = timeseries_api.timeseries_get(response_id=facevideo_api_response.response_id)
            if len(ts_api_response) == 0:
                print("The random timeseries is not ready yet. Wait 10 seconds and retry...")
                time.sleep(10)
            else:
                ts_found = True

        # Take the first random metric
        print("response_id: {}".format(ts_api_response[0].response_id))
        print("metric_id: {}".format(ts_api_response[0].metric_id))
        print("metric_name: {}".format(ts_api_response[0].metric_name))
        print("start_index: {}".format(ts_api_response[0].start_index))
        print("end_index: {}".format(ts_api_response[0].end_index))
        print("step_size: {}".format(ts_api_response[0].step_size))
        print("custom_message: {}".format(ts_api_response[0].custom_message))
        print("data amount: {}".format(str(len(ts_api_response[0].data))))

    except ApiException as e:
        print("Exception when calling TimeSeriesAPI")
        print("Exception detail: {}".format(e))
else:
    print("The FaceVideo upload didn't finish successfully, then skip the search of the Time-series")
