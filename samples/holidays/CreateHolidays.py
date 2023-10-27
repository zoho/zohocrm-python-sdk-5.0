from datetime import date

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.holidays import HolidaysOperations, BusinessHoliday, CreateBusinessHoliday, \
    CreateShiftHoliday, ShiftHoliday, ShiftHour, APIException, SuccessResponse, ActionWrapper
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class CreateHolidays(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_holidays():
        holidays_operations = HolidaysOperations()
        request = CreateBusinessHoliday()
        holidays = []
        holiday = BusinessHoliday()
        holiday.set_name("holiday1")
        holiday.set_date(date(2023, 9, 22))
        holiday.set_type(Choice("business_holiday"))
        holidays.append(holiday)
        request.set_holidays(holidays)
        # when type is shift_holiday
        request1 = CreateShiftHoliday()
        shift_holidays = []
        shift_holiday = ShiftHoliday()
        shift_hour = ShiftHour()
        shift_hour.set_name("shift hour for TX")
        shift_hour.set_id(440248001507189)
        shift_holiday.set_shift_hour(shift_hour)
        shift_holiday.set_name("shift-holiday")
        shift_holiday.set_type(Choice("shift_holiday"))
        shift_holiday.set_date(date(2023, 11, 11))
        shift_holidays.append(shift_holiday)
        request1.set_holidays(shift_holidays)

        response = holidays_operations.create_holidays(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_holidays()
                    for action_response in action_response_list:
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


CreateHolidays.initialize()
CreateHolidays.create_holidays()