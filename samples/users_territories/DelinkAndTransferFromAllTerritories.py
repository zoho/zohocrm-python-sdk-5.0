from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.users_territories import UsersTerritoriesOperations, TransferWrapper, \
    TransferAndDelink, TransferToUser, TransferActionWrapper, SuccessResponse, APIException


class DelinkAndTransferFromAllTerritories(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def de_link_and_transfer_from_all_territories(user_id):
        user_territories_operations = UsersTerritoriesOperations()
        request = TransferWrapper()
        user_territories_list = []
        territory = TransferAndDelink()
        territory.set_id(32032312312)
        transfer_to_user = TransferToUser()
        transfer_to_user.set_id(320909232039923)
        territory.set_transfer_to_user(transfer_to_user)
        user_territories_list.append(territory)
        request.set_transfer_and_delink(user_territories_list)
        response = user_territories_operations.delink_and_transfer_from_all_territories(user_id, request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, TransferActionWrapper):
                    action_response_list = response_object.get_transfer_and_delink()
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


user_id = 32423412312312
DelinkAndTransferFromAllTerritories.initialize()
DelinkAndTransferFromAllTerritories.de_link_and_transfer_from_all_territories(user_id)