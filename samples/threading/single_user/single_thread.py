from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.api.authenticator.store import DBStore
from zohocrmsdk.src.com.zoho.api.logger import Logger
from zohocrmsdk.src.com.zoho.crm.api import SDKConfig, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations


class SingleThread:
    @staticmethod
    def call():
        log_instance = Logger.get_instance(Logger.Levels.INFO,
                                           "/Users/docs/multi_thread_logs.txt")
        token = OAuthToken("1000.xxxx", "xxxx", "1000.xxx.xxx")
        environment = USDataCenter.PRODUCTION()
        store = DBStore(password='root@123')
        resource_path = '/Users/python-sdk-sample-application'
        sdk_config = SDKConfig(auto_refresh_fields=True, pick_list_validation=False)
        Initializer.initialize(environment, token, store, sdk_config, resource_path, log_instance)
        module_1 = "Leads"
        module_2 = "Contacts"
        response_1 = RecordOperations().get_records(module_1)
        response_2 = RecordOperations().get_records(module_2)


SingleThread.call()