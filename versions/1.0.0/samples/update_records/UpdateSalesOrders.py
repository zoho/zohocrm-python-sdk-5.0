import datetime

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, BodyWrapper, Record, Field, Consent, FileDetails, \
    CreateRecordsHeader, APIException, SuccessResponse, ActionWrapper, LineItemProduct, LineTax
from zohocrmsdk.src.com.zoho.crm.api.tags import Tag
from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class UpdateSalesOrders(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_sales_orders(module):
        record_operations = RecordOperations()
        body_wrapper = BodyWrapper()
        records = []
        record1 = Record()
        record1.set_id(3342341231321)
        account = Record()
        account.add_field_value(Field.Accounts.id, 440248884001)
        record1.add_field_value(Field.Sales_Orders.account_name(), account)
        record1.add_field_value(Field.Sales_Orders.subject(), "new order")
        record1.add_field_value(Field.Sales_Orders.adjustment(), 10.0)
        record1.add_field_value(Field.Sales_Orders.description(), "description")
        record1.add_field_value(Field.Sales_Orders.terms_and_conditions(), "details of terms and conditions")
        record1.add_field_value(Field.Sales_Orders.customer_no(), "123212211")
        quoteName = Record()
        quoteName.add_field_value(Field.Quotes.id, 329202323121)
        record1.add_field_value(Field.Sales_Orders.quote_name(), quoteName)
        record1.add_field_value(Field.Sales_Orders.pending(), None)
        record1.add_field_value(Field.Sales_Orders.carrier(), Choice("FedEx"))
        record1.add_field_value(Field.Sales_Orders.sales_commission(), 40.0)
        record1.add_field_value(Field.Sales_Orders.purchase_order(), None)
        record1.add_field_value(Field.Sales_Orders.excise_duty(), 30.0)
        record1.add_field_value(Field.Sales_Orders.status(), Choice("Created"))
        deal_name = Record()
        deal_name.add_field_value(Field.Deals.id, 32124313234313)
        record1.add_field_value(Field.Sales_Orders.deal_name(), deal_name)
        contact_name = Record()
        contact_name.add_field_value(Field.Contacts.id, 323435332143342)
        record1.add_field_value(Field.Sales_Orders.contact_name(), contact_name)
        record1.add_field_value(Field.Sales_Orders.due_date(), datetime.date(2023, 12, 21))
        inventoryLineItemList = []
        inventoryLineItem = Record()
        lineItemProduct = LineItemProduct()
        lineItemProduct.set_id(4402480954344)
        data = Record()
        data.set_id(440248954344)
        inventoryLineItem.add_key_value("Description", "asd")
        inventoryLineItem.add_key_value("Discount", "5")
        inventoryLineItem.add_key_value("Quantity", 10.0)
        inventoryLineItem.add_key_value("List_Price", 100.0)
        inventoryLineItem.add_key_value("Product_Name", lineItemProduct)
        inventoryLineItem.add_key_value("Product_Category_1", "hardware")
        inventoryLineItemList.append(inventoryLineItem)
        productLineTaxes = []
        productLineTax = LineTax()
        productLineTax.set_name("Vat")
        productLineTax.set_value(10.0)
        productLineTax.set_id(4402480020810)
        productLineTax.set_percentage(10.0)
        productLineTaxes.append(productLineTax)
        inventoryLineItem.add_key_value("Line_Tax", productLineTaxes)
        inventoryLineItemList.append(inventoryLineItem)
        record1.add_field_value(Field.Sales_Orders.ordered_items(), inventoryLineItemList)
        lineTaxes = []
        lineTax = LineTax()
        lineTax.set_name("MyTax1134")
        lineTax.set_percentage(20.0)
        lineTaxes.append(lineTax)
        record1.add_key_value("$line_tax", lineTaxes)

        # Address info
        record1.add_field_value(Field.Sales_Orders.billing_city(), "city")
        record1.add_field_value(Field.Sales_Orders.billing_code(), "12345")
        record1.add_field_value(Field.Sales_Orders.billing_country(), "country")
        record1.add_field_value(Field.Sales_Orders.billing_state(), "state")
        record1.add_field_value(Field.Sales_Orders.billing_street(), "street")
        record1.add_field_value(Field.Sales_Orders.shipping_city(), "shipping city")
        record1.add_field_value(Field.Sales_Orders.shipping_code(), "shipping code")
        record1.add_field_value(Field.Sales_Orders.shipping_country(), "shipping country")
        record1.add_field_value(Field.Sales_Orders.shipping_state(), "shipping state")
        record1.add_field_value(Field.Sales_Orders.shipping_street(), "shipping street")

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


module = "Sales_Orders"
UpdateSalesOrders.initialize()
UpdateSalesOrders.update_sales_orders(module)