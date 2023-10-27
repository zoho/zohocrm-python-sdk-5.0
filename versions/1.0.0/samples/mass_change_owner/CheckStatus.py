from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.mass_change_owner import MassChangeOwnerOperations, CheckStatusParam, \
    ResponseWrapper, APIException


class CheckStatus(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def check_status(job_id, module):
        mass_change_owner_operations = MassChangeOwnerOperations()
        param_instance = ParameterMap()
        param_instance.add(CheckStatusParam.job_id, job_id)
        response = mass_change_owner_operations.check_status(module, param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                response_wrapper = response_object
                status = response_wrapper.get_data()
                for status1 in status:
                    print("MassChangeOwner TotalCount: " + status1.get_total_count())
                    print("MassChangeOwner UpdatedCount: " + status1.get_updated_count())
                    print("MassChangeOwner NotUpdatedCount: " + status1.get_not_updated_count())
                    print("MassChangeOwner FailedCount: " + status1.get_failed_count())
                    print("MassChangeOwner Status: " + status1.get_status())
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message().get_value())


job_id = 4402480014804
module = "Calls"
CheckStatus.initialize()
CheckStatus.check_status(job_id, module)
