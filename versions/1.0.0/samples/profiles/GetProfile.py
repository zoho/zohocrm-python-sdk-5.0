from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.profiles import ProfilesOperations, ProfileWrapper, APIException


class GetProfile:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_profile(profile_id):
        """
        This method is used to get the details of any specific profile with ID.
        :param profile_id: The ID of the Profile to be obtained
        """
        """
        example
        profile_id = 34096430022802
        """
        profiles_operations = ProfilesOperations()
        response = profiles_operations.get_profile(profile_id)
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
                        permissions_details = profile.get_permissions_details()
                        if permissions_details is not None:
                            for permissions_detail in permissions_details:
                                print("Profile PermissionDetail DisplayLabel: " + str(
                                    permissions_detail.get_display_label()))
                                print("Profile PermissionDetail Module: " + str(permissions_detail.get_module()))
                                print("Profile PermissionDetail Name: " + str(permissions_detail.get_name()))
                                print("Profile PermissionDetail ID: " + str(permissions_detail.get_id()))
                                print("Profile PermissionDetail Enabled: " + str(permissions_detail.get_enabled()))
                        sections = profile.get_sections()
                        if sections is not None:
                            for section in sections:
                                print("Profile Section Name: " + section.get_name())
                                categories = section.get_categories()
                                if categories is not None:
                                    for category in categories:
                                        print("Profile Section Category DisplayLabel: " + str(
                                            category.get_display_label()))
                                        category_permissions_details = category.get_permissions_details()
                                        if category_permissions_details is not None:
                                            for permissions_detail_id in category_permissions_details:
                                                print(
                                                    "Profile Section Category permissionsDetailID: " + permissions_detail_id)
                                        print("Profile Section Category Name: " + str(category.get_name()))
                        if profile.get_delete() is not None:
                            print("Profile Delete: " + str(profile.get_delete()))
                        if profile.get_default() is not None:
                            print("Profile Default: " + str(profile.get_default()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


profile_id = 4402480031157
GetProfile.initialize()
GetProfile.get_profile(profile_id)