import datetime

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.users_unavailability import UsersUnavailabilityOperations, BodyWrapper, \
    UsersUnavailability, User, ActionWrapper, SuccessResponse, APIException


class UpdateUsersUnavailabilites(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_users_unavailabilities():
        user_operations = UsersUnavailabilityOperations()
        request = BodyWrapper()
        user_list =[]
        user1 = UsersUnavailability()
        user1.set_id(32312323113)
        user1.set_comments("Unavailable")
        user1.set_from(datetime.datetime(2023, 9, 2, 11, 9, 1))
        user1.set_to(datetime.datetime(2023, 9, 3, 11, 0, 1))
        user = User()
        user.set_id(32324223232132)
        user1.set_user(user)
        user_list.append(user1)
        request.set_users_unavailability(user_list)
        response = user_operations.update_users_unavailabilites(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_users_unavailability()
                    for action_response in action_response_list:
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
                            print("Message: " + action_response.get_message().get_value())

                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


UpdateUsersUnavailabilites.initialize()
UpdateUsersUnavailabilites.update_users_unavailabilities()