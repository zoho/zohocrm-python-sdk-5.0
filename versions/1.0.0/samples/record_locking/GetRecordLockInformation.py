from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.parameter_map import ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.record_locking import RecordLockingOperations, \
    ResponseWrapper, LockedForS, APIException, getrecordlockinformationParam


class GetRecordLockInformation:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_record_lock_information(module_api_name, record_id):
        record_locking_configurations_operations = RecordLockingOperations()
        param_instance = ParameterMap()
        param_instance.add(getrecordlockinformationParam.fields, "Lock_Source__s")
        response = record_locking_configurations_operations.get_record_lock_information(record_id, module_api_name, param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    record_list = response_object.get_data()
                    for record in record_list:
                        key_values = record.get_key_values()
                        for key_name, value in key_values.items():
                            if isinstance(value, LockedForS):
                                print(key_name)
                                print("locked_for_s name: " + value.get_name())
                                print("locked_for_s id: " + str(value.get_id()))
                                module = value.get_module()
                                if module is not None and isinstance(module, dict):
                                    print("locked_for_s module")
                                    for key, val in module.items():
                                        print(key + " : " + str(val))

                            elif isinstance(value, dict):
                                print(key_name + " : ")
                                for key, val in value.items():
                                    print(key + " : " + str(val))
                            else:
                                print(key_name + " : " + str(value))

                    info = response_object.get_info()
                    if info is not None:
                        if info.get_per_page() is not None:
                            print('Record Info PerPage: ' +
                                  str(info.get_per_page()))
                        if info.get_page() is not None:
                            print('Record Info Page: ' + str(info.get_page()))
                        if info.get_count() is not None:
                            print('Record Info Count: ' +
                                  str(info.get_count()))
                        if info.get_more_records() is not None:
                            print('Record Info MoreRecords: ' +
                                  str(info.get_more_records()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


GetRecordLockInformation.initialize()
GetRecordLockInformation.get_record_lock_information(module_api_name="Leads", record_id=4402481787377)