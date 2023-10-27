from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.attachments import AttachmentsOperations, ActionWrapper, SuccessResponse, \
    APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class DeleteAttachment:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)
        
    @staticmethod
    def delete_attachment(module_api_name, record_id, attachment_id):
        """
        This method is used to delete an attachment of a single record with ID and attachment ID and print the response
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to delete attachment
        :param attachment_id: The ID of the attachment to be deleted
        """
        """
        example
        module_api_name = "Leads";
        record_id = 3409643002267003
        attachment_id = 3409643002267024
        """
        attachments_operations = AttachmentsOperations()
        # Call delete_attachment method that takes attachment_id as parameter
        response = attachments_operations.delete_attachment(record_id, module_api_name, attachment_id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_data()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message())
                        elif isinstance(action_response, APIException):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


module = "Leads"
record_id = 4402480774074
attachment_id = 334234123123213
DeleteAttachment.initialize()
DeleteAttachment.delete_attachment(module, record_id, attachment_id)
