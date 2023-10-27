import threading

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.api.authenticator.store import DBStore
from zohocrmsdk.src.com.zoho.api.logger import Logger
from zohocrmsdk.src.com.zoho.crm.api import SDKConfig, Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, GetRecordParam


class MultiThread(threading.Thread):

    def __init__(self, module_api_name):
        super().__init__()
        self.module_api_name = module_api_name

    def run(self):
        print("Calling Get Records for module: " + self.module_api_name)
        param_instance = ParameterMap()
        param_instance.add(GetRecordParam.fields, "id")
        response = RecordOperations().get_records(self.module_api_name, param_instance)
        print(response)

    @staticmethod
    def call():
        log_instance = Logger.get_instance(Logger.Levels.INFO,
                                           "/Users/docs/multi_thread_logs.txt")
        token = OAuthToken("1000.xxx", "xxxx", "1000.xxx.xxx")
        environment = USDataCenter.PRODUCTION()
        store = DBStore(password='root@123')
        resource_path = '/Users/zohocrm-python-sdk-sample-application'
        sdk_config = SDKConfig(auto_refresh_fields=True, pick_list_validation=False)
        Initializer.initialize(environment, token, store, sdk_config, resource_path, log_instance)
        t1 = MultiThread('Leads')
        t2 = MultiThread('Deals')
        t1.start()
        t2.start()
        t1.join()
        t2.join()


MultiThread.call()
