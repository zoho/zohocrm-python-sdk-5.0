from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.mail_merge import MailMergeOperations, MailMergeWrapper, APIException, \
    SuccessResponse, ActionWrapper, MailMerge, MailMergeTemplate
from zohocrmsdk.src.com.zoho.crm.api.mail_merge.address import Address


class SendMailMerge(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def send_mail_merge(module_api_name, id):
        mail_merge_operations = MailMergeOperations(module_api_name, id)
        request = MailMergeWrapper()
        send_mail_merge = []
        mail_merge = MailMerge()
        mail_merge_template = MailMergeTemplate()
        mail_merge_template.set_name("Test")
        mail_merge.set_mail_merge_template(mail_merge_template)
        mail_merge.set_attachment_name("testdocument")
        from_address = Address()
        from_address.set_value("abc@zoho.com")
        mail_merge.set_from_address(from_address)
        to_address = []
        address_value_map1 = Address()
        address_value_map1.set_value("abc@zoho.com")
        to_address.append(address_value_map1)
        mail_merge.set_to_address(to_address)
        cc_email = []
        address_value_map2 = Address()
        address_value_map2.set_value("abc2@zoho.com")
        cc_email.append(address_value_map2)
        mail_merge.set_cc_email(cc_email)
        bcc_email = []
        address_value_map2 = Address()
        address_value_map2.set_value("abc3@zoho.com")
        bcc_email.append(address_value_map2)
        mail_merge.set_bcc_email(bcc_email)
        mail_merge.set_subject("subject")
        mail_merge.set_message("ewsadsqdwd")
        mail_merge.set_type("attachment")
        send_mail_merge.append(mail_merge)
        request.set_send_mail_merge(send_mail_merge)
        response = mail_merge_operations.send_mail_merge(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_send_mail_merge()
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


SendMailMerge.initialize()
id = "347701"
module = "Leads"
SendMailMerge.send_mail_merge(module, id)
