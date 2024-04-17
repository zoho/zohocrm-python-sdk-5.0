from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.users_territories import UsersTerritoriesOperations, ValidationWrapper, \
    BulkValidation, Validation, APIException


class ValidateBeforeTransfer(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def validate_before_transfer(territory_id, user_id):
        user_territories_operartions = UsersTerritoriesOperations()
        response = user_territories_operartions.validate_before_transfer(territory_id, user_id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ValidationWrapper):
                user_territory = response_object.get_validate_before_transfer()
                for validation_group in user_territory:
                    if isinstance(validation_group, BulkValidation):
                        print("User Territory Validation Alert : " + str(validation_group.get_alert()))
                        print("User Territory Validation Assignment : " + str(validation_group.get_assignment()))
                        print("User Territory Validation Criteria : " + str(validation_group.get_criteria()))
                        print("User Territory Validation Name : " + validation_group.get_name())
                        print("User Territory Validation Id : " + str(validation_group.get_id()))
                    elif isinstance(validation_group, Validation):
                        print("User Territory Validation Records : " + str(validation_group.get_records()))
                        print("User Territory Validation Name : " + validation_group.get_name())
                        print("User Territory Validation Id : " + str(validation_group.get_id()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


user_id = 440248001502002
territory_id = 440248001390040
ValidateBeforeTransfer.initialize()
ValidateBeforeTransfer.validate_before_transfer(territory_id, user_id)