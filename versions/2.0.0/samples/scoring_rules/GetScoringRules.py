from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.scoring_rules import ScoringRulesOperations, GetScoringRulesParam, ResponseWrapper, \
    APIException


class GetScoringRules(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_scoring_rules():
        scoring_rules_operations = ScoringRulesOperations()
        param_instance = ParameterMap()
        param_instance.add(GetScoringRulesParam.module, "Leads")
        response = scoring_rules_operations.get_scoring_rules(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                response_wrapper = response_object
                scoring_rules = response_wrapper.get_scoring_rules()
                for scoring_rule in scoring_rules:
                    layout = scoring_rule.get_layout()
                    if layout is not None:
                        print("scoring_rule Layout Id: " + str(layout.get_id()))
                        print("scoring_rule Layout APIName :" + str(layout.get_api_name()))
                    print("scoring_rule CreatedTime: " + str(scoring_rule.get_created_time()))
                    print("scoring_rule ModifiedTime: " + str(scoring_rule.get_modified_time()))
                    fieldRules = scoring_rule.get_field_rules()
                    for fieldRule in fieldRules:
                        print("scoring_rule FieldRule Score: " + str(fieldRule.get_score()))
                        criteria = fieldRule.get_criteria()
                        if criteria is not None:
                            GetScoringRules.print_criteria(criteria)
                        print("scoring_rule FieldRule Id: " + str(fieldRule.get_id()))
                    module = scoring_rule.get_module()
                    if module is not None:
                        print("scoring_rule Module ID: " + str(module.get_id()))
                        print("scoring_rule Module APIName: " + module.get_api_name())
                    print("scoring_rule Name: " + scoring_rule.get_name())
                    modifiedBy = scoring_rule.get_modified_by()
                    if modifiedBy is not None:
                        print("scoring_rule Modified By Name : " + modifiedBy.get_name())
                        print("scoring_rule Modified By id : " + str(modifiedBy.get_id()))
                    print("scoring_rule Active: " + str(scoring_rule.get_active()))
                    print("scoring_rule Description: " + str(scoring_rule.get_description()))
                    print("scoring_rule Id: " + str(scoring_rule.get_id()))
                    signalRules = scoring_rule.get_signal_rules()
                    if signalRules is not None:
                        for signalRule in signalRules:
                            print("scoring_rule SignalRule Score: " + signalRule.get_score())
                            print("scoring_rule SignalRule Id: " + str(signalRule.get_id()))
                            signal = signalRule.get_signal()
                            if signal is not None:
                                print("scoring_rule SignalRule Signal Namespace: " + signal.get_namespace())
                                print("scoring_rule SignalRule Signal Id: " + signal.get_id())
                    createdBy = scoring_rule.get_created_by()
                    if createdBy is not None:
                        print("scoring_rule Created By Name : " + createdBy.get_name())
                        print("scoring_rule Created By id : " + str(createdBy.get_id()))
                info = response_wrapper.get_info()
                if info is not None:
                    if info.get_per_page() is not None:
                        print("Info PerPage: " + str(info.get_per_page()))
                    if info.get_count() is not None:
                        print("Info Count: " + str(info.get_count()))
                    if info.get_page() is not None:
                        print("Info Page: " + str(info.get_page()))
                    if info.get_more_records() is not None:
                        print("Info MoreRecords: " + str(info.get_more_records()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message().get_value())

    @staticmethod
    def print_criteria(criteria):
        if criteria.get_comparator() is not None:
            print("CustomView Criteria Comparator: " + criteria.get_comparator())
        if criteria.get_field() is not None:
            print("CustomView Criteria field name: " + criteria.get_field().get_api_name())
        if criteria.get_value() is not None:
            print("CustomView Criteria Value: " + str(criteria.get_value()))
        criteriaGroup = criteria.get_group()
        if criteriaGroup is not None:
            for criteria1 in criteriaGroup:
                GetScoringRules.print_criteria(criteria1)
        if criteria.get_group_operator() is not None:
            print("CustomView Criteria Group Operator: " + criteria.get_group_operator())


GetScoringRules.initialize()
GetScoringRules.get_scoring_rules()