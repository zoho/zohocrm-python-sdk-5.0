from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.service_preference import ServicePreferenceOperations, BodyWrapper, \
    ServicePreference, APIException, SuccessResponse, ActionWrapper


class UpdateServicePreference(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_service_preferences():
        service_preference_operations = ServicePreferenceOperations()
        request = BodyWrapper()
        service_preference = ServicePreference()
        service_preference.set_job_sheet_enabled(True)
        request.set_service_preferences(service_preference)
        response = service_preference_operations.update_service_preference(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response = response_object.get_service_preferences()
                    if isinstance(action_response, SuccessResponse):
                        print("Status: " + action_response.get_status().get_value())
                        print("Code: " + action_response.get_code().get_value())
                        print("Details")
                        details = action_response.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + action_response.get_message().get_value())
                    elif isinstance(action_response, APIException):
                        print("Status: " + action_response.get_status().get_value())
                        print("Code: " + action_response.get_code().get_value())
                        print("Details")
                        details = action_response.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + action_response.get_message())

                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


UpdateServicePreference.initialize()
UpdateServicePreference.update_service_preferences()