from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.users import UsersOperations, BodyWrapper, Users, Role, ActionWrapper, \
    SuccessResponse, APIException


class UpdateUsers:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_users():
        """
        This method is used to update the details of multiple users of your organization and print the response.
        """
        users_operations = UsersOperations()
        request = BodyWrapper()
        # List to hold User instances
        user_list = []
        user_1 = Users()
        user_1.set_id(3477061012716004)
        role = Role()
        role.set_id(34770610026005)
        user_1.set_role(role)
        user_1.set_country_locale('en_US')
        # Add User instance to list
        user_list.append(user_1)
        user_2 = Users()
        user_2.set_id(34096430302042)
        role = Role()
        role.set_id(34096430026008)
        user_2.set_role(role)
        user_2.set_country_locale('en_US')
        # Add User instance to list
        user_list.append(user_2)
        request.set_users(user_list)
        # Call update_users method that takes BodyWrapper instance as parameter
        response = users_operations.update_users(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_users()
                    for action_response in action_response_list:
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
                            print("Message: " + action_response.get_message())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


UpdateUsers.initialize()
UpdateUsers.update_users()
