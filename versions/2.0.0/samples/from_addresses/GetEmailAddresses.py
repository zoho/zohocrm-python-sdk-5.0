from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.from_addresses import FromAddressesOperations, ResponseWrapper, APIException


class GetEmailAddresses(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_email_addresses():
        send_mail_operations = FromAddressesOperations()
        response = send_mail_operations.get_from_addresses()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                response_wrapper = response_object
                user_addresses = response_wrapper.get_from_addresses()
                for user_address in user_addresses:
                    print("UserAdress Email: " + user_address.get_email())
                    print("UserAdress Type: " + user_address.get_type())
                    print("UserAdress UserName: " + user_address.get_user_name())
                    print("UserAdress Default: " + str(user_address.get_default()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


GetEmailAddresses.initialize()
GetEmailAddresses.get_email_addresses()