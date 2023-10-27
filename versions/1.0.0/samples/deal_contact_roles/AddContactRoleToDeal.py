from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.deal_contact_roles import DealContactRolesOperations, BodyWrapper, ContactRole, \
    Data, ActionWrapper, SuccessResponse, APIException


class AddContactRoleToDeal(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def add_contact_role_to_deal(contact_id, deal_id):
        contact_roles_operations = DealContactRolesOperations()
        body_wrapper = BodyWrapper()
        data = []
        data1 = Data()
        contact_role = ContactRole()
        contact_role.set_id(4402480388001)
        contact_role.set_name("contactRole1")
        data1.set_contact_role(contact_role)
        data.append(data1)
        body_wrapper.set_data(data)
        response = contact_roles_operations.associate_contact_role_to_deal(contact_id, deal_id, body_wrapper)
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


deal_id = 440248001393069
contact_id = 440248001393062
AddContactRoleToDeal.initialize()
AddContactRoleToDeal.add_contact_role_to_deal(contact_id, deal_id)