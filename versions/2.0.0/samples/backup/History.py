from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.backup import BackupOperations, HistoryWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class History(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def history():
        backup_operations = BackupOperations()
        paramInstance = ParameterMap()
        response = backup_operations.history(paramInstance)
        if response is not None:
            print(("Status Code: " + str(response.get_status_code())))
            responseHandler = response.get_object()
            if isinstance(responseHandler, HistoryWrapper):
                historyWrapper = responseHandler
                history = historyWrapper.get_history()
                for history1 in history:
                    print("History Id : " + history1.get_is())
                    done_by = history1.get_done_by()
                    if done_by is not None:
                        print("History DoneBy Id : " + done_by.get_id())
                        print("History DoneBy Name : " + done_by.get_name())
                        print("History DoneBy Zuid: " + done_by.get_zuid())
                    print("History LogTime: " + history1.get_log_time())
                    print("History State: " + history1.get_state())
                    print("History Action: " + history1.get_action())
                    print("History RepeatType: " + history1.get_repeat_type())
                    print("History FileName: " + history1.get_file_name())
                    print("History Count: " + history1.get_count())
                info = historyWrapper.get_info()
                if info is not None:
                    if info.get_per_page() is not None:
                        print("History Info PerPage: " + str(info.get_per_page()))
                    if info.get_count() is not None:
                        print("History Info Count: " + str(info.get_count()))
                    if info.get_page() is not None:
                        print("History Info page: " + str(info.get_page()))
                    if info.get_more_records() is not None:
                        print("History Info MoreRecords: " + str(info.get_more_records()))
            elif isinstance(responseHandler, APIException):
                print("Status: " + responseHandler.get_status().get_value())
                print("Code: " + responseHandler.get_code().get_value())
                print("Details")
                details = responseHandler.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + responseHandler.get_message())


History.initialize()
History.history()