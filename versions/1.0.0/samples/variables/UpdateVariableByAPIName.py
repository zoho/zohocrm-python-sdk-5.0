from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.variables import VariablesOperations, BodyWrapper, Variable, ActionWrapper, \
    SuccessResponse, APIException


class UpdateVariableByAPIName:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_variable_by_api_name(variable_api_name):
        """
        This method is used to update details of a specific variable in CRM with API Name and print the response.
        :param variable_api_name: The API name of the Variable to be updated
        """
        """
        example
        variable_api_name = 'Variable55'
        """
        variables_operations = VariablesOperations()
        request = BodyWrapper()
        # List to hold Variable instances
        variable_list = []
        variable_1 = Variable()
        variable_1.set_value('98')
        variable_1.set_api_name('Edited-variable55')
        # Add the variable instance to the array
        variable_list.append(variable_1)
        request.set_variables(variable_list)
        # Call update_variable_by_api_name method that takes BodyWrapper instance and variable_api_name as parameters
        response = variables_operations.update_variable_by_apiname(variable_api_name, request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_variables()
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


UpdateVariableByAPIName.initialize()
UpdateVariableByAPIName.update_variable_by_api_name("variable1234")
