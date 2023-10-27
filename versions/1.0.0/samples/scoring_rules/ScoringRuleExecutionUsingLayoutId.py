from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.scoring_rules import ScoringRulesOperations, LayoutRequestWrapper, Layout, \
    ActionWrapper, SuccessResponse, APIException


class ScoringRuleExecutionUsingLayoutId(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def scoring_rule_execution_layout_id(module_api_name):
        scoring_rules_operation = ScoringRulesOperations()
        body_wrapper = LayoutRequestWrapper()
        layout = Layout()
        layout.set_id(4402480167)
        body_wrapper.set_layout(layout)
        response = scoring_rules_operation.scoring_rule_execution_using_layout_id(module_api_name, body_wrapper)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            action_response = response.get_object()
            if action_response is not None:
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

                elif isinstance(action_response, APIException):
                    print("Status: " + action_response.get_status().get_value())
                    print("Code: " + action_response.get_code().get_value())
                    print("Details")
                    details = action_response.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + action_response.get_message().get_value())


module_api_name = "Leads"
ScoringRuleExecutionUsingLayoutId.initialize()
ScoringRuleExecutionUsingLayoutId.scoring_rule_execution_layout_id(module_api_name)