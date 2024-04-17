from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.profiles import ProfilesOperations, ActionWrapper, \
    SuccessResponse, APIException, DeleteProfileParam


class DeleteProfile:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def delete_profile(profile_id, existing_profile_id):
        profiles_operations = ProfilesOperations()
        param_instance = ParameterMap()
        param_instance.add(DeleteProfileParam.transfer_to, existing_profile_id)
        response = profiles_operations.delete_profile(profile_id, param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            action_response = response.get_object()
            if action_response is not None:
                if isinstance(action_response, SuccessResponse):
                    print("Status: " + action_response.get_status().get_value())
                    print("Code: " + action_response.get_code().get_value())
                    print("Details")
                    details = action_response.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + action_response.get_message())
                elif isinstance(action_response, APIException):
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
                    print("Message: " + action_response.get_message().get_value())


profile_id = 440248001475027
existing_profile_id = 4402480031157
DeleteProfile.initialize()
DeleteProfile.delete_profile(profile_id, existing_profile_id)