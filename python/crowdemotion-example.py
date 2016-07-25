import crowdemotion_api_client_python
from crowdemotion_api_client_python.rest import ApiException
from pprint import pprint

API_KEY = "USER_API_KEY"

crowdemotion_api_client_python.configuration.api_key['Authorization'] = API_KEY

api_instance = crowdemotion_api_client_python.ResearchApi()

try:
	api_response = api_instance.research_get()
	pprint(api_response)

except ApiException as e:
	print "Exception when calling ResearchAPI"
	print e
