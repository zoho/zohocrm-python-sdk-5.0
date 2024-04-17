from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.users_transfer_delete import UsersTransferDeleteOperations, GetStatusParam, \
    ResponseWrapper, APIException


class GetStatus(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_status():
        user_transfer_delete_operations = UsersTransferDeleteOperations()
        param_instance = ParameterMap()
        param_instance.add(GetStatusParam.job_id, 440248001498022)
        response = user_transfer_delete_operations.get_status(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                transfer_and_delete = response_object.get_transfer_and_delete()
                if transfer_and_delete is not None:
                    for status in transfer_and_delete:
                        print("TransferAndDelete status: " + status.get_status())
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message().get_value())


GetStatus.initialize()
GetStatus.get_status()