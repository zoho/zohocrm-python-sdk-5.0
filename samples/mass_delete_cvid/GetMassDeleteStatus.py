from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.mass_delete_cvid import MassDeleteCvidOperations, GetMassDeleteStatusParam, \
    ResponseWrapper, APIException


class GetMassDeleteStatus(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_mass_delete_status(job_id, module_api_name):
        mass_delete_cvid_operations = MassDeleteCvidOperations(module_api_name)
        param_instance = ParameterMap()
        param_instance.add(GetMassDeleteStatusParam.job_id, job_id)
        response = mass_delete_cvid_operations.get_mass_delete_status(param_instance)
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
                    print("MassDelete TotalCount: " + status1.get_total_count())
                    print("MassDelete ConvertedCount: " + status1.get_deleted_count())
                    print("MassDelete FailedCount: " + status1.get_failed_count())
                    print("MassDelete Status: " + status1.get_status())
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message().get_value())


module_api_name = "Leads"
job_id = 440248001409012
GetMassDeleteStatus.initialize()
GetMassDeleteStatus.get_mass_delete_status(job_id, module_api_name)