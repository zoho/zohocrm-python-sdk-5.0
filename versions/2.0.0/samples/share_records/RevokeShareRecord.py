from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.share_records import ShareRecordsOperations, DeleteActionWrapper, SuccessResponse, \
    APIException


class RevokeShareRecord:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)
        
    @staticmethod
    def revoke_shared_record(module_api_name, record_id):
        """
        This method is used to revoke access to a shared record that was shared to users and print the response.
        :param module_api_name: The API Name of the module to revoke shared record.
        :param record_id: The ID of the record
        """
        """
        example
        module_api_name = Contacts
        record_id = 3409643002112011
        """
        shared_records_operations = ShareRecordsOperations(record_id, module_api_name)
        # Call revoke_shared_record method
        response = shared_records_operations.revoke_shared_record()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, DeleteActionWrapper):
                    action_response = response_object.get_share()
                    if isinstance(action_response, SuccessResponse):
                        print("Status: " + action_response.get_status().get_value())
                        print("Code: " + action_response.get_code().get_value())
                        print("Details")
                        details = action_response.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + action_response.get_message().get_value())
                    elif isinstance(action_response, APIException):
                        print("Status: " + action_response.get_status().get_value())
                        print("Code: " + action_response.get_code().get_value())
                        print("Details")
                        details = action_response.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + action_response.get_message().get_value())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


RevokeShareRecord.initialize()
RevokeShareRecord.revoke_shared_record(module_api_name="Leads", record_id=440248001483007)