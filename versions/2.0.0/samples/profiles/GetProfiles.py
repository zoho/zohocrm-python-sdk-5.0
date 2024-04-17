from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.profiles import ProfilesOperations, ProfileWrapper, APIException


class GetProfiles:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_profiles():

        """
        This method is used to retrieve the profiles data through an API request and print the response.
        """
        profiles_operations = ProfilesOperations()
        response = profiles_operations.get_profiles()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ProfileWrapper):
                    profiles_list = response_object.get_profiles()
                    for profile in profiles_list:
                        print("Profile DisplayLabel: " + profile.get_display_label())
                        if profile.get_created_time() is not None:
                            print("Profile CreatedTime: " + str(profile.get_created_time()))
                        if profile.get_modified_time() is not None:
                            print("Profile ModifiedTime: " + str(profile.get_modified_time()))
                        print("Profile Name: " + profile.get_name())
                        modified_by = profile.get_modified_by()
                        if modified_by is not None:
                            print("Profile Modified By - Name: " + modified_by.get_name())
                            print("Profile Modified By - ID: " + str(modified_by.get_id()))
                        default_view = profile.get_defaultview()
                        if default_view is not None:
                            print("Profile Default view - Name: " + default_view.get_name())
                            print("Profile Default view - ID: " + str(default_view.get_id()))
                            print("Profile Default view - Type: " + str(default_view.get_type()))
                        print("Profile custom: " + str(profile.get_custom()))
                        print("Profile delete: " + str(profile.get_delete()))
                        print("Profile permission_type: " + str(profile.get_permission_type()))
                        print("Profile Description: " + str(profile.get_description()))
                        print("Profile ID: " + str(profile.get_id()))
                        created_by = profile.get_created_by()
                        if created_by is not None:
                            print("Profile Created By - Name: " + created_by.get_name())
                            print("Profile Created By - ID: " + str(created_by.get_id()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


GetProfiles.initialize()
GetProfiles.get_profiles()