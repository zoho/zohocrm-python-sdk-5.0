from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.timelines import TimelinesOperations, ResponseWrapper, APIException


class GetTimelines(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_time_lines(module, record_id):
        timelines_operations = TimelinesOperations()
        param_instance = ParameterMap()
        response = timelines_operations.get_timelines(module, record_id, param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                timelines = response_object.get_timeline()
                if timelines is not None:
                    for timeline in timelines:
                        done_by = timeline.get_done_by()
                        if done_by is not None:
                            print("Done_by None: " + done_by.get_name())
                            print("Done_By Id : " + done_by.get_id())
                        related_record = timeline.get_related_record()
                        if related_record is not None:
                            print("RelatedRecord Id: " + str(related_record.get_id()))
                            print("RelatedRecord Name: " + related_record.get_name())
                            module1 = related_record.get_module()
                            print("Module : ")
                            if module1 is not None:
                                print("RelatedRecord Module Name: " + str(module1.get_name()))
                                print("RelatedRecord Module Id: " + module1.get_id())
                        automationDetails = timeline.get_automation_details()
                        if automationDetails is not None:
                            print("automationdetails type: " + automationDetails.get_type())
                            rule = automationDetails.get_rule()
                            if rule is not None:
                                print("automationDetails Rule Name :" + rule.get_name())
                                print("automationDetails Rule Id :" + rule.get_id())
                        record1 = timeline.get_record()
                        if record1 is not None:
                            print("Record Id: " + str(record1.get_id()))
                            print("Record Name: " + str(record1.get_name()))
                            module2 = record1.get_module()
                            print("Module : ")
                            if module2 is not None:
                                print("Record Module Name: " + module2.get_api_name())
                                print("Record Module Id: " + str(module2.get_id()))
                        print("auditedTime : " + str(timeline.get_audited_time()))
                        print("action : " + str(timeline.get_action()))
                        print("Timeline Id: " + str(timeline.get_id()))
                        print("source: " + timeline.get_source())
                        print("extension: " + str(timeline.get_extension()))
                        print("Type:: " + str(timeline.get_type()))
                        field_history = timeline.get_field_history()
                        if field_history is not None:
                            for history in field_history:
                                print("FieldHistory dataType: " + str(history.get_data_type()))
                                print("FieldHistory enableColourCode: " + str(history.get_enable_colour_code()))
                                print("FieldHistory fieldLabel: " + str(history.get_field_label()))
                                print("FieldHistory apiName: " + str(history.get_api_name()))
                                print("FieldHistory id: " + str(history.get_id()))
                                value = history.get_value()
                                if value is not None:
                                    print("new :" + str(value.get_new()))
                                    print("old :" + str(value.get_old()))
                                pickListValues = history.get_pick_list_values()
                                if pickListValues is not None:
                                    for pickListValue in pickListValues:
                                        print("picklistvalue DisplayValue : " + pickListValue.get_display_value())
                                        print("picklistvalue sequenceNumber : " + pickListValue.get_sequence_number())
                                        print("picklistvalue colourCode : " + pickListValue.get_colour_code())
                                        print("picklistvalue actualValue : " + pickListValue.get_actual_value())
                                        print("picklistvalue id : " + pickListValue.get_id())
                                        print("picklistvalue type : " + pickListValue.get_type())
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message().get_value())


module = "Leads"
record_id = "4402480774074"
GetTimelines.initialize()
GetTimelines.get_time_lines(module, record_id)