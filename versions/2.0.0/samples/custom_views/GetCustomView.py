from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.api.authenticator.store import DBStore
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap, UserSignature
from zohocrmsdk.src.com.zoho.crm.api.custom_views import CustomViewsOperations, BodyWrapper, APIException, \
    GetCustomViewParam
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class GetCustomView(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_custom_view(module_api_name, custom_view_id):
        """
        This method is used to get the data of any specific custom view of the module with ID
        :param module_api_name: The API name of the required module.
        :param custom_view_id: ID of the CustomView to be obtained
        :return:
        """
        """
        example
        module_api_name = "Leads"
        custom_view_id = 3409643002955026n
        """
        custom_views_operations = CustomViewsOperations()
        param_instance = ParameterMap()
        param_instance.add(GetCustomViewParam.module, module_api_name)
        # Call get_custom_view method that takes custom_view_id as parameter
        response = custom_views_operations.get_custom_view(custom_view_id, param_instance)
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
                            print("CustomView Created By - ID: ")
                            print(created_by.get_id())
                        if custom_view.get_modified_time() is not None:
                            print("Record ModifiedTime: " + str(custom_view.get_modified_time()))
                            modified_by = custom_view.get_modified_by()
                            if modified_by is not None:
                                print("Record Modified By - Name: " + modified_by.get_name())
                                print("Record Modified By - ID: " + str(modified_by.get_id()))
                        print('CustomView AccessType: ' + str(custom_view.get_access_type()))
                        print('CustomView Is default: ' + str(custom_view.get_default()))
                        print('CustomView Is System Defined: ' + str(custom_view.get_system_defined()))
                        print('CustomView System Name: ' + str(custom_view.get_system_name()))
                        print('CustomView Category: ' + str(custom_view.get_category()))
                        print('CustomView Display Value: ' + str(custom_view.get_display_value()))
                        shared_to_details = custom_view.get_shared_to()
                        if shared_to_details is not None:
                            for shared_to_detail in shared_to_details:
                                print("SharedDetails Name: " + shared_to_detail.get_name())
                                print("SharedDetails ID: " + shared_to_detail.get_id())
                                print("SharedDetails Type: " + shared_to_detail.get_type())
                                print("SharedDetails Subordinates: " + str(shared_to_detail.get_subordinates()))
                        criteria = custom_view.get_criteria()
                        if criteria is not None:
                            GetCustomView.print_criteria(criteria)
                        print('CustomView Is default: ' + str(custom_view.get_default()))
                        print('CustomView SortBy: ' + str(custom_view.get_sort_by()))
                        if custom_view.get_sort_order() is not None:
                            print('CustomView SortOrder: ' + str(custom_view.get_sort_order()))
                        print('CustomView Is System Defined: ' + str(custom_view.get_system_defined()))
                        if custom_view.get_favorite() is not None:
                            print('CustomView Favorite: ' + str(custom_view.get_favorite()))
                        fields = custom_view.get_fields()
                        if fields is not None:
                            print('Fields')
                            for field in fields:
                                print(field)
                    info = response_object.get_info()
                    if info is not None:
                        print("CustomView Info")
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
    @staticmethod
    def print_criteria(criteria):
        if criteria.get_comparator() is not None:
            print('CustomView Criteria Comparator: ' + criteria.get_comparator())
        if criteria.get_field() is not None:
            print('CustomView Criteria Field: ' + criteria.get_field().get_api_name())
        if criteria.get_value() is not None:
            print('CustomView Criteria Value: ' + str(criteria.get_value()))
        criteria_group = criteria.get_group()
        if criteria_group is not None:
            for each_criteria in criteria_group:
                GetCustomView.print_criteria(each_criteria)
        if criteria.get_group_operator() is not None:
            print('CustomView Criteria Group Operator: ' + criteria.get_group_operator())


module = "Leads"
id = 440248001437022
GetCustomView.initialize()
GetCustomView.get_custom_view(module, id)