from datetime import date

import pytz
from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.shift_hours import ShiftHoursOperations, BodyWrapper, ShiftHours, \
    ShiftCustomTiming, BreakHours, BreakCustomTiming, Users, Holidays, APIException, SuccessResponse, ActionWrapper


class CreateShiftHours(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_shift_hours():
        shift_hours_operations = ShiftHoursOperations()
        request = BodyWrapper()
        shift_hours_array = []
        shift_hours = ShiftHours()
        shift_hours.set_timezone(pytz.timezone("Asia/Kolkata"))
        shift_hours.set_name("Shift_hours_with_holiday")
        shift_hours.set_same_as_everyday(False)
        shift_days = ["Monday", "Tuesday"]
        shift_hours.set_shift_days(shift_days)
        # if same as everyday is true
        daily_timing = ["10:00", "19:00"]
        shift_hours.set_daily_timing(daily_timing)
        # if same as everyday is false
        custom_timings =[]
        custom_timing = ShiftCustomTiming()
        shift_timing = ["10:00", "19:00"]
        custom_timing.set_shift_timing(shift_timing)
        custom_timing.set_days("Monday")
        custom_timings.append(custom_timing)
        custom_timing1 = ShiftCustomTiming()
        shift_timing1 = ["10:00", "19:00"]
        custom_timing1.set_shift_timing(shift_timing1)
        custom_timing1.set_days("Tuesday")
        custom_timings.append(custom_timing1)
        shift_hours.set_custom_timing(custom_timings)
        ##
        break_hours = []
        break_hour = BreakHours()
        break_days = ["Monday", "Tuesday"]
        break_hour.set_break_days(break_days)
        # if same as everyday is true
        break_hour.set_same_as_everyday(True)
        daily_timing_for_break_hours =["11:00", "11:30"]
        break_hour.set_daily_timing(daily_timing_for_break_hours)
        break_hours.append(break_hour)
        shift_hours.set_break_hours(break_hours)
        # if same as everyday is false
        break_hour.set_same_as_everyday(False)
        custom_timings_for_break_hours = []
        custom_timings_for_break_hour = BreakCustomTiming()
        break_timings = ["12:00", "12:15"]
        custom_timings_for_break_hour.set_break_timing(break_timings)
        custom_timings_for_break_hour.set_days("Monday")
        custom_timings_for_break_hours.append(custom_timings_for_break_hour)
        custom_timings_for_break_hour1 = BreakCustomTiming()
        break_timings1 = ["16:00", "16:15"]
        custom_timings_for_break_hour1.set_break_timing(break_timings1)
        custom_timings_for_break_hour1.set_days("Tuesday")
        custom_timings_for_break_hours.append(custom_timings_for_break_hour1)
        break_hour.set_custom_timing(custom_timings_for_break_hours)
        break_hours.append(break_hour)
        shift_hours.set_break_hours(break_hours)
        ##
        users = []
        user = Users()
        user = Users()
        user.set_id(343242421434)
        user.set_effective_from(date(2023, 10, 12))
        users.append(user)
        shift_hours.set_users(users)
        holidays = []
        holiday = Holidays()
        holiday.set_date(date(2023, 10, 12))
        holiday.set_id(3323423423423)
        holiday.set_name("holi")
        holiday.set_year(2023)
        holidays.append(holiday)
        # shift_hours.set_holidays(holidays)
        shift_hours_array.append(shift_hours)
        request.set_shift_hours(shift_hours_array)
        response = shift_hours_operations.create_shifts_hours(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_shift_hours()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message())
                        elif isinstance(action_response, APIException):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message())

                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


CreateShiftHours.initialize()
CreateShiftHours.create_shift_hours()