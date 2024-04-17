from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.territory_users import TerritoryUsersOperations, ResponseWrapper, APIException


class GetTerritoryUsers(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_territory_users(territory):
        territory_users_operations = TerritoryUsersOperations()
        response = territory_users_operations.get_territory_users(territory)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                users = response_object.get_users()
                if users is not None:
                    for user in users:
                        print("Territory user id : " + str(user.get_id()))
                info = response_object.get_info()
                if info is not None:
                    if info.get_per_page() is not None:
                        print("Territory Info PerPage : " + str(info.get_per_page()))
                    if info.get_count() is not None:
                        print("Territory Info Count: " + str(info.get_count()))
                    if info.get_page() is not None:
                        print("Territory info Page: " + str(info.get_page()))
                    if info.get_more_records() is not None:
                        print("Territroy info morerecords : " + str(info.get_more_records()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


GetTerritoryUsers.initialize()
GetTerritoryUsers.get_territory_users(territory=440248001390040)