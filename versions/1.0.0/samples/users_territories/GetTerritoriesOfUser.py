from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.users_territories import UsersTerritoriesOperations, ResponseWrapper, APIException


class GetTerritoriesOfUser(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_territories_of_user(user_id):
        user_territories_operartions = UsersTerritoriesOperations()
        response = user_territories_operartions.get_territories_of_user(user_id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                users_territory = response_object.get_territories()
                for territory in users_territory:
                    print("User Territory Id: " + str(territory.get_id()))
                    manager = territory.get_manager()
                    if manager is not None:
                        print("User Territory Manager Name: " + str(manager.get_name()))
                        print("User Territory Manager ID: " + str(manager.get_id()))
                    reportingTo = territory.get_reporting_to()
                    if reportingTo is not None:
                        print("User Territory ReportingTo Name: " + reportingTo.get_name())
                        print("User Territory ReportingTo ID: " + str(reportingTo.get_id()))
                    print("User Territory Name: " + territory.get_name())
                info = response_object.get_info()
                if info is not None:
                    if info.get_per_page() is not None:
                        print("User Info PerPage: " + str(info.get_per_page()))
                    if info.get_count() is not None:
                        print("User Info Count: " + str(info.get_count()))
                    if info.get_page() is not None:
                        print("User Info Page: " + str(info.get_page()))
                    if info.get_more_records() is not None:
                        print("User Info MoreRecords: " + str(info.get_more_records()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


user_id = 440248001502002
GetTerritoriesOfUser.initialize()
GetTerritoriesOfUser.get_territories_of_user(user_id)