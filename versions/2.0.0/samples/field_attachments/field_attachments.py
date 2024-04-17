import os

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.field_attachments import FieldAttachmentsOperations, FileBodyWrapper, APIException


class FieldAttachments(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_field_attachments(module_api_name, record_id, attachment_id, destination_folder):
        """
        This method is used to get a field_attachments' details with ID and print the response.

        """
        # Get instance of FieldAttachmentsOperations Class
        # destination_folder = "/Users/test/Desktop"
        field_attachments_operations = FieldAttachmentsOperations(module_api_name, record_id, attachment_id)
        # Possible parameters for Get field_attachments Operation
        response = field_attachments_operations.get_field_attachments()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, FileBodyWrapper):
                    stream_wrapper = response_object.get_file()
                    file_name = os.path.join(destination_folder, stream_wrapper.get_name())
                    with open(file_name, 'wb') as f:
                        for chunk in stream_wrapper.get_stream():
                            f.write(chunk)
                        f.close()
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    if details is not None:
                        if details is not None:
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


module_api_name = "Leads"
record_id = 4402480774074
attachment_id = 440248001529117
destination_folder = "/users/sample/file"
FieldAttachments.initialize()
FieldAttachments.get_field_attachments(module_api_name, record_id, attachment_id, destination_folder)
