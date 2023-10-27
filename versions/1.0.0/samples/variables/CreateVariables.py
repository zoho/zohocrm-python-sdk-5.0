from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.util import Choice
from zohocrmsdk.src.com.zoho.crm.api.variables import VariablesOperations, BodyWrapper, Variable, VariableGroup, \
    ActionWrapper, SuccessResponse, APIException


class CreateVariables:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_variables():
        """
        This method is used to create variables and print the response.
        """
        variables_operations = VariablesOperations()
        request = BodyWrapper()
        # List to hold Variable instances
        variable_list = []
        variable_1 = Variable()
        variable_1.set_api_name('Variable1234')
        variable_1.set_name('Variable1234')
        variable_group = VariableGroup()
        variable_group.set_id(4402480345005)
        variable_1.set_variable_group(variable_group)
        variable_1.set_type(Choice('integer'))
        variable_1.set_value('55')
        variable_1.set_description('This denotes variable 5 description')
        # Add the variable instance to the array
        variable_list.append(variable_1)
        variable_2 = Variable()
        variable_2.set_api_name('Variablenew1')
        variable_2.set_name('Variablenew1')
        variable_group = VariableGroup()
        variable_group.set_id(3409643002275023)
        variable_group.set_name("New VG")
        variable_2.set_variable_group(variable_group)
        variable_2.set_type(Choice('text'))
        variable_2.set_value('Python')
        variable_2.set_description('This denotes variable 5 description')
        # Add the variable instance to the array
        variable_list.append(variable_2)
        request.set_variables(variable_list)
        # Call create_variables method that takes BodyWrapper instance as parameter
        response = variables_operations.createvariable(request)
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


CreateVariables.initialize()
CreateVariables.create_variables()
