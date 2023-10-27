from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.variables import VariablesOperations, GetVariableByAPINameParam, ResponseWrapper, \
    APIException

class GetVariableForAPIName:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_variable_for_api_name(variable_api_name):
        """
        This method is used to get the details of any specific variable with API Name
        :param variable_api_name: The API name of the Variable to be obtained
        """
        """
        example
        variable_api_name = 'Variable55'
        """
        variables_operations = VariablesOperations()
        param_instance = ParameterMap()
        # Possible parameters of Get Variable For API Name operation
        param_instance.add(GetVariableByAPINameParam.group, '4402480345005')
        # Call get_variable_for_api_name method that takes ParameterMap instance and variable_api_name as parameters
        response = variables_operations.get_variable_by_apiname(variable_api_name, param_instance)
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


variable_api_name = "new"
GetVariableForAPIName.initialize()
GetVariableForAPIName.get_variable_for_api_name(variable_api_name)
