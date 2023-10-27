from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.currencies import CurrenciesOperations, BodyWrapper, Currency, Format, \
    ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class AddCurrencies(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def add_currencies():
        """
        This method is used to add new currencies to your organization.
        """
        currencies_operations = CurrenciesOperations()
        request = BodyWrapper()
        # List to hold Currency instances
        currencies_list = []
        currency = Currency()
        # To set the position of the ISO code in the currency.
        # True: Display ISO code before the currency value.
        # False: Display ISO code after the currency value.
        currency.set_prefix_symbol(True)
        # To set the name of the currency.
        currency.set_name("Angolan Kwanza - AOA")
        # To set the ISO code of the currency.
        currency.set_iso_code("AOA")
        # To set the symbol of the currency.
        currency.set_symbol("Kz")
        # To set the rate at which the currency has to be exchanged for home currency.
        currency.set_exchange_rate("20.0")
        # To set the status of the currency.
        # True: The currency is active.
        # False: The currency is inactive.
        currency.set_is_active(True)
        format = Format()
        # It can be a Period or Comma, depending on the currency.
        format.set_decimal_separator(Choice('Period'))
        # It can be a Period, Comma, or Space, depending on the currency.
        format.set_thousand_separator(Choice('Comma'))
        # To set the number of decimal places allowed for the currency. It can be 0, 2, or 3.
        format.set_decimal_places(Choice('2'))
        # To set the format of the currency
        currency.set_format(format)
        currencies_list.append(currency)
        request.set_currencies(currencies_list)
        # Call add_currencies method that takes BodyWrapper instance as parameter
        response = currencies_operations.create_currencies(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_currencies()
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


AddCurrencies.initialize()
AddCurrencies.add_currencies()