from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.email_templates import EmailTemplatesOperations, ResponseWrapper, APIException


class GetEmailTemplateById:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_email_template_by_id(id):
        """
        This method is used to get  email_templates' details with ID and print the response.
        """
        email_templates_operations = EmailTemplatesOperations()
        response = email_templates_operations.get_email_template(id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    email_templates_list = response_object.get_email_templates()
                    for email_template in email_templates_list:
                        print(" ID " + str(email_template.get_id()))
                        print("Name: " + str(email_template.get_name()))
                        print("description: " + str(email_template.get_description()))
                        print("Modified Time: " + str(email_template.get_modified_time()))
                        print("Created Time: " + str(email_template.get_created_time()))
                        print("Subject: " + str(email_template.get_subject()))
                        print("Type: " + str(email_template.get_type()))
                        print("Last Usage Time: " + str(email_template.get_last_usage_time()))
                        print("Consent Linked: " + str(email_template.get_consent_linked()))
                        print("Associated: " + str(email_template.get_associated()))
                        print("Content: " + str(email_template.get_content()))
                        print("EditorMode: " + str(email_template.get_editor_mode()))
                        created_by = email_template.get_created_by()
                        if created_by is not None:
                            print("Created By - Name: " + created_by.get_name())
                            print("Created By - ID: " + str(created_by.get_id()))
                            print("Created By - email: " + str(created_by.get_email()))
                        folder = email_template.get_folder()
                        if folder is not None:
                            print("EmailTemplate folder ID: " + folder.get_name())
                            print("EmailTemplate folder Name:" + str(folder.get_id()))
                        # get module
                        module = email_template.get_module()
                        if module is not None:
                            print("Module - API Name: " + module.get_api_name())
                            print("Module - ID: " + str(module.get_id()))
                        # get attachments
                        attachments = email_template.get_attachments()
                        if attachments is not None:
                            for attachment in attachments:
                                print("EmailTemplate Attachment File ID: " + attachment.get_file_id)
                                print("EmailTemplate Attachment File Name: " + attachment.get_file_name)
                                print("EmailTemplate Attachment File Size: " + attachment.get_size)
                                print("EmailTemplate Attachment File ID: " + attachment.get_id)
                        modified_by = email_template.get_modified_by()
                        if modified_by is not None:
                            print("Modified By - Name: " + modified_by.get_name())
                            print("Modified By - ID: " + str(modified_by.get_id()))
                            print("Modified By - ID: " + str(modified_by.get_email()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    if details is not None:
                        if details is not None:
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


GetEmailTemplateById.initialize()
GetEmailTemplateById.get_email_template_by_id(4402480627040)