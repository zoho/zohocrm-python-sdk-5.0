import os

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.download_attachments import DownloadAttachmentsOperations, \
    GetDownloadAttachmentsDetailsParam, APIException, FileBodyWrapper


class GetDownloadAttachmentsDetails(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_download_attachment_details(module, record_id, user_id, message_id, destination_folder):
        download_attachments_operations = DownloadAttachmentsOperations()
        param_instance = ParameterMap()
        param_instance.add(GetDownloadAttachmentsDetailsParam.message_id, message_id)
        param_instance.add(GetDownloadAttachmentsDetailsParam.user_id, user_id)
        response = download_attachments_operations.get_download_attachments_details(record_id, module, param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, FileBodyWrapper):
                    stream_wrapper = response_object.get_file()
                    file_name = os.path.join(
                        destination_folder, stream_wrapper.get_name())
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
                    print("Message: " + response_object.get_message().get_value())


module = "Leads"
record_id = 4402480774074
user_id = 4402480254001
message_id = "c6085fae06cbd7b75001d7e5b0e37dc775a2c7158404f"
destination_folder = "/users/sample/file"
GetDownloadAttachmentsDetails.initialize()
GetDownloadAttachmentsDetails.get_download_attachment_details(module, record_id, user_id, message_id, destination_folder)