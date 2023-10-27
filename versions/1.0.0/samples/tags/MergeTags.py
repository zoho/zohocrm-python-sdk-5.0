from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.tags import TagsOperations, MergeWrapper, ConflictWrapper, ActionWrapper, \
    SuccessResponse, APIException


class MergeTags:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def merge_tags(tag_id, conflict_id):
        """
        This method is used to merge tags and put all the records under the two tags into a single tag and print the response.
        :param tag_id: The ID of the tag
        :param conflict_id: The ID of the conflict tag.
        """
        """
        example
        tag_id = 34096430661047
        conflict_id = '34096430661026'
        """
        tags_operations = TagsOperations()
        request = MergeWrapper()
        # List to hold ConflictWrapper instances
        tag_list = []
        conflict_wrapper = ConflictWrapper()
        conflict_wrapper.set_conflict_id(conflict_id)
        # Add the instance to list
        tag_list.append(conflict_wrapper)
        request.set_tags(tag_list)
        # Call merge_tags method that takes MergeWrapper instance and tag_id as parameter
        response = tags_operations.merge_tags(tag_id, request)
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


MergeTags.initialize()
MergeTags.merge_tags(tag_id=440248001390027, conflict_id="440248001504017")