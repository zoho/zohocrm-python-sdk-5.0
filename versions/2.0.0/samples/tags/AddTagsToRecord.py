from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.tags import TagsOperations, NewTagRequestWrapper, Tag, RecordActionWrapper, \
    SuccessResponse, RecordSuccessResponse, APIException


class AddTagsToRecord:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def add_tags_to_record(module_api_name, record_id):
        """
        This method is used to add tags to a specific record and print the response.
        :param module_api_name: The API Name of the module to add tag.
        :param record_id: The ID of the record to add tag
        :param tag_names: The list of tag names
        """
        """
        example
        module_api_name = "Leads"
        record_id = 3409643002157023
        tag_names = ["addtag1,addtag12"]
        """
        tags_operations = TagsOperations()
        request = NewTagRequestWrapper()
        tag_list = []
        tag1 = Tag()
        tag1.set_name("tagNam3e3e12345")
        tag1.set_id(440248001390027)
        tag_list.append(tag1)
        request.set_tags(tag_list)
        # request.set_over_write(True)
        param_instance = ParameterMap()
        response = tags_operations.add_tags(record_id, module_api_name, request, param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, RecordActionWrapper):
                    action_response_list = response_object.get_data()
                    for action_response in action_response_list:
                        if isinstance(action_response, RecordSuccessResponse):
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
                            print("Message: " + action_response.get_message().get_value())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


module_api_name = "Leads"
record_id = 440248001483007
AddTagsToRecord.initialize()
AddTagsToRecord.add_tags_to_record(module_api_name, record_id)
