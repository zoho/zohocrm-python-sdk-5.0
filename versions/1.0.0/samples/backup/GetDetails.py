from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.backup import BackupOperations, BodyWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class GetDetails(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_details():
        backup_operations = BackupOperations()
        response = backup_operations.get_details()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, BodyWrapper):
                responseWrapper = response_object
                backup = responseWrapper.get_backup()
                if backup is not None:
                    print("Backup Rrule: " + backup.get_rrule())
                    print("Backup Id: " + str(backup.get_id()))
                    print("Backup StartDate: " + backup.get_start_date())
                    print("Backup ScheduledDate: " + backup.get_scheduled_date())
                    print("Backup Status: " + backup.get_status())
                    requester = backup.get_requester()
                    if requester is not None:
                        print("Backup Requester Id: " + str(requester.get_id()))
                        print("Backup Requester Name: " + requester.get_name())
                        print("Backup Requester Zuid: " + str(requester.get_zuid()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


GetDetails.initialize()
GetDetails.get_details()