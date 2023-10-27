from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.portal_user_type import PortalUserTypeOperations, ResponseWrapper, APIException


class GetUserType(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_user_type(portal_name, user_type_id):
        user_type_operations = PortalUserTypeOperations()
        response = user_type_operations.get_user_type(user_type_id)
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
                    print("UserType Default: " + user_type1.getDefault())
                    personalityModule = user_type1.getPersonalityModule()
                    if personalityModule is not None:
                        print("UserType PersonalityModule ID: " + personalityModule.get_id())
                        print("UserType PersonalityModule APIName: " + personalityModule.get_api_name())
                        print("UserType PersonalityModule PluralLabel: " + personalityModule.get_plural_label())
                    print("UserType Name: " + user_type1.get_name())
                    print("UserType Active: " + user_type1.get_active())
                    print("UserType Id: " + user_type1.get_id())
                    print("UserType NoOfUsers: " + user_type1.get_no_of_users())
                    modules = user_type1.get_modules()
                    if modules is not None:
                        for module in modules:
                            print("UserType Modules PluralLabel: " + module.get_plural_label())
                            print("UserType Modules SharedType: " + module.get_shared_type().get_value())
                            print("UserType Modules APIName: " + module.get_api_name())
                            permissions = module.get_permissions()
                            if permissions is not None:
                                print("UserType Modules Permissions View: " + permissions.get_view())
                                print("UserType Modules Permissions Edit: " + permissions.get_edit())
                                print("UserType Modules Permissions EditSharedRecords: " + permissions.get_edit_shared_records())
                                print("UserType Modules Permissions Create: " + permissions.get_create())
                                print("UserType Modules Permissions Delete: " + permissions.get_delete())
                            print("UserType Modules Id: " + module.get_id())
                            filters = module.get_filters()
                            if filters is not None:
                                for filter1 in filters:
                                    print("UserType Modules Filters APIName: " + filter1.get_api_name())
                                    print("UserType Modules Filters DisplayLabel: " + filter1.get_display_label())
                                    print("UserType Modules Filters Id: " + filter1.get_id())
                            fields = module.get_fields()
                            if fields is not None:
                                for field in fields:
                                    print("UserType Modules Fields APIName: " + field.get_api_name())
                                    print("UserType Modules Fields ReadOnly: " + field.get_read_only())
                                    print("UserType Modules Fields Id: " + field.get_id())
                            layouts = module.get_layouts()
                            if layouts is not None:
                                for layout in layouts:
                                    print("UserType Modules Layouts Name: " + layout.get_name())
                                    print("UserType Modules Layouts DisplayLabel: " + layout.get_display_label())
                                    print("UserType Modules Layouts Id: " + layout.get_id())
                            views = module.get_views()
                            if views is not None:
                                print("UserType Modules Views DisplayLabel: " + views.get_display_label())
                                print("UserType Modules Views Name: " + views.get_name())
                                print("UserType Modules Views Id: " + views.get_id())
                                print("UserType Modules Permissions Type: " + views.get_type())
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


portal_name = "PortalsAPItest100"
user_type_id = "440248001304019"
GetUserType.initialize()
GetUserType.get_user_type(portal_name, user_type_id)