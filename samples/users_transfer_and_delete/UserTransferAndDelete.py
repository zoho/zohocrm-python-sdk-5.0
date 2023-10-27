from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.users_transfer_delete import UsersTransferDeleteOperations, BodyWrapper, \
    TransferAndDelete, Transfer, MoveSubordinate, ActionWrapper, SuccessResponse, APIException


class UserTransferAndDelete(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def user_transfer_and_delete(id):
        user_transfer_delete_operations = UsersTransferDeleteOperations()
        request = BodyWrapper()
        transfer_and_deletes = []
        transfer_and_delete = TransferAndDelete()
        transfer = Transfer()
        transfer.set_records(True)
        transfer.set_assignment(True)
        transfer.set_criteria(False)
        transfer.set_id(32329329393092)
        transfer_and_delete.set_transfer(transfer)
        move_subordinate = MoveSubordinate()
        move_subordinate.set_id(3409093029302)
        transfer_and_delete.set_move_subordinate(move_subordinate)
        transfer_and_deletes.append(transfer_and_delete)
        request.set_transfer_and_delete(transfer_and_deletes)
        response = user_transfer_delete_operations.user_transfer_and_delete(id, request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_transfer_and_delete()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message().get_value())
                        elif isinstance(action_response, APIException):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message().get_value())

                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


UserTransferAndDelete.initialize()
UserTransferAndDelete.user_transfer_and_delete(id=32303903302392)