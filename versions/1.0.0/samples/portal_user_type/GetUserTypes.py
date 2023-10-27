from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.portal_user_type import PortalUserTypeOperations, ResponseWrapper, APIException


class GetUserTypes(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_user_types(portal_name):
        user_type_operations = PortalUserTypeOperations(portal_name)
        param_instance = ParameterMap()
        response = user_type_operations.get_user_types(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                response_wrapper = response_object
                user_type = response_wrapper.get_user_type()
                for user_type1 in user_type:
                    print("UserType CreatedTime: " + str(user_type1.get_created_time()))

                    print("UserType Default: " + str(user_type1.get_default()))

                    print("UserType ModifiedTime: " + str(user_type1.get_modified_time()))

                    personalityModule = user_type1.get_personality_module()
                    if personalityModule is not None:
                        print("UserType PersonalityModule ID: " + str(personalityModule.get_id()))
                        print("UserType PersonalityModule APIName: " + personalityModule.get_api_name())
                        print("UserType PersonalityModule PluralLabel: " + personalityModule.get_plural_label())
                        print("UserType Name: " + user_type1.get_name())
                    modifiedBy = user_type1.get_modified_by()
                    if modifiedBy is not None:
                        print("UserType ModifiedBy User-ID: " + str(modifiedBy.get_id()))
                        print("UserType ModifiedBy User-Name: " + modifiedBy.get_name())
                    print("UserType Active: " + str(user_type1.get_active()))
                    print("UserType Id: " + str(user_type1.get_id()))
                    createdBy = user_type1.get_created_by()
                    if createdBy is not None:
                        print("UserType CreatedBy User-ID: " + str(createdBy.get_id()))
                        print("UserType CreatedBy User-Name: " + createdBy.get_name())
                    print("UserType NoOfUsers: " + str(user_type1.get_no_of_users()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


portal_name = "PortalsAPITest101"
GetUserTypes.initialize()
GetUserTypes.get_user_types(portal_name)
