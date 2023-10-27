from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.contact_roles import ContactRolesOperations, BodyWrapper, ContactRole, \
    ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class UpdateContactRole(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_contact_role(contact_role_id):
        """
        This method is used to update single Contact Role with ID and print the response.
        :param contact_role_id: The ID of the ContactRole to be updated
        """
        """
        example
        contact_role_id = 3409643002212003
        """
        contact_roles_operations = ContactRolesOperations()
        request = BodyWrapper()
        # List to hold ContactRole instances
        contact_roles_list = []
        cr_1 = ContactRole()
        cr_1.set_name("Edited1")
        contact_roles_list.append(cr_1)
        request.set_contact_roles(contact_roles_list)
        # Call update_contact_role method that takes BodyWrapper instance and contact_role_id as parameters
        response = contact_roles_operations.update_role(contact_role_id, request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_contact_roles()
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


UpdateContactRole.initialize()
UpdateContactRole.update_contact_role(contact_role_id=4402480020551)
