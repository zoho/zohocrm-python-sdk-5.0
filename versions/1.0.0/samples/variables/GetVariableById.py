from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.variables import VariablesOperations, GetVariableByIDParam, ResponseWrapper, \
    APIException


class GetVariableById:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_variable_by_id(variable_id):
        """
        This method is used to get the details of any specific variable with ID and print the response
        :param variable_id: The ID of the Variable to be obtained
        """
        """
        example
        variable_id = 3409643002275025
        """
        variables_operations = VariablesOperations()
        param_instance = ParameterMap()
        # Possible parameters of Get Variable By ID operation
        param_instance.add(GetVariableByIDParam.group, '4402480345005')
        # Call get_variable_by_id method that takes ParameterMap instance and variable_id as parameters
        response = variables_operations.get_variable_by_id(variable_id, param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    variable_list = response_object.get_variables()
                    for variable in variable_list:
                        print("Variable ID: " + str(variable.get_id()))
                        print("Variable APIName: " + variable.get_api_name())
                        print("Variable Name: " + variable.get_name())
                        print("Variable Description: " + variable.get_description())
                        print("Variable Type: " + str(variable.get_type()))
                        variable_group = variable.get_variable_group()
                        if variable_group is not None:
                            print("Variable VariableGroup APIName: " + variable_group.get_api_name())
                            print("Variable VariableGroup ID: " + str(variable_group.get_id()))
                        print("Variable Value: " + variable.get_value())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


id = 440248001501020
GetVariableById.initialize()
GetVariableById.get_variable_by_id(id)
