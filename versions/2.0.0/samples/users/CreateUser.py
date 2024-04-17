from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.users import UsersOperations, BodyWrapper, Users, Role, Profile, ActionWrapper, \
    SuccessResponse, APIException


class CreateUser:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_user():
        """
        This method is used to add a user to your organization and print the response.
        """
        users_operations = UsersOperations()
        request = BodyWrapper()
        # List to hold User instances
        user_list = []
        user = Users()
        role = Role()
        role.set_id(4402480031151)
        user.set_role(role)
        user.set_country_locale('en_US')
        user.set_first_name('Test')
        user.set_last_name('User')
        user.set_email('testuser-1234567@zoho.com')
        profile = Profile()
        profile.set_id(4402480031160)
        user.set_profile(profile)
        # Add the User instance to list
        user_list.append(user)
        request.set_users(user_list)
        # Call create_user method that takes RequestWrapper class instance as parameter
        response = users_operations.create_users(request)
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


CreateUser.initialize()
CreateUser.create_user()