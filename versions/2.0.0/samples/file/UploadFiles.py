from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.files import FilesOperations, UploadFilesParam, BodyWrapper, ActionWrapper, \
    SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.util import StreamWrapper


class UploadFiles:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def upload_files():
        """
        This method is used to upload files and print the response.
        """
        file_operations = FilesOperations()
        param_instance = ParameterMap()
        request = BodyWrapper()
        """
        StreamWrapper can be initialized in any of the following ways
        * param 1 -> fileName 
        * param 2 -> Read Stream.
        """
        # stream_wrapper = StreamWrapper(stream=open(absolute_file_path, 'rb'))
        """
        * param 1 -> fileName
        * param 2 -> Read Stream
        * param 3 -> Absolute File Path of the file to be attached
        """
        stream_wrapper1 = StreamWrapper(
            file_path='users/file/download.png')
        stream_wrapper2 = StreamWrapper(
            file_path='/Users/file/download.png')
        stream_wrapper3 = StreamWrapper(
            file_path='/Users/file/download.png')
        request.set_file([stream_wrapper1, stream_wrapper2, stream_wrapper3])
        # Call upload_files method that takes BodyWrapper instance and ParameterMap instance as parameter.
        response = file_operations.upload_files(request, param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_data()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
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
                            print("Message: " + action_response.get_message())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


UploadFiles.initialize()
UploadFiles.upload_files()