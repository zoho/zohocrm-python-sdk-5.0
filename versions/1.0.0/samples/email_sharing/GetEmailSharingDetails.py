from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.email_sharing import EmailSharingOperations, ResponseWrapper, APIException


class GetEmailSharingDetails(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_email_sharing_details(record_id, module):
        email_sharing_operations = EmailSharingOperations(record_id, module)
        response = email_sharing_operations.get_email_sharing_details()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                response_wrapper = response_object
                email_sharing_details = response_wrapper.get_emailssharingdetails()
                if email_sharing_details is not None:
                    for get_email_sharing in email_sharing_details:
                        print("Email Sharing Details : ")
                        share_from_users = get_email_sharing.get_share_from_users()
                        if share_from_users is not None:
                            print("ShareFromUsers: ")
                            for share_from_user in share_from_users:
                                print("id : " + share_from_user.get_id())
                                print("name : " + share_from_user.get_name())
                                print("type : " + share_from_user.get_type())
                        available_types = get_email_sharing.get_available_types()
                        if available_types is not None:
                            print("Available Types: ")
                            for available_type in available_types:
                                print(available_type)
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
GetEmailSharingDetails.initialize()
GetEmailSharingDetails.get_email_sharing_details(record_id, module)