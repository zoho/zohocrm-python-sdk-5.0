from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.share_records import ShareRecordsOperations, BodyWrapper, ShareRecord, \
    ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.users import Users
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class UpdateSharePermissions:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_share_permissions(module_api_name, record_id):
        """
        This method is used to update the sharing permissions of a record granted to users as Read-Write, Read-only, or grant full access.
        :param module_api_name: The API Name of the module to update share permissions.
        :param record_id: The ID of the record
        """
        """
        example
        module_api_name = Contacts
        record_id = 3409643002112011
        """
        shared_records_operations = ShareRecordsOperations(record_id, module_api_name)
        request = BodyWrapper()
        share_record_list = []
        share_record = ShareRecord()
        share_record.set_share_related_records(True)
        share_record.set_permission(Choice('full_access'))
        user = Users()
        user.set_id(3477061005791024)
        share_record.set_user(user)
        share_record_list.append(share_record)
        request.set_share(share_record_list)
        # Call update_share_permissions method that takes BodyWrapper instance as parameter
        response = shared_records_operations.update_share_permissions(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_share()
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


UpdateSharePermissions.initialize()
UpdateSharePermissions.update_share_permissions(module_api_name="Leads", record_id=3342342123123)