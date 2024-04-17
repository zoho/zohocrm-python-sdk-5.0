import datetime

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, BodyWrapper, Record, Field, Consent, FileDetails, \
    CreateRecordsHeader, APIException, SuccessResponse, ActionWrapper
from zohocrmsdk.src.com.zoho.crm.api.tags import Tag
from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class UpdateLeads(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_leads(module):
        record_operations = RecordOperations()
        body_wrapper = BodyWrapper()
        records = []
        record1 = Record()
        record1.set_id(440248001661043)
        record1.add_field_value(Field.Leads.last_name(), "Last Name")
        record1.add_field_value(Field.Leads.first_name(), "First Name")
        record1.add_field_value(Field.Leads.company(), "KKRNP")
        record1.add_field_value(Field.Leads.annual_revenue(), 1221.2)
        record1.add_field_value(Field.Leads.lead_status(), Choice("Not Contacted"))
        record1.add_field_value(Field.Leads.lead_source(), Choice("Advertisement"))
        record1.add_key_value("Title", "titleName")
        record1.add_field_value(Field.Leads.phone(), "11123")
        record1.add_field_value(Field.Leads.mobile(), "200221")
        record1.add_field_value(Field.Leads.industry(), Choice("ERP"))
        record1.add_field_value(Field.Leads.email_opt_out(), True)
        record1.add_field_value(Field.Leads.email(), "abc@zoho.com")
        record1.add_field_value(Field.Leads.fax(), "fax")
        record1.add_field_value(Field.Leads.website(), "website.com")
        record1.add_field_value(Field.Leads.no_of_employees(), 10)
        record1.add_field_value(Field.Leads.rating(), Choice("Active"))
        record1.add_field_value(Field.Leads.skype_id(), "Skype123")
        record1.add_field_value(Field.Leads.secondary_email(), "abc1@zoho.com")
        record1.add_field_value(Field.Leads.twitter(), "twitter55")
        # Address info of Lead
        record1.add_field_value(Field.Leads.city(), "City")
        record1.add_field_value(Field.Leads.country(), "country")
        record1.add_field_value(Field.Leads.street(), "street")
        record1.add_field_value(Field.Leads.state(), "state")
        record1.add_field_value(Field.Leads.zip_code(), "501210")
        #
        record1.add_field_value(Field.Leads.description(), "description")

        # Used when GDPR is enabled
        data_consent = Consent()
        data_consent.set_consent_remarks("Approved.")
        data_consent.set_consent_through('Email')
        data_consent.set_contact_through_email(True)
        data_consent.set_contact_through_social(False)
        data_consent.set_contact_through_phone(True)
        data_consent.set_contact_through_survey(False)
        data_consent.set_data_processing_basis("Obtained")
        record1.add_key_value('Data_Processing_Basis_Details', data_consent)
        
        # for custom fields
        record1.add_key_value("External", "Value12345")
        record1.add_key_value("LongInteger", 123)
        record1.add_key_value("CustomField", "custom_field")
        record1.add_key_value("Datetime", datetime.datetime(2020, 12, 20, 10, 29, 33))
        record1.add_key_value("Date_1", datetime.date(2020, 10, 12))
        record1.add_key_value("Subject", "AutomatedSDK")
        record1.add_key_value("Product_Name", "Automated")
        fileDetails = []
        fileDetail = FileDetails()
        fileDetail.set_file_id__s("ae9c7cefa418aec1d6a5cc2d9ab35c32a6ae23d729ad87c6d90b0bd44183")
        fileDetails.append(fileDetail)
        fileDetail2 = FileDetails()
        fileDetail2.set_file_id__s("ae9c7cefa418aec1d6a5cc2d9ab35c32a6ae2329ad87c6d90b0bd44183")
        fileDetails.append(fileDetail2)
        record1.add_key_value("file_Upload", fileDetails)
        # for Custom User LookUp
        user = MinifiedUser()
        user.set_id(4323001232)
        record1.add_key_value("User_1", user)
        # for Custom LookUp
        data = Record()
        data.set_id(4034234234234)
        record1.add_key_value("LookUp_1", data)
        # for Custom PicKList
        record1.add_key_value("Pick", Choice(True))
        # for Custom MultiPickList
        record1.add_key_value("Multiselect", [Choice("Option 2")])
        # for Subform
        subformList = []
        subform = Record()
        subform.add_key_value("customfield", "customValue")
        user1 = MinifiedUser()
        user1.set_id(42393413434213)
        subform.add_key_value("Userfield", user1)
        lookup = Record()
        lookup.set_id(440248001548062)
        subform.add_key_value("Test1", lookup)
        subformList.append(subform)
        delete_subform = Record()
        delete_subform.set_id(440248001727045)
        delete_subform.add_key_value("_delete", None)
        subformList.append(delete_subform)
        record1.add_key_value("Subform_2", subformList)
        # for MultiSelectLookUp / custom MultiSelectLookUp
        multiSelectList = []
        record = Record()
        record.add_key_value("id", 440248001563004)
        record.set_id(440248001390054)
        linkingRecord = Record()
        linkingRecord.set_id(440248001563004)
        linkingRecord.add_key_value("_delete", None)
        linkingRecord.add_key_value("MultiSelectLookup", record)
        multiSelectList.append(linkingRecord)
        record2 = Record()
        record2.add_key_value("id", 43234234423434)
        linkingRecord2 = Record()
        linkingRecord2.add_key_value("MultiSelectLookup", record2)
        multiSelectList.append(linkingRecord2)
        record1.add_key_value("MultiSelectLookup", multiSelectList)
        
        # can add update another record with same above mention fields
        record2 = Record()
        record2.set_id(34352353435)
        
        tag_list = []
        tag = Tag()
        tag.set_name("testtask")
        tag_list.append(tag)
        record1.set_tag(tag_list)
        # add record instance to list
        records.append(record1)
        body_wrapper.set_data(records)
        trigger = ["approval", "workflow", "blueprint"]
        body_wrapper.set_trigger(trigger)
        body_wrapper.set_lar_id("32434234234")
        header_instance = HeaderMap()
        # header_instance.add(CreateRecordsHeader.x_external, "Quotes.Quoted_Items.Product_Name.Products_External")
        response = record_operations.update_records(module, body_wrapper, header_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_data()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message().get_value())
                        elif isinstance(action_response, APIException):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message().get_value())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


module = "Leads"
UpdateLeads.initialize()
UpdateLeads.update_leads(module)