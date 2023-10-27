from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.appointment_preference import AppointmentPreferenceOperations, BodyWrapper, \
    AppointmentPreference, Layout, FieldMappings, Field, ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class UpdateAppointmentPreference(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_appointment_preference():
        appointment_preference_operartions = AppointmentPreferenceOperations()
        request = BodyWrapper()
        appoint_preferences = AppointmentPreference()
        appoint_preferences.set_allow_booking_outside_businesshours(False)
        appoint_preferences.set_allow_booking_outside_service_availability(True)
        appoint_preferences.set_when_appointment_completed(Choice("do_not_create_deal"))
        appoint_preferences.set_when_duration_exceeds(Choice("mark_as_complete"))
        appoint_preferences.set_show_job_sheet(False)
        dealRecordConfiguration = {}
        layout = Layout()
        layout.set_api_name("Standard")
        layout.set_id(32313243323232)
        dealRecordConfiguration['layout'] = layout
        mappings = []
        field_mappings = FieldMappings()
        field_mappings.set_type(Choice("static"))
        field_mappings.set_value("Closed Won")
        field = Field()
        field.set_api_name("Stage")
        field.set_id(34342344523243)
        field_mappings.set_field(field)
        mappings.append(field_mappings)

        dealRecordConfiguration["field_mappings"] = mappings
        # appoint_preferences.set_deal_record_configuration(dealRecordConfiguration)
        request.set_appointment_preferences(appoint_preferences)
        response = appointment_preference_operartions.update_appointment_preference(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response = response_object.get_appointment_preferences()
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
                        print("Message: " + action_response.get_message())

                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


UpdateAppointmentPreference.initialize()
UpdateAppointmentPreference.update_appointment_preference()