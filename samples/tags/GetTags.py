from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.tags import TagsOperations, GetTagsParam, ResponseWrapper, APIException


class GetTags:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_tags(module_api_name):
        """
        This method is used to get all the tags in a module
        :param module_api_name: The API Name of the module to get tags.
        """
        """
        example
        module_api_name = "Leads"
        """
        tags_operations = TagsOperations()
        param_instance = ParameterMap()
        # Possible parameters of Get Tags operation
        param_instance.add(GetTagsParam.module, module_api_name)
        # param_instance.add(GetTagsParam.my_tags, 'true')
        # Call get_tags method that takes ParameterMap instance as parameter
        response = tags_operations.get_tags(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    tags_list = response_object.get_tags()
                    for tag in tags_list:
                        print("Tag CreatedTime: " + str(tag.get_created_time()))
                        if tag.get_modified_time() is not None:
                            print("Tag ModifiedTime: " + str(tag.get_modified_time()))
                        print("Tag ColorCode: " + str(tag.get_color_code()))
                        print("Tag Name: " + tag.get_name())
                        modified_by = tag.get_modified_by()
                        if modified_by is not None:
                            print("Tag Modified By - Name: " + modified_by.get_name())
                            print("Tag Modified By - ID: " + str(modified_by.get_id()))
                        print("Tag ID: " + str(tag.get_id()))
                        created_by = tag.get_created_by()
                        if created_by is not None:
                            print("Tag Created By - Name: " + created_by.get_name())
                            print("Tag Created By - ID: " + str(created_by.get_id()))
                    info = response_object.get_info()
                    if info is not None:
                        if info.get_count() is not None:
                            print("Tag Info Count: " + str(info.get_count()))
                        if info.get_allowed_count() is not None:
                            print("Tag Info AllowedCount: " + str(info.get_allowed_count()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


GetTags.initialize()
GetTags.get_tags(module_api_name="Leads")
