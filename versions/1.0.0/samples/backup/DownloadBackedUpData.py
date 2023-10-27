import os

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.backup import BackupOperations, FileBodyWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class DownloadBackedUpData(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def downloadBackedUpData(download_url, destination_folder):
        backup_operations = BackupOperations()
        response = backup_operations.download_backed_up_data(download_url)
        if response is not None:
            print("Status code : " + str(response.get_status_code()))
            if response.get_status_code() == 204:
                print("No Content")
                return
            responseHandler = response.get_object()
            if isinstance(responseHandler, FileBodyWrapper):
                stream_wrapper = responseHandler.get_file()
                file_name = os.path.join(
                    destination_folder, stream_wrapper.get_name())
                with open(file_name, 'wb') as f:
                    for chunk in stream_wrapper.get_stream():
                        f.write(chunk)
                    f.close()
            elif isinstance(responseHandler, APIException):
                print("Status: " + responseHandler.get_status().get_value())
                print("Code: " + responseHandler.get_code().get_value())
                print("Details")
                details = responseHandler.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + responseHandler.get_message())


download_url = "https://download-accl.zoho.com/v2/crm/123456789/backup/36523003/Data_001.zip"
destination_folder = "/Users/zohocrm-java-sdk-sample/file"
DownloadBackedUpData.initialize()
DownloadBackedUpData.downloadBackedUpData(download_url, destination_folder)
