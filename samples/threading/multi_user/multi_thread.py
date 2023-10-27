import threading

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.api.authenticator.store import FileStore, DBStore
from zohocrmsdk.src.com.zoho.api.logger import Logger
from zohocrmsdk.src.com.zoho.crm.api import Initializer, SDKConfig, RequestProxy, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, ResponseWrapper, APIException, GetRecordParam


class MultiThread(threading.Thread):

    def __init__(self, environment, token, module_api_name, sdk_config, proxy=None):
        super().__init__()
        self.environment = environment
        self.token = token
        self.module_api_name = module_api_name
        self.sdk_config = sdk_config
        self.proxy = proxy

    def run(self):
        try:
            Initializer.switch_user(self.environment, self.token, self.sdk_config, self.proxy)
            param_instance = ParameterMap()
            param_instance.add(GetRecordParam.fields, "id")
            response = RecordOperations().get_records(self.module_api_name, param_instance)
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
                            for key, value in record.get_key_values().items():
                                print(key + " : " + str(value))
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message().get_value())
        except Exception as e:
            print(e)

    @staticmethod
    def call():
        log_instance = Logger.get_instance(Logger.Levels.INFO,
                                           "/Users/sample-application/logs.txt")
        token1 = OAuthToken("1000.xxx", "xxx", "1000.xxx.xxx")
        environment = USDataCenter.PRODUCTION()
        sdk_config_1 = SDKConfig(auto_refresh_fields=False, pick_list_validation=True)
        store = DBStore(password='password')
        store = FileStore("/Users/sample-application/sdk_token.txt")
        resource_path = '/Users/sample-application/file'
        auto_refresh_fields = True
        user1_module_api_name = 'Leads'
        user2_module_api_name = 'Contacts'
        token2 = OAuthToken("1000.xxx", "xxx", "1000.xxxx.xxx")
        proxy_user2 = RequestProxy('host', 8080)
        sdk_config_2 = SDKConfig(auto_refresh_fields=True, pick_list_validation=False)
        Initializer.initialize(environment, token1)
        t1 = MultiThread(environment, token1, user1_module_api_name, sdk_config_1)
        t2 = MultiThread(environment, token2, user2_module_api_name, sdk_config_2)
        t1.start()
        t2.start()
        t1.join()
        t2.join()


MultiThread.call()
