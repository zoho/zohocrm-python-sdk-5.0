from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.territories import TerritoriesOperations, AssociatedUsersCountWrapper, APIException


class AssociatedUserCount(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_associated_user_count():
        territories_operations = TerritoriesOperations()
        response = territories_operations.get_associated_user_count()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, AssociatedUsersCountWrapper):
                response_wrapper = response_object
                territory_list = response_wrapper.get_associated_users_count()
                for territory_count in territory_list:
                    print("AssociatedUsersCount count : " + territory_count.get_count())
                    territory = territory_count.get_territory()
                    if territory is not None:
                        print("AssociatedUsersCount Name :" + territory.get_name())
                        print("AssociatedUsersCount ID :" + str(territory.get_id()))
                        print("AssociatedUsersCount Subordinates :" + str(territory.get_subordinates()))
                info = response_wrapper.get_info()
                if info is not None:
                    if info.get_per_page() is not None:
                        print("Territory Info PerPage : " + str(info.get_per_page()))
                    if info.get_count() is not None:
                        print("Territory Info count : " + str(info.get_count()))
                    if info.get_page() is not None:
                        print("Territory Info page : " + str(info.get_page()))
                    if info.get_more_records() is not None:
                        print("Territory Info morerecords : " + str(info.get_more_records()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


AssociatedUserCount.initialize()
AssociatedUserCount.get_associated_user_count()