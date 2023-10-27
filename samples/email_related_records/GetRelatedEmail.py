from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.email_related_records import EmailRelatedRecordsOperations, ResponseWrapper, \
    APIException


class GetRelatedEmail(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_related_email(module_api_name, id, message_id):
        email_template_operations = EmailRelatedRecordsOperations(id, module_api_name)
        response = email_template_operations.get_emails_related_record(message_id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                response_wrapper = response_object
                email_templates = response_wrapper.get_emails()
                for email_template in email_templates:
                    user_details = email_template.get_cc()
                    if user_details is not None:
                        for user_detail in user_details:
                            print("EmailRelatedRecords User Email:  "+ user_detail.get_email())
                            print("EmailRelatedRecords User Name:  " + user_detail.get_user_name())
                    print("EmailRelatedRecords Summary : " + str(email_template.get_summary()))
                    owner = email_template.get_owner()
                    if owner is not None:
                        print("EmailRelatedRecords User ID: "+ owner.get_id())
                        print("EmailRelatedRecords User Name: " + owner.get_name())
                    print("EmailRelatedRecords Read : " + str(email_template.get_read()))
                    print("EmailRelatedRecords Sent: " + str(email_template.get_sent()))
                    print("EmailRelatedRecords Subject: " + email_template.get_subject())
                    print("EmailRelatedRecords Intent: " + str(email_template.get_intent()))
                    print("EmailRelatedRecords SentimentInfo: " + str(email_template.get_sentiment_info()))
                    print("EmailRelatedRecords Source: " + str(email_template.get_source()))
                    linked_record = email_template.get_linked_record()
                    if linked_record is not None:
                        print("EmailRelatedRecords LinkedRecord id : " + str(linked_record.get_id()))
                        module = linked_record.get_module()
                        if module is not None:
                            print("EmailRelatedRecords LinkedRecord Module APIName : " + module.get_api_name())
                            print("EmailRelatedRecords LinkedRecord Module Id : " + module.get_id())
                    print("EmailRelatedRecords Emotion : " + str(email_template.get_emotion()))
                    from1 = email_template.get_from()
                    if from1 is not None:
                        print("EmailRelatedRecords from user Email: " + from1.get_email())
                        print("EmailRelatedRecords from user Name: " + str(from1.get_user_name()))
                    to_user_details = email_template.get_to()
                    if to_user_details is not None:
                        for user_detail in to_user_details:
                            print("EmailRelatedRecords from user Email: " + user_detail.get_email())
                            print("EmailRelatedRecords from user Name: " + str(user_detail.get_user_name()))
                    print("EmailRelatedRecords Time : " + str(email_template.get_time()))
                    status = email_template.get_status()
                    if status is not None:
                        for status1 in status:
                            print("EmailRelatedRecords Status Type: " + status1.get_type())
                            print("EmailRelatedRecords Status BouncedTime: " + status1.get_bounced_time())
                            print("EmailRelatedRecords Status BouncedReason: " + status1.get_bounced_reason())
                info = response_wrapper.get_info()
                if info is not None:
                    if info.get_per_page() is not None:
                        print("Record Info PerPage: " + str(info.get_per_page()))
                    if info.get_next_index() is not None:
                        print("Record Info nextIndex: " + str(info.get_next_index()))
                    if info.get_count() is not None:
                        print("Record Info Count: " + str(info.get_count()))
                    if info.get_prev_index() is not None:
                        print("Record Info prevIndex: " + str(info.get_prev_index()))
                    if info.get_more_records() is not None:
                        print("Record Info MoreRecords: " + str(info.get_more_records()))

            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message().get_value())


module_api_name = "Leads"
id1 = 4402480774074
message_id = "c6085fae06cbd7b75001d80ffefabb4aec0de7e69721f2750ec4eb616"
GetRelatedEmail.initialize()
GetRelatedEmail.get_related_email(module_api_name, id1, message_id)
