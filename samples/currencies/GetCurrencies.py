from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.currencies import CurrenciesOperations, BodyWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter, USDataCenter


class GetCurrencies(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", refresh_token="refresh_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_currencies():
        """
        This method is used to get all the available currencies in your organization.
        """
        currencies_operations = CurrenciesOperations()
        # Call get_currencies method
        response = currencies_operations.get_currencies()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, BodyWrapper):
                    currencies_list = response_object.get_currencies()
                    for currency in currencies_list:
                        print("Currency Id: " + str(currency.get_id()))
                        print("Currency IsoCode: " + str(currency.get_iso_code()))
                        print("Currency Symbol: " + str(currency.get_symbol()))
                        print("Currency CreatedTime: " + str(currency.get_created_time()))
                        print("Currency IsActive: " + str(currency.get_is_active()))
                        print("Currency ExchangeRate: " + str(currency.get_exchange_rate()))
                        format = currency.get_format()
                        if format is not None:
                            print("Currency Format DecimalSeparator: " + format.get_decimal_separator().get_value())
                            print("Currency Format ThousandSeparator: " + format.get_thousand_separator().get_value())
                            print("Currency Format DecimalPlaces: " + format.get_decimal_places().get_value())
                        created_by = currency.get_created_by()
                        if created_by is not None:
                            print("Currency Created By - Name: " + created_by.get_name())
                            print("Currency Created By - ID: " + str(created_by.get_id()))
                        modified_by = currency.get_modified_by()
                        if modified_by is not None:
                            print("Currency Modified By - Name: " + modified_by.get_name())
                            print("Currency Modified By - ID: " + str(modified_by.get_id()))
                        print("Currency PrefixSymbol: " + str(currency.get_prefix_symbol()))
                        print("Currency IsBase: " + str(currency.get_is_base()))
                        print("Currency ModifiedTime: " + str(currency.get_modified_time()))
                        print("Currency Name: " + currency.get_name())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


GetCurrencies.initialize()
GetCurrencies.get_currencies()
