from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.assignment_rules import *
from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class GetAssignmentRule:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_assignment_rule(rule_id):
        """
        This method is used to get  assignment_rules' details with ID and print the response.
        """
        assignment_rules_operations = AssignmentRulesOperations()
        param_instance = ParameterMap()
        param_instance.add(GetAssignmentRuleParam.module, "Leads")
        # Call get_assignment_rules method that takes ParameterMap instance as parameter
        response = assignment_rules_operations.get_assignment_rule(
            rule_id, param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code()
                                      == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    assignment_rules_list = response_object.get_assignment_rules()
                    for assignment_rule in assignment_rules_list:
                        print("Name: " + str(assignment_rule.get_name()))
                        print("description: " +
                              str(assignment_rule.get_description()))
                        print("Modified Time: " +
                              str(assignment_rule.get_modified_time()))
                        print("Created Time: " +
                              str(assignment_rule.get_created_time()))
                        created_by = assignment_rule.get_created_by()
                        if created_by is not None:
                            print("Created By - Name: " +
                                  created_by.get_name())
                            print("Created By - ID: " +
                                  str(created_by.get_id()))
                            print("Created By - email: " +
                                  str(created_by.get_email()))
                        default_assignee = assignment_rule.get_default_assignee()
                        if default_assignee is not None:
                            print("Created By - Name: " +
                                  default_assignee.get_name())
                            print("Created By - ID: " +
                                  str(default_assignee.get_id()))
                        module = assignment_rule.get_module()
                        if module is not None:
                            print("Module - API Name: " +
                                  module.get_api_name())
                            print("Module - ID: " + str(module.get_id()))
                        modified_by = assignment_rule.get_modified_by()
                        if modified_by is not None:
                            print("Modified By - Name: " +
                                  modified_by.get_name())
                            print("Modified By - ID: " +
                                  str(modified_by.get_id()))
                            print("Modified By - ID: " +
                                  str(modified_by.get_email()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    if details is not None:
                        if details is not None:
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


GetAssignmentRule.initialize()
GetAssignmentRule.get_assignment_rule(440248001305001)
