from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.modules import Modules
from zohocrmsdk.src.com.zoho.crm.api.scoring_rules import ScoringRulesOperations, BodyWrapper, ScoringRule, Layout, \
    FieldRule, Criteria, Field, SignalRule, Signal, ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class CreateScoringRules(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_scoring_rules():
        scoring_rules_operations = ScoringRulesOperations()
        body_wrapper = BodyWrapper()
        scoring_rules = []
        scoring_rule = ScoringRule()
        scoring_rule.set_name("rule 10")
        scoring_rule.set_description("Rule for Module Leads")
        module = Modules()
        module.set_api_name("Leads")
        # module.set_id(33325234242423)
        scoring_rule.set_module(module)
        layout = Layout()
        layout.set_api_name("Standard")
        # layout.set_id(33423523435345)
        scoring_rule.set_layout(layout)
        scoring_rule.set_active(False)
        field_rules = []
        field_rule = FieldRule()
        field_rule.set_score(10)
        criteria = Criteria()
        criteria.set_group_operator("or")
        group = []
        criteria1 = Criteria()
        field1 = Field()
        field1.set_api_name("Company")
        criteria1.set_field(field1)
        criteria1.set_comparator("equal")
        criteria1.set_value("zoho")
        group.append(criteria1)
        # criteria2 = Criteria()
        # field2 = Field()
        # field2.set_api_name("Designation")
        # criteria2.set_field(field2)
        # criteria2.set_comparator("equal")
        # criteria2.set_value("review")
        # group.append(criteria2)
        criteria.set_group(group)
        field_rule.set_criteria(criteria)
        field_rules.append(field_rule)
        scoring_rule.set_field_rules(field_rules)
        # signal_rules = []
        # signal_rule = SignalRule()
        # signal_rule.set_id("3242331324132")
        # signal_rule.set_score(10)
        # signal = Signal()
        # signal.set_id(321423423422)
        # signal.set_namespace("Email_Incoming__s")
        # signal_rule.set_signal(signal)
        # signal_rules.append(signal_rule)
        # scoring_rule.set_signal_rules(scoring_rules)
        scoring_rules.append(scoring_rule)
        body_wrapper.set_scoring_rules(scoring_rules)
        response = scoring_rules_operations.create_scoring_rules(body_wrapper)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_scoring_rules()
                    for action_response in action_response_list:
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

                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


CreateScoringRules.initialize()
CreateScoringRules.create_scoring_rules()
