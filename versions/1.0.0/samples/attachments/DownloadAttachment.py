import os
from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.attachments import AttachmentsOperations, FileBodyWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class DownloadAttachment(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)
        
    @staticmethod
    def download_attachment(module_api_name, record_id, attachment_id, destination_folder):
        """
        This method is used to download an attachment of a single record of a module with ID and attachment ID and write the file in the specified destination.
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to download attachment
        :param attachment_id: The ID of the attachment to be downloaded
        :param destination_folder: The absolute path of the destination folder to store the attachment
        """
        """
        example
        module_api_name = "Leads";
        record_id = 3409643002267003
        attachment_id = 3409643002267024
        destination_folder = "/Users/user-name/Desktop";
        """
        attachments_operations = AttachmentsOperations()
        # Call download_attachment method that takes attachment_id as parameters
        response = attachments_operations.get_attachment(attachment_id, record_id, module_api_name,)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code()
                                      == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, FileBodyWrapper):
                    stream_wrapper = response_object.get_file()
                    # Construct the file name by joining the destinationFolder and the name from StreamWrapper instance
                    file_name = os.path.join(
                        destination_folder, stream_wrapper.get_name())
                    # Open the destination file where the file needs to be written in 'wb' mode
                    with open(file_name, 'wb') as f:
                        for chunk in stream_wrapper.get_stream():
                            f.write(chunk)
                        f.close()
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


module= "Leads"
record_id = 4402480774074
attachment_id = 440248001437004
destination_folder = "/users/sample/file"
DownloadAttachment.initialize()
DownloadAttachment.download_attachment(module, record_id, attachment_id, destination_folder)