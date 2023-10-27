from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.taxes import TaxesOperations, BodyWrapper, Tax, ActionWrapper, SuccessResponse, \
    APIException, OrgTax, Preference


class UpdateTaxes:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)
        
    @staticmethod
    def update_taxes():
        """
        This method is used to update Organization Taxes and print the response.
        """
        taxes_operations = TaxesOperations()
        request = BodyWrapper()
        org_tax = OrgTax()
        tax_list = []
        tax_1 = Tax()
        tax_1.set_id(440248001506005)
        tax_1.set_name('ModifiedMyTax22')
        tax_1.set_sequence_number(3)
        tax_1.set_value(10.0)
        tax_list.append(tax_1)
        org_tax.set_taxes(tax_list)
        prefernce = Preference()
        prefernce.set_auto_populate_tax(False)
        prefernce.set_modify_tax_rates(False)
        org_tax.set_preference(prefernce)
        request.set_org_taxes(org_tax)
        response = taxes_operations.update_taxes(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response = response_object.get_org_taxes()
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


UpdateTaxes.initialize()
UpdateTaxes.update_taxes()
