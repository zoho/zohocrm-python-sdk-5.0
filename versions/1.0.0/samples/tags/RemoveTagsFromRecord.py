from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.tags import TagsOperations, ExistingTagRequestWrapper, ExistingTag, \
    RecordActionWrapper, SuccessResponse, APIException, RecordSuccessResponse


class RemoveTagsFromRecord:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def remove_tags_from_record(module_api_name, record_id):
        """
        This method is used to delete the tags associated with a specific record and print the response.
        :param module_api_name: The API Name of the module to remove tags
        :param record_id: The ID of the record to delete tags
        :param tag_names: The list of the tag names to be removed.
        :return:
        """
        """
        example
        module_api_name = "Leads"
        record_id = 3409643002157023
        """
        tags_operations = TagsOperations()
        request = ExistingTagRequestWrapper()
        tag_list = []
        tag1 = ExistingTag()
        tag1.set_name("tagNam3e3e12345")
        tag_list.append(tag1)
        request.set_tags(tag_list)
        response = tags_operations.remove_tags(record_id, module_api_name, request)
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


RemoveTagsFromRecord.initialize()
RemoveTagsFromRecord.remove_tags_from_record(module_api_name="Leads", record_id=440248001483007)