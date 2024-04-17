from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.user_type_users import UserTypeUsersOperations, ResponseWrapper, APIException


class GetUsersOfUserType(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_users_of_usertype(portal_name, user_type_id):
        user_type_operations = UserTypeUsersOperations()
        param_instance = ParameterMap()
        response = user_type_operations.get_users_of_user_type(user_type_id, portal_name, param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                users = response_object.get_users()
                for user in users:
                    print("Users PersonalityId: " + str(user.get_personality_id()))
                    print("Users Confirm: " + user.get_confirm())
                    print("Users StatusReasonS: " + user.get_status_reasonS())
                    print("Users InvitedTime: " + str(user.get_invited_time()))
                    print("Users Module: " + user.get_module())
                    print("Users Name: " + user.get_name())
                    print("Users Active: " + user.get_active())
                    print("Users Email: " + user.get_email())
                info = response_object.get_info()
                if info is not None:
                    if info.get_per_page() is not None:
                        print("User Info PerPage: " + str(info.get_per_page()))
                    if info.get_count() is not None:
                        print("User Info Count: " + str(info.get_count()))
                    if info.get_page() is not None:
                        print("User Info Page: " + str(info.get_page()))
                    if info.get_more_records() is not None:
                        print("User Info MoreRecords: " + str(info.get_more_records()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


GetUsersOfUserType.initialize()
GetUsersOfUserType.get_users_of_usertype(portal_name="PortalsAPItest100", user_type_id=440248001304019)
