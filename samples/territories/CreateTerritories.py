from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.territories import TerritoriesOperations, BodyWrapper, Territories, Criteria, \
    Field, ReportingTo, Manager, ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class CreateTerritories(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_territories():
        territories_operations = TerritoriesOperations()
        request = BodyWrapper()
        territories = []
        territory = Territories()
        territory.set_name("territoryName")
        criteria = Criteria()
        criteria.set_comparator("equal")
        criteria.set_value("name")
        field = Field()
        field.set_api_name("Account_Name")
        field.set_id(4402480605)
        criteria.set_field(field)
        territory.set_account_rule_criteria(criteria)
        criteria1 = Criteria()
        criteria1.set_comparator("greater_than")
        value = 1001
        criteria1.set_value(value)
        field1 = Field()
        field1.set_api_name("Annual Revenue")
        field1.set_id(4402480625)
        criteria1.set_field(field1)
        territory.set_deal_rule_criteria(criteria1)
        territory.set_description("description")
        territory.set_permission_type(Choice("read_only"))
        reportingTo = ReportingTo()
        reportingTo.set_id(440248001305227)
        territory.set_reporting_to(reportingTo)
        manager = Manager()
        manager.set_id(4402480254001)
        territory.set_manager(manager)
        territories.append(territory)
        request.set_territories(territories)
        response = territories_operations.create_territories(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_territories()
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


CreateTerritories.initialize()
CreateTerritories.create_territories()