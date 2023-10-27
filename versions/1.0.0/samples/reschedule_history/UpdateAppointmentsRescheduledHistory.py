import datetime

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.reschedule_history import RescheduleHistoryOperations, BodyWrapper, \
    RescheduleHistory, AppointmentName, User, ActionWrapper, SuccessResponse, APIException


class UpdateAppointmentsRescheduledHistory(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_appointments_reschedule_history():
        reschedule_history_operations = RescheduleHistoryOperations()
        request = BodyWrapper()
        data = []
        reschedule_history = RescheduleHistory()
        reschedule_history.set_id(3242342342422)
        appointment_name = AppointmentName()
        appointment_name.set_name("Name")
        appointment_name.set_id(34234234234234)
        reschedule_history.set_appointment_name(appointment_name)
        rescheduled_by = User()
        rescheduled_by.set_id(3242342342312)
        rescheduled_by.set_name("username")
        reschedule_history.set_rescheduled_by(rescheduled_by)
        reschedule_history.set_rescheduled_to(datetime.datetime(2023, 11, 20, 11, 30, 1))
        reschedule_history.set_rescheduled_from(datetime.datetime(2023, 11, 20, 9, 30, 1))
        reschedule_history.set_rescheduled_time(datetime.datetime(2023, 11, 20, 20, 9, 1))
        reschedule_history.set_reschedule_note("Customer unavailable")
        reschedule_history.set_reschedule_reason("By customer")
        data.append(reschedule_history)
        request.set_data(data)
        response = reschedule_history_operations.update_appointments_rescheduled_history(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_data()
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


UpdateAppointmentsRescheduledHistory.initialize()
UpdateAppointmentsRescheduledHistory.update_appointments_reschedule_history()