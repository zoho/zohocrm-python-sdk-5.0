from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.api.authenticator.store import DBStore
from zohocrmsdk.src.com.zoho.api.logger import Logger
from zohocrmsdk.src.com.zoho.crm.api import Initializer, UserSignature, SDKConfig
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations


class SingleThread(object):

    def __init__(self, environment, token, module_api_name, sdk_config):
        self.environment = environment
        self.token = token
        self.module_api_name = module_api_name
        self.sdk_config = sdk_config

    def run(self):
        try:
            Initializer.switch_user(self.environment, self.token, self.sdk_config)
            response = RecordOperations().get_records(self.module_api_name)
            print(response)

        except Exception as e:
            print(e)

    @staticmethod
    def call():
        log_instance = Logger.get_instance(Logger.Levels.INFO,
                                           "/Users/docs/logs_3.8.txt")
        token1 = OAuthToken("1000.xxxx", "xxxx", "xx.xxx.xxx")
        environment = USDataCenter.PRODUCTION()
        store = DBStore(password='root@123')
        resource_path = '/Users/python-sdk-sample-application'
        user1_module_api_name = 'Leads'
        user2_module_api_name = 'Contacts'
        token2 = OAuthToken("1000.xxxx", "xxx", "1000.xx.xxxx")
        sdk_config_1 = SDKConfig(auto_refresh_fields=True, pick_list_validation=False)
        sdk_config_2 = SDKConfig(auto_refresh_fields=False, pick_list_validation=False)
        Initializer.initialize(environment, token1, store, sdk_config_1, resource_path, log_instance)
        single_thread = SingleThread(environment, token1, user1_module_api_name, sdk_config_1)
        single_thread.run()
        single_thread = SingleThread(environment, token2, user2_module_api_name, sdk_config_2)
        single_thread.run()


SingleThread.call()