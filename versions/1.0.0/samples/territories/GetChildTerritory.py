from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.territories import TerritoriesOperations, ResponseWrapper, APIException


class GetChildTerritory(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_child_territory(id):
        territories_operations = TerritoriesOperations()
        param_instance = ParameterMap()
        response = territories_operations.get_child_territory(id, param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                territory_list = response_object.get_territories()
                for territory in territory_list:
                    print("Territory CreatedTime: " + str(territory.get_created_time()))
                    if territory.get_modified_time() is not None:
                        print("Territory ModifiedTime: " + str(territory.get_modified_time()))
                    manager = territory.get_manager()
                    deal_rule_criteria = territory.get_deal_rule_criteria()
                    if deal_rule_criteria is not None:
                        GetChildTerritory.print_criteria(deal_rule_criteria)
                    accounts_rule_criteria = territory.get_account_rule_criteria()
                    if accounts_rule_criteria is not None:
                        GetChildTerritory.print_criteria(accounts_rule_criteria)
                    print("Territory Name: " + str(territory.get_name()))
                    modified_by = territory.get_modified_by()
                    if modified_by is not None:
                        print("Territory Modified By User-Name: " + modified_by.get_name())
                        print("Territory Modified By User-ID: " + str(modified_by.get_id()))
                    print("Territory Description: " + str(territory.get_description()))
                    print("Territory permission type: " + str(territory.get_permission_type()))
                    print("Territory ID: " + str(territory.get_id()))
                    created_by = territory.get_created_by()
                    if created_by is not None:
                        print("Territory Created By User-Name: " + created_by.get_name())
                        print("Territory Created By User-ID: " + str(created_by.get_id()))
                    info = response_object.get_info()
                    if info is not None:
                        if info.get_per_page() is not None:
                            print('Territory Info PerPage: ' + str(info.get_per_page()))
                        if info.get_page() is not None:
                            print('Territory Info Page: ' + str(info.get_page()))
                        if info.get_count() is not None:
                            print('Territory Info Count: ' + str(info.get_count()))
                        if info.get_more_records() is not None:
                            print('Territory Info MoreRecords: ' + str(info.get_more_records()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())
    @staticmethod
    def print_criteria(criteria):
        if criteria.get_comparator() is not None:
            print('Territory Criteria Comparator: ' + criteria.get_comparator())
        if criteria.get_field() is not None:
            print('Territory Criteria Field: ')
            print(criteria.get_field())
        if criteria.get_value() is not None:
            print('Territory Criteria Value: ' + str(criteria.get_value()))
        criteria_group = criteria.get_group()
        if criteria_group is not None:
            for each_criteria in criteria_group:
                GetChildTerritory.print_criteria(each_criteria)
        if criteria.get_group_operator() is not None:
            print('Territory Criteria Group Operator: ' + criteria.get_group_operator().get_value())


id = 440248001305227
GetChildTerritory.initialize()
GetChildTerritory.get_child_territory(id)