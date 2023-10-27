from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.holidays import HolidaysOperations, GetHolidaysParam, ResponseWrapper, APIException


class GetHolidays(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_holidays():
        holidays_operations = HolidaysOperations()
        param_instance = ParameterMap()
        # param_instance.add(GetHolidaysParam.shift_id, 440248001507189)
        response  =  holidays_operations.get_holidays(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                response_wrapper = response_object
                holidays = response_wrapper.get_holidays()
                if holidays is not None:
                    print("holidays : ")
                    for holiday in holidays:
                        print("Hoilday ID: " + str(holiday.get_id()))
                        print("Name: " + holiday.get_name())
                        print("date: " + str(holiday.get_date()))
                        print("year: " + str(holiday.get_year()))
                        print("type: " + holiday.get_type())
                        shift_hour = holiday.get_shift_hour()
                        if shift_hour is not None:
                            print("shifthour: ")
                            print("name : " + shift_hour.get_name())
                            print("Shifthour id : " + str(shift_hour.get_id()))
                info = response_wrapper.get_info()
                if info is not None:
                    print("info : ")
                    print("perpage : " + str(info.get_per_page()))
                    print("count : " + str(info.get_count()))
                    print("page : " + str(info.get_page()))
                    print("more_records : " + str(info.get_more_records()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message().get_value())


GetHolidays.initialize()
GetHolidays.get_holidays()
