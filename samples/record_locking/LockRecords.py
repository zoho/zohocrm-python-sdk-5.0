from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.record_locking import RecordLockingOperations, \
    LockRecord, BodyWrapper, ActionWrapper, SuccessResponse, APIException


class LockRecords:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def lock_records(module_api_name, record_id):
        record_locking_configurations_operations = RecordLockingOperations(record_id, module_api_name)
        request = BodyWrapper()
        data = []
        locked_record = LockRecord()
        locked_record.set_locked_reason__s("deal in progress")
        data.append(locked_record)
        request.set_data(data)
        response = record_locking_configurations_operations.lock_records(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_data()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message().get_value())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


LockRecords.initialize()
LockRecords.lock_records("Leads", 440280377)
