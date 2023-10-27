from datetime import date

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, ConvertBodyWrapper, LeadConverter, Record, Field, \
    ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.tags import Tag
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class ConvertLead:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def convert_lead(lead_id):
        """
        This method is used to Convert a Lead record and print the response.
        :param lead_id: The ID of the Lead to be converted.
        """
        """
        example
        lead_id = 3409643002034003
        """
        record_operations = RecordOperations()
        request = ConvertBodyWrapper()
        # List to hold LeadConverter instances
        data = []
        record = LeadConverter()
        record.set_overwrite(True)
        record.set_notify_lead_owner(True)
        record.set_notify_new_entity_owner(True)
        record.set_accounts('34096430692007')
        record.set_contacts('34096430836001')
        record.set_assign_to('34096430302031')
        deals = Record()
        """
        Call add_field_value method that takes two arguments
        Import the zcrmsdk.src.com.zoho.crm.api.record.field file
        1 -> Call Field "." and choose the module from the displayed list and press "." and choose the field name from the displayed list.
        2 -> Value
        """
        deals.add_field_value(Field.Deals.deal_name(), 'deal_name')
        deals.add_field_value(Field.Deals.description(), "deals description")
        deals.add_field_value(Field.Deals.closing_date(), date(2020, 10, 2))
        deals.add_field_value(Field.Deals.stage(), Choice("Closed Won"))
        deals.add_field_value(Field.Deals.amount(), 500.78)
        """
        Call add_key_value method that takes two arguments
        1 -> A string that is the Field's API Name
        2 -> Value
        """
        deals.add_key_value('Custom_field', 'Value')
        tag_list = []
        tag = Tag()
        tag.set_name('Converted')
        tag_list.append(tag)
        deals.set_tag(tag_list)
        record.set_deals(deals)
        data.append(record)
        request.set_data(data)
        # Call convertLead method that takes ConvertBodyWrapper instance and lead_id as parameter
        response = record_operations.convert_lead(lead_id, request)
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


lead_id = 440248001507154
ConvertLead.initialize()
ConvertLead.convert_lead(lead_id)
