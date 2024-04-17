from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.mail_merge import MailMergeOperations, APIException, \
    SuccessResponse, MailMergeTemplate, SignMailMergeWrapper, SignMailMerge, Signers, \
    SignActionWrapper
from zohocrmsdk.src.com.zoho.crm.api.mail_merge.address import Address
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class SignmailMerge(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def sign_mail_merge(module_api_name, id):
        mail_merge_operations = MailMergeOperations(module_api_name, id)
        request = SignMailMergeWrapper()
        sign_mail_merge = []
        mail_merge = SignMailMerge()
        mail_merge_template = MailMergeTemplate()
        mail_merge_template.set_name("Test")
        mail_merge.set_mail_merge_template(mail_merge_template)
        mail_merge.set_file_name("testfile")
        mail_merge.set_sign_in_order(True)
        signers = []
        signer = Signers()
        signer.set_action_type(Choice("sign"))
        recipient = Address()
        recipient.set_value("abc@zoho.com")
        signer.set_recipient(recipient)
        signers.append(signer)
        mail_merge.set_signers(signers)
        sign_mail_merge.append(mail_merge)
        request.set_sign_mail_merge(sign_mail_merge)
        response = mail_merge_operations.sign_mail_merge(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, SignActionWrapper):
                    action_response_list = response_object.get_sign_mail_merge()
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


SignmailMerge.initialize()
id = "347502001"
module = "Leads"
SignmailMerge.sign_mail_merge(module, id)
