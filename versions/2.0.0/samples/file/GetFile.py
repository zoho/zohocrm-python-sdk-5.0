import os
from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.files import FilesOperations, GetFileParam, FileBodyWrapper, APIException


class GetFile:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_file(id, destination_folder):
        """
        This method is used to download the file with ID and write in the destinationFolder
        :param id: The ID of the uploaded File.
        :param destination_folder: The absolute path of the destination folder to store the File
        """
        """
        example
        id = "ae9c7cefa418aec1d6a5cc2d9ab35c3231aae3bfeef7d5e00a54b7563c0dd42b";
        destination_folder = "/Users/user_name/Desktop"
        """
        file_operations = FilesOperations()
        param_instance = ParameterMap()
        # Add the id to ParameterMap instance
        param_instance.add(GetFileParam.id, id)
        # Call get_file method that takes ParameterMap instance as parameter
        response = file_operations.get_file(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, FileBodyWrapper):
                    stream_wrapper = response_object.get_file()
                    # Construct the file name by joining the destinationFolder and the name from StreamWrapper instance
                    file_name = os.path.join(destination_folder, stream_wrapper.get_name())
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


id = "c6085fae06cbd7b75006b08827c04e44e44c56ea3f571bfea62fe"
destination_folder = "/users/sample/file"
GetFile.initialize()
GetFile.get_file(id, destination_folder)