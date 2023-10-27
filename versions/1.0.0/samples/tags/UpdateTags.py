from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.tags import TagsOperations, UpdateTagsParam, BodyWrapper, Tag, ActionWrapper, \
    SuccessResponse, APIException


class UpdateTags:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_tags(module_api_name):
        """
        This method is used to update multiple tags simultaneously and print the response.
        :param module_api_name: The API Name of the module to update tags
        """
        """
        example
        module_api_name = "Leads"
        """
        tags_operations = TagsOperations()
        param_instance = ParameterMap()
        # Possible parameters of Update Tags operation
        param_instance.add(UpdateTagsParam.module, module_api_name)
        request = BodyWrapper()
        # List to hold Tag instances
        tags_list = []
        tag_1 = Tag()
        tag_1.set_id(3477061012712002)
        tag_1.set_name("edited-tagname")
        # Add the instance to list
        tags_list.append(tag_1)
        tag_2 = Tag()
        tag_2.set_id(3477061012712001)
        tag_2.set_name("edited-tagname")
        # Add the instance to list
        tags_list.append(tag_2)
        request.set_tags(tags_list)
        # Call update_tags method that takes BodyWrapper instance and ParameterMap instance as parameter
        response = tags_operations.update_tags(request, param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_tags()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message().get_value())
                        elif isinstance(action_response, APIException):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message().get_value())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


UpdateTags.initialize()
UpdateTags.update_tags(module_api_name="Leads")