from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.associate_email import AssociateEmailOperations, BodyWrapper, AssociateEmail, From, \
    To, Attachments, ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
import datetime

from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class Associate(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def associate(recordId, module):
        associate_email_operations = AssociateEmailOperations()
        request = BodyWrapper()
        emails = list()
        for i in range(1):
            associate_email = AssociateEmail()
            from1 = From()
            from1.set_email('abc@zoho.com')
            from1.set_user_name("username")
            associate_email.set_from(from1)
            tos = []
            to = To()
            to.set_email('abc1@zoho.com')
            to.set_user_name("username1")
            tos.append(to)
            tos1 = []
            to1 = To()
            to1.set_email("abc2@zoho.com")
            to1.set_user_name("user_name1")
            tos1.append(to1)
            tos2 = []
            to2 = To()
            to2.set_email("abc3@zoho.com")
            to2.set_user_name("user_name2")
            tos2.append(to2)
            associate_email.set_to(tos)
            associate_email.set_cc(tos1)
            associate_email.set_bcc(tos2)
            associate_email.set_subject("Subject")
            associate_email.set_original_message_id("c6085fae06cbd7b750eb925d5797d1a5554f0ab7a158661d")
            associate_email.set_date_time(datetime.datetime.now())
            associate_email.set_sent(True)
            associate_email.set_content("<h3><span style=\\\"background-color: rgb(254, 255, 102)\\\">Mail is of rich text format</span></h3><h3><span style=\\\"background-color: rgb(254, 255, 102)\\\">REGARDS,</span></h3><div><span style=\\\"background-color: rgb(254, 255, 102)\\\">AZ</span></div><div><span style=\\\"background-color: rgb(254, 255, 102)\\\">ADMIN</span></div> <div></div>")
            associate_email.set_mail_format(Choice("html"))
            attachments = []
            attachment = Attachments()
            attachment.set_id("c6085fae06cbd7b75001d806b54e30b905c6e1efa82c6")
            attachments.append(attachment)
            associate_email.set_attachments(attachments)
            emails.append(associate_email)
        request.set_emails(emails)
        response = associate_email_operations.associate(recordId, module, request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_emails()
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


recordId = 440248001409007
module = "Leads"
Associate.initialize()
Associate.associate(recordId=recordId, module=module)