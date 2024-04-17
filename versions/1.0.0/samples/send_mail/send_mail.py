from datetime import datetime

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.email_templates import EmailTemplate
from zohocrmsdk.src.com.zoho.crm.api.send_mail import SendMailOperations, BodyWrapper, Data, From, To, Attachment, \
    APIException, SuccessResponse, ActionWrapper, InventoryDetails, InventoryTemplate
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class SendMail(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def send_mail(record_id, module_api_name):
        """
        This method is used to   send_mail'

        """
        # Get instance of SendMailOperations Class
        send_mail_operations = SendMailOperations(record_id, module_api_name)

        request = BodyWrapper()
        mail = Data()
        user_address_from = From()
        user_address_to = To()
        user_address_cc = To()
        user_address_bcc = To()
        user_address_reply_to = To()
        attachment = Attachment()
        attachment.set_id("2cceafa194d037b63f20181dd81864b4812b1f8b0b4fe0949a982de89fa75a")
        template = EmailTemplate()
        template.set_id(4402480258279)
        user_address_from.set_user_name("username")
        user_address_from.set_email("abc@zoho.com")
        user_address_to.set_user_name("username1")
        user_address_to.set_email("abc1@zoho.com")
        user_address_cc.set_user_name("Jasweon Smith")
        user_address_cc.set_email("abc2@zoho.com")
        user_address_bcc.set_user_name("Jassdon Smith")
        user_address_bcc.set_email("abc3@zoho.com")
        user_address_reply_to.set_user_name("Jassdon Smith")
        user_address_reply_to.set_email("abc4@zoho.com")
        mail.set_from(user_address_from)
        mail.set_to([user_address_to])
        mail.set_bcc([user_address_bcc])
        mail.set_cc([user_address_cc])
        mail.set_reply_to(user_address_reply_to)
        mail.set_org_email(False)
        mail.set_in_reply_to("2cceafa194d037b63f20181dd8186486f1eb0360aee76d802b6d376dea97e7")
        mail.set_scheduled_time(datetime(2023, 8, 30, 1, 42, 10))
        mail.set_subject("Testing Send Mail API")
        mail.set_content("<h3><span style=\"background-color: rgb(254, 255, 102)\">Mail is of rich text format</span></h3><h3><span style=\"background-color: rgb(254, 255, 102)\"><img src=\"https://www.zohoapis.com/crm/viewInLineImage?fileContent=2cceafa194d037b63f20181dd818646fd5e5167a274098b625c35654a20ed2\"></span></h3><h3><span style=\"background-color: rgb(254, 255, 102)\">REGARDS,</span></h3><div><span style=\"background-color: rgb(254, 255, 102)\">AZ</span></div><div><span style=\"background-color: rgb(254, 255, 102)\">ADMIN</span></div> <div></div>")
        mail.set_mail_format(Choice("html"))
        mail.set_attachments([attachment])
        mail.set_template(template)
        template = InventoryTemplate()
        template.set_id(4402480258279)

        # To send an Email for inventory modules - include inventory details
        inventory_details = InventoryDetails()
        inventory_details.set_inventory_template(template)
        mail.set_inventory_details(inventory_details)
        #
        request.set_data([mail])
        response = send_mail_operations.send_mail(request)
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
                            print("Message: " + action_response.get_message())
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


SendMail.initialize()
SendMail.send_mail(record_id=440248001575053, module_api_name="Quotes")
