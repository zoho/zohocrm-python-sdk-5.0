from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.available_currencies import AvailableCurrenciesOperations, ResponseWrapper, \
    APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class GetAvailableCurrencies(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)
        
    @staticmethod
    def get_available_currencies():
        currencies_operations = AvailableCurrenciesOperations()
        response = currencies_operations.get_available_currencies()
        if response is not None:
            print("Status code: " + str(response.get_status_code()))
            if response.get_status_code() == 204:
                print("No Content")
                return
            responseHandler = response.get_object()
            if isinstance(responseHandler, ResponseWrapper):
                responseWrapper = responseHandler
                currencies_list = responseWrapper.get_available_currencies()
                for currency in currencies_list:
                    print("Currency DisplayValue: " + currency.get_display_value())
                    print("Currency DecimalSeparator: " + currency.get_decimal_separator())
                    print("Currency Symbol: " + currency.get_symbol())
                    print("Currency ThousandSeparator: " + currency.get_thousand_separator())
                    print("Currency IsoCode: " + currency.get_iso_code())
                    print("Currency DisplayName: " + currency.get_display_name())
                    print("Currency DecimalPlaces: " + currency.get_decimal_places())
            elif isinstance(responseHandler, APIException):
                print("Status: " + responseHandler.get_status().get_value())
                print("Code: " + responseHandler.get_code().get_value())
                print("Details")
                details = responseHandler.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + responseHandler.get_message())


GetAvailableCurrencies.initialize()
GetAvailableCurrencies.get_available_currencies()
