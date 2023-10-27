from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.variable_groups import VariableGroupsOperations, ResponseWrapper, APIException


class GetVariableGroupById:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_variable_group_by_id(variable_group_id):
        """
        This method is used to get the details of any variable group with group id and print the response.
        :param variable_group_id: The ID of the VariableGroup to be obtained
        """
        """
        example
        variable_group_id = 3409643002275023
        """
        variable_groups_operations = VariableGroupsOperations()
        # Call get_variable_group_by_id method that takes variable_group_id as parameter
        response = variable_groups_operations.get_variable_group_by_id(variable_group_id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    variablegroup_list = response_object.get_variable_groups()
                    for variable_group in variablegroup_list:
                        print("VariableGroup DisplayLabel: " + str(variable_group.get_display_label()))
                        print("VariableGroup APIName: " + str(variable_group.get_api_name()))
                        print("VariableGroup Name: " + str(variable_group.get_name()))
                        print("VariableGroup Description: " + str(variable_group.get_description()))
                        print("VariableGroup ID: " + str(variable_group.get_id()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


GetVariableGroupById.initialize()
GetVariableGroupById.get_variable_group_by_id("4402400345005")