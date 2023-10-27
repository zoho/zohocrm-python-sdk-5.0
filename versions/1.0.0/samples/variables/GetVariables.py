from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.variables import APIException, ResponseWrapper, GetVariablesParam, \
    VariablesOperations


class GetVariables:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_variables():
        """
        This method is used to retrieve all the available variables through an API request and print the response.
        """
        variables_operations = VariablesOperations()
        param_instance = ParameterMap()
        # Possible parameters of Get Variables operation
        param_instance.add(GetVariablesParam.group, 'General')
        # Call get_variables method that takes ParameterMap instance as parameter
        response = variables_operations.get_variables(param_instance)
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


GetVariables.initialize()
GetVariables.get_variables()
