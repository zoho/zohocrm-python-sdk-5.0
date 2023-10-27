from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.shift_hours import ShiftHoursOperations, ResponseWrapper, APIException


class GetShiftHour(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_shift_hour(shift_hour_id):
        shift_hours_operations = ShiftHoursOperations()
        response = shift_hours_operations.get_shift_hour(shift_hour_id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                response_wrapper = response_object
                shift_count = response_wrapper.get_shift_count()
                print("Shift_count :")
                print("total_shift_with_user :" + str(shift_count.get_total_shift_with_user()))
                print("total_shift :" + str(shift_count.get_total_shift()))
                shift_hours = response_wrapper.get_shift_hours()
                for shift_hour in shift_hours:
                    print("name : " + shift_hour.get_name())
                    print("same_as_everyday : " + str(shift_hour.get_same_as_everyday()))
                    print("users_count : " + str(shift_hour.get_users_count()))
                    print("timezone : " + str(shift_hour.get_timezone()))
                    shift_days = shift_hour.get_shift_days()
                    if shift_days is not None:
                        print("ShiftDays : ")
                        for shift_day in shift_days:
                            print(shift_day)
                    daily_timing = shift_hour.get_daily_timing()
                    if daily_timing is not None:
                        print("daily_timing: ")
                        for daily_timing1 in daily_timing:
                            print(daily_timing1)
                    custom_timing = shift_hour.get_custom_timing()
                    if custom_timing is not None:
                        print("custom_timing: ")
                        for custom_timing1 in custom_timing:
                            shift_timing = custom_timing1.get_shift_timing()
                            print("shift_timing : ")
                            for shift_timing1 in shift_timing:
                                print(str(shift_timing1))
                            print("days: " + custom_timing.get_days())
                    holidays = shift_hour.get_holidays()
                    if holidays is not None:
                        print("holidays: ")
                        for holiday in holidays:
                            print("date : " + holiday.get_date())
                            print("year : " + holiday.get_year())
                            print("name : " + holiday.get_name())
                            print("id : " + holiday.get_id())
                    users = shift_hour.get_users()
                    if users is not None:
                        print("Users : ")
                        for user in users:
                            print("User_Id : " + user.get_id())
                            print("User_name : " + user.get_name())
                            print("User_email : " + user.get_email())
                            print("User_role : " + user.get_role())
                            print("User_ZUID : " + user.get_zuid())
                            print("effective_from : " + user.get_effective_from())
                    break_hours = shift_hour.get_break_hours()
                    if break_hours is not None:
                        for break_hour in break_hours:
                            print("break_hour_ID : " + str(break_hour.get_id()))
                            print("same_as_everyday : " + str(break_hour.get_same_as_everyday()))
                            breakdays = break_hour.get_break_days()
                            if breakdays is not None:
                                for breakday in breakdays:
                                    print("breakdays : " + breakday)
                            dailyTimings = break_hour.get_daily_timing()
                            if dailyTimings is not None:
                                for dailytiming in dailyTimings:
                                    print("dailyTiming : " + dailytiming)
                            break_hoursCustomTimings = break_hour.get_custom_timing()
                            if break_hoursCustomTimings is not None:
                                for break_hourCustomTiming in break_hoursCustomTimings:
                                    print("CustomTiming : ")
                                    breakTimings = break_hourCustomTiming.get_break_timing()
                                    if breakTimings is not None:
                                        for breakTiming in breakTimings:
                                            print("breakTiming : " + breakTiming)
                                        print("days : " + break_hourCustomTiming.get_days())

            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


shift_hour_id = 440248001538100
GetShiftHour.initialize()
GetShiftHour.get_shift_hour(shift_hour_id)