from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.appointment_preference import *
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class GetAppointmentPreferences:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def getAppointmentPreferences():
        appointmentPrefernceOperations = AppointmentPreferenceOperations()
        paramInstance = ParameterMap()
        paramInstance.add(GetAppointmentPreferenceParam.include, "")
        response = appointmentPrefernceOperations.get_appointment_preference(paramInstance)
        if response is not None:
            print("Status code: " + str(response.get_status_code()))
            if response.get_status_code() == 204:
                print("No Content")
                return
            responseHandler = response.get_object()
            if isinstance(responseHandler, ResponseWrapper):
                responseWrapper = responseHandler
                appointmentPreferences = responseWrapper.get_appointment_preferences()
                if appointmentPreferences is not None:
                    print("AppointmentPreference showJobSheet : " + str(appointmentPreferences.get_show_job_sheet()))
                    print("AppointmentPreference whenDurationExceeds : " + appointmentPreferences.get_when_duration_exceeds().get_value())
                    print("AppointmentPreference allowBookingOutsideServiceAvailability : " + str(appointmentPreferences.get_allow_booking_outside_service_availability()))
                    print( "AppointmentPreference whenAppointmentCompleted : " + appointmentPreferences.get_when_appointment_completed().get_value())
                    print("AppointmentPreference allowBookingOutsideBusinesshours : " + str(appointmentPreferences.get_allow_booking_outside_businesshours()))
                    dealRecordConfiguration = appointmentPreferences.get_deal_record_configuration()
                    if dealRecordConfiguration is not None:
                        for key, value in dealRecordConfiguration.items():
                            if key == "layout":
                                layout = value
                                print("layout Id: " + layout.get_id())
                                print("LayoutName :" + layout.get_api_name())
                            if key == "field_mappings":
                                field_mappings = value
                                if field_mappings is not None:
                                    for field_mapping in field_mappings:
                                        print("Field Mappings type: " + field_mapping.get_type().get_value())
                                        print("Field Mappings value: " + field_mapping.get_value())
                                        field = field_mapping.get_field()
                                        if field is not None:
                                            print("Field APIName: " + field.get_api_name())
                                            print("Field Id: " + field.get_id())
            elif isinstance(responseHandler, APIException):
                print("Status: " + responseHandler.get_status().get_value())
                print("Code: " + responseHandler.get_code().get_value())
                print("Details")
                details = responseHandler.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + responseHandler.get_message())


GetAppointmentPreferences.initialize()
GetAppointmentPreferences.getAppointmentPreferences()
