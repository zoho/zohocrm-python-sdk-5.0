from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.reschedule_history import RescheduleHistoryOperations, ResponseWrapper, \
    APIException, GetAppointmentsRescheduledHistoryParam


class GetAppointmentsRescheduledHistory(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_appointments_rescheduled_history():
        reschedled_history_operations = RescheduleHistoryOperations()
        param_instance = ParameterMap()
        param_instance.add(GetAppointmentsRescheduledHistoryParam.fields, "Rescheduled_From,Rescheduled_To")
        response = reschedled_history_operations.get_appointments_rescheduled_history(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                response_wrapper = response_object
                data = response_wrapper.get_data()
                if data is not None:
                    for history in data:
                        print("CurrencySymbol: " + history.get_currency_symbol())
                        print("reviewProcess: " + str(history.get_review_process()))
                        print("rescheduleReason: " + history.get_reschedule_reason())
                        print("sharingPermission: " + history.get_sharing_permission())
                        print("Name: " + history.get_name())
                        print("Review: " + str(history.get_review()))
                        print("State: " + history.get_state())
                        print("canvasId: " + str(history.get_canvas_id()))
                        print("processFlow: " + str(history.get_process_flow()))
                        print("Id: " + str(history.get_id()))
                        print("ziaVisions: " + str(history.get_zia_visions()))
                        print("approved: " + str(history.get_approved()))
                        print("ziaVisions: " + str(history.get_zia_visions()))
                        print("editable: " + str(history.get_editable()))
                        print("orchestration: " + str(history.get_orchestration()))
                        print("inMerge: " + str(history.get_in_merge()))
                        print("approvalState: " + str(history.get_approval_state()))
                        print("rescheduleNote: " + history.get_reschedule_note())
                        print("rescheduledTo: " + str(history.get_rescheduled_to()))
                        print("rescheduledTime: " + str(history.get_rescheduled_time()))
                        print("rescheduledFrom: " + str(history.get_rescheduled_from()))
                        appointmentName = history.get_appointment_name()
                        if appointmentName is not None:
                            print("Appointment Name: " + appointmentName.get_name())
                            print("Appointmnet Id: " + str(appointmentName.get_id()))
                        approval = history.get_approval()
                        if approval is not None:
                            print("delegate : " + str(approval.get_delegate()))
                            print("approve : " + str(approval.get_approve()))
                            print("reject : " + str(approval.get_reject()))
                            print("resubmit : " + str(approval.get_resubmit()))
                        modifiedBy = history.get_modified_by()
                        if modifiedBy is not None:
                            print("modifiedBy : " + str(modifiedBy.get_id()))
                            print("modifiedBy : " + modifiedBy.get_name())
                            print("modifiedBy : " + modifiedBy.get_email())
                        rescheduledBy = history.get_rescheduled_by()
                        if rescheduledBy is not None:
                            print("rescheduledBy : " + str(rescheduledBy.get_id()))
                            print("rescheduledBy : " + rescheduledBy.get_name())
                            print("rescheduledBy" + rescheduledBy.get_email())
                        createdBy = history.get_created_by()
                        if createdBy is not None:
                            print("createdBy : " + str(createdBy.get_id()))
                            print("createdBy : " + createdBy.get_name())
                            print("createdBy : " + createdBy.get_email())
                info = response_wrapper.get_info()
                if info is not None:
                    for info1 in info:
                        if info1 is not None:
                            if info1.get_per_page() is not None:
                                print("RelatedRecord Info PerPage: " + str(info1.get_per_page()))
                            if info1.get_count() is not None:
                                print("RelatedRecord Info Count: " + str(info1.get_count()))
                            if info1.get_page() is not None:
                                print("RelatedRecord Info Page: " + str(info1.get_page()))
                            if info1.get_more_records() is not None:
                                print("RelatedRecord Info MoreRecords: " + str(info1.get_more_records()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message().get_value())


GetAppointmentsRescheduledHistory.initialize()
GetAppointmentsRescheduledHistory.get_appointments_rescheduled_history()