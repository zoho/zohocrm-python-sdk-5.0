from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.backup import BackupOperations, UrlsWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class GetUrls(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_urls():
        backup_operations = BackupOperations()
        response = backup_operations.get_urls()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, UrlsWrapper):
                responseWrapper = response_object
                urls = responseWrapper.get_urls()
                if urls is not None:
                    data_links = urls.get_data_links()
                    if data_links is not None:
                        print("Urls DataLinks: ")
                        for url in data_links:
                            print(url)
                    attachment_links = urls.get_attachments_links()
                    if attachment_links is not None:
                        print("Urls AttachmentLinks : ")
                        for url in attachment_links:
                            print(url)
                    print("Urls ExpiryDate:" + urls.get_expiry_date())
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


GetUrls.initialize()
GetUrls.get_urls()
