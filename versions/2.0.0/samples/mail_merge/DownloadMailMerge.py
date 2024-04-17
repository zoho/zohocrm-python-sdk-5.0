import os

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.files.file_body_wrapper import FileBodyWrapper
from zohocrmsdk.src.com.zoho.crm.api.mail_merge import MailMergeOperations, APIException, \
    MailMergeTemplate, DownloadMailMergeWrapper, DownloadMailMerge
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class DownloadMailMerge1(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def download_mail_merge(module_api_name, id, destination_folder):
        mail_merge_operations = MailMergeOperations(module_api_name, id)
        request = DownloadMailMergeWrapper()
        download_mail_merge = []
        mail_merge = DownloadMailMerge()
        mail_merge_template = MailMergeTemplate()
        mail_merge_template.set_name("Test")
        mail_merge.set_mail_merge_template(mail_merge_template)
        mail_merge.set_output_format(Choice("pdf"))
        mail_merge.set_file_name("SDK Name")
        mail_merge.set_password("TestSDK")
        download_mail_merge.append(mail_merge)
        request.set_download_mail_merge(download_mail_merge)
        response = mail_merge_operations.download_mail_merge(request)
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


DownloadMailMerge1.initialize()
id = "3477001"
module = "Leads"
destination_folder = "/Users/file"
DownloadMailMerge1.download_mail_merge(module, id, destination_folder)
