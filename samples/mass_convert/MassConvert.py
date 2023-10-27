import datetime

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.mass_convert import MassConvertOperations, Convert, MoveAttachmentsTo, \
    RelatedModule, AssignTo, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.record import Record, Field
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class MassConvert(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def mass_convert():
        mass_convert_operations = MassConvertOperations()
        body_wrapper = Convert()
        body_wrapper.set_ids([440248001629121])
        deals = Record()
        deals.add_field_value(Field.Deals.amount(), 10.0)
        deals.add_field_value(Field.Deals.deal_name(), "V4SDK")
        deals.add_field_value(Field.Deals.closing_date(), datetime.date(2023, 10, 11))
        deals.add_field_value(Field.Deals.pipeline(), Choice("Standard (Standard)"))
        deals.add_field_value(Field.Deals.stage(), Choice("Closed Won"))
        body_wrapper.set_deals(deals)
        carry_over_tags = MoveAttachmentsTo()
        carry_over_tags.set_api_name("Deals")
        body_wrapper.set_carry_over_tags([carry_over_tags])
        related_modules = []
        related_module = RelatedModule()
        related_module.set_api_name("Tasks")
        related_module.set_id(440248001438054)
        related_modules.append(related_module)
        body_wrapper.set_related_modules(related_modules)
        assign_to = AssignTo()
        assign_to.set_id(4402480254001)
        body_wrapper.set_assign_to(assign_to)
        move_attachments_to = MoveAttachmentsTo()
        move_attachments_to.set_id(3445465609323)
        move_attachments_to.set_api_name("Contacts")
        # body_wrapper.set_move_attachments_to(move_attachments_to)
        response = mass_convert_operations.mass_convert(body_wrapper)
        if response is not None:
            print("Status Code: " + str(response.get_status_code()))
            action_handler = response.get_object()
            if isinstance(action_handler, SuccessResponse):
                print("Status: " + action_handler.get_status().get_value())
                print("Code: " + action_handler.get_code().get_value())
                print("Details")
                details = action_handler.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + action_handler.get_message())
            elif isinstance(action_handler, APIException):
                print("Status: " + action_handler.get_status().get_value())
                print("Code: " + action_handler.get_code().get_value())
                print("Details")
                details = action_handler.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + action_handler.get_message())


MassConvert.initialize()
MassConvert.mass_convert()