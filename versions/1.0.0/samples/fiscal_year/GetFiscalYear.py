from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.fiscal_year import FiscalYearOperations, ResponseWrapper, APIException


class GetFiscalYear(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_fiscal_year():
        fiscal_year_operations = FiscalYearOperations()
        response = fiscal_year_operations.get_fiscal_year()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                response_wrapper = response_object
                fiscal_year = response_wrapper.get_fiscal_year()
                if fiscal_year is not None:
                    print("FiscalYear startMonth :" + fiscal_year.get_start_month().get_value())
                    print("FiscalYear displayBasedOn :" + fiscal_year.get_display_based_on().get_value())
                    print("FiscalYear Id : " + str(fiscal_year.get_id()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message().get_value())


GetFiscalYear.initialize()
GetFiscalYear.get_fiscal_year()