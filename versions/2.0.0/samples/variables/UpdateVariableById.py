from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.variables import VariablesOperations, BodyWrapper, Variable, ActionWrapper, \
    SuccessResponse, APIException


class UpdateVariableById:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_variable_by_id(variable_id):
        """
        This method is used to update details of a specific variable in CRM and print the response.
        :param variable_id: The ID of the Variable to be updated
        :return:
        """
        """
        example
        variable_id = 3409643002275025
        """
        variables_operations = VariablesOperations()
        request = BodyWrapper()
        # List to hold Variable instances
        variable_list = []
        variable_1 = Variable()
        variable_1.set_value('98')
        # Add the variable instance to the array
        variable_list.append(variable_1)
        request.set_variables(variable_list)
        # Call update_variable_by_id method that takes BodyWrapper instance and variable_id as parameters
        response = variables_operations.update_variable_by_id(variable_id, request)
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


UpdateVariableById.initialize()
UpdateVariableById.update_variable_by_id(32324234234)
