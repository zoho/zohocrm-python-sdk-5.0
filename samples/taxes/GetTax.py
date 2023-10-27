from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.taxes import TaxesOperations, ResponseWrapper, APIException


class GetTax:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)
        
    @staticmethod
    def get_tax(tax_id):
        """
        This method is used to get the Organization Tax with ID and print the response.
        :param tax_id: The ID of the tax to be obtained
        """
        """
        example
        tax_id = 3409643002317003
        """
        taxes_operations = TaxesOperations()
        # Call get_tax method that takes tax_id as parameter
        response = taxes_operations.get_tax(tax_id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    org_tax = response_object.get_org_taxes()
                    taxes_list = org_tax.get_taxes()
                    for tax in taxes_list:
                        print("Tax DisplayLabel: " + tax.get_display_label())
                        print("Tax Name: " + tax.get_name())
                        print("Tax sequence number : " + str(tax.get_sequence_number()))
                        print("Tax ID: " + str(tax.get_id()))
                        print("Tax Value: " + str(tax.get_value()))
                    preference = org_tax.get_preference()
                    if preference is not None:
                        print("Preference AutoPopulateTax: " + str(preference.get_auto_populate_tax()))
                        print("Preference ModifyTaxRates: " + str(preference.get_modify_tax_rates()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


tax_id = 440248001507003
GetTax.initialize()
GetTax.get_tax(tax_id)