import datetime

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, BodyWrapper, Record, Field, Consent, FileDetails, \
    CreateRecordsHeader, APIException, SuccessResponse, ActionWrapper
from zohocrmsdk.src.com.zoho.crm.api.tags import Tag
from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class UpdateContacts(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_contacts(module):
        record_operations = RecordOperations()
        body_wrapper = BodyWrapper()
        records = []
        record1 = Record()
        record1.set_id(32423452332)
        record1.add_field_value(Field.Contacts.last_name(), "Last Name")
        record1.add_field_value(Field.Contacts.email(), "abc@zoho.com")
        accountname = Record()
        accountname.set_id(440248001392066)
        record1.add_field_value(Field.Contacts.account_name(), accountname)
        record1.add_field_value(Field.Contacts.first_name(), "First Name")
        record1.add_field_value(Field.Contacts.phone(), "3323")
        record1.add_field_value(Field.Contacts.title(), "Title")
        record1.add_field_value(Field.Contacts.department(), "department name")
        record1.add_field_value(Field.Contacts.other_phone(), "12132")
        record1.add_field_value(Field.Contacts.home_phone(), "23123121")
        record1.add_field_value(Field.Contacts.mobile(), "4141")
        record1.add_field_value(Field.Contacts.fax(), "fax")
        record1.add_field_value(Field.Contacts.date_of_birth(), datetime.date(2023, 12, 1))
        vendorName = Record()
        vendorName.set_id(440248001330038)
        record1.add_field_value(Field.Contacts.vendor_name(), vendorName)
        record1.add_field_value(Field.Contacts.email_opt_out(), False)
        record1.add_field_value(Field.Contacts.secondary_email(), "abc2@zoho.com")
        contact = Record()
        contact.set_id(3322321323)
        record1.add_field_value(Field.Contacts.reporting_to(), contact)
        record1.add_field_value(Field.Contacts.skype_id(), "skype_id")
        # Address info of Contact
        record1.add_field_value(Field.Contacts.mailing_city(), "city")
        record1.add_field_value(Field.Contacts.mailing_country(), "country")
        record1.add_field_value(Field.Contacts.mailing_state(), "state")
        record1.add_field_value(Field.Contacts.mailing_street(), "street")
        record1.add_field_value(Field.Contacts.mailing_zip(), "zip")
        record1.add_field_value(Field.Contacts.other_city(), "city")
        record1.add_field_value(Field.Contacts.other_country(), "country")
        record1.add_field_value(Field.Contacts.other_state(), "state")
        record1.add_field_value(Field.Contacts.other_street(), "street")
        record1.add_field_value(Field.Contacts.other_zip(), "zip")
        #
        record1.add_field_value(Field.Contacts.description(), "description")

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
        record1.add_key_value("MultiSelecr", [Choice("Option 1"), Choice("Option 2")])
        # for Subform
        subformList = []
        subform = Record()
        subform.add_key_value("customfield", "customValue")
        user1 = MinifiedUser()
        user1.set_id(42393413434213)
        subform.add_key_value("Userfield", user1)
        subformList.append(subform)
        record1.add_key_value("Subform_2", subformList)
        # for MultiSelectLookUp / custom MultiSelectLookUp
        multiSelectList = []
        record = Record()
        record.add_key_value("id", 43234234423434)
        linkingRecord = Record()
        linkingRecord.add_key_value("MultiSelectLookup", record)
        multiSelectList.append(linkingRecord)
        record2 = Record()
        record2.add_key_value("id", 43234234423434)
        linkingRecord2 = Record()
        linkingRecord2.add_key_value("MultiSelectLookup", record2)
        multiSelectList.append(linkingRecord2)
        record1.add_key_value("MultiSelectlookup", multiSelectList)

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
        header_instance.add(CreateRecordsHeader.x_external, "Quotes.Quoted_Items.Product_Name.Products_External")
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


module = "Contacts"
UpdateContacts.initialize()
UpdateContacts.update_contacts(module)