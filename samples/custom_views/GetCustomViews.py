from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.api.authenticator.store import DBStore
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap, UserSignature
from zohocrmsdk.src.com.zoho.crm.api.custom_views import CustomViewsOperations, GetCustomViewsParam, BodyWrapper, \
    APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class GetCustomViews(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_custom_views(module_api_name):
        """
        This method is used to get the custom views data of a particular module.
        Specify the module name in your API request whose custom view data you want to retrieve.
        :param module_api_name: the API name of the required module.
        """
        """
        example
        module_api_name = "Leads";
        """
        custom_views_operations = CustomViewsOperations()
        param_instance = ParameterMap()
        # Possible parameters of Get CustomViews operation
        param_instance.add(GetCustomViewsParam.module, module_api_name)
        # Call get_custom_views method that takes ParameterMap instance as parameter
        response = custom_views_operations.get_custom_views(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, BodyWrapper):
                    custom_views_list = response_object.get_custom_views()
                    for custom_view in custom_views_list:
                        print('CustomView ID: ' + str(custom_view.get_id()))
                        print('CustomView Name: ' + str(custom_view.get_name()))
                        created_by = custom_view.get_created_by()
                        if created_by is not None:
                            print("CustomView Created By - Name: " + created_by.get_name())
                            print("CustomView Created By - ID: " + str(created_by.get_id()))
                        if custom_view.get_modified_time() is not None:
                            print("Record ModifiedTime: " + str(custom_view.get_modified_time()))
                            modified_by = custom_view.get_modified_by()
                            if modified_by is not None:
                                print("Record Modified By - Name: " + modified_by.get_name())
                                print("Record Modified By - ID: " + str(modified_by.get_id()))
                        print('CustomView System Name: ' + str(custom_view.get_system_name()))
                        print('CustomView Category: ' + str(custom_view.get_category()))
                        print('CustomView __last_accessed_time: ' + str(custom_view.get_last_accessed_time()))
                        print('CustomView Display Value: ' + str(custom_view.get_display_value()))
                        print('CustomView AccessType: ' + str(custom_view.get_access_type()))
                        print('CustomView Is default: ' + str(custom_view.get_default()))
                        print('CustomView Is System Defined: ' + str(custom_view.get_system_defined()))
                        if custom_view.get_favorite() is not None:
                            print('CustomView Favorite: ' + str(custom_view.get_favorite()))
                    info = response_object.get_info()
                    if info is not None:
                        print("CustomView Info")
                        if info.get_per_page() is not None:
                            print('PerPage: ' + str(info.get_per_page()))
                        if info.get_page() is not None:
                            print('Page: ' + str(info.get_page()))
                        if info.get_more_records() is not None:
                            print('MoreRecords: ' + str(info.get_more_records()))
                        if info.get_default() is not None:
                            print('Default: ' + str(info.get_default()))
                        if info.get_count() is not None:
                            print('Count: ' + str(info.get_count()))
                        translation = info.get_translation()
                        if translation is not None:
                            print("Translation details")
                            print('PublicViews: ' + translation.get_public_views())
                            print('OtherUsersViews: ' + translation.get_other_users_views())
                            print('SharedWithMe: ' + translation.get_shared_with_me())
                            print('CreatedByMe: ' + translation.get_created_by_me())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


GetCustomViews.initialize()
GetCustomViews.get_custom_views(module_api_name="Leads")