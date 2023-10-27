from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, BodyWrapper, Record, Territory, ActionWrapper, \
    SuccessResponse, APIException


class AssignTerritoryToRecord:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def assign_territory_to_record(module_api_name, id):
        # API Name of the module to assignTerritoriesToMultipleRecords
        record_operations = RecordOperations()
        request = BodyWrapper()
        # List of Record instances
        records = []
        record1 = Record()
        record1.set_id(3477061012107002)
        territory = Territory()
        territory.set_id(3477061003051397)
        record1.add_key_value("Territories", [territory])
        # Add Record instance to the list
        records.append(record1)
        request.set_data(records)
        # Call assign_territory_to_record method that takes module_api_name, id and  BodyWrapper instance as parameter.
        response = record_operations.assign_territory_to_record(module_api_name, id, request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_responses = response_object.get_data()
                    for action_response in action_responses:
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


module_api_name = "Leads"
record_id = 3232342423423
AssignTerritoryToRecord.initialize()
AssignTerritoryToRecord.assign_territory_to_record(module_api_name, record_id)