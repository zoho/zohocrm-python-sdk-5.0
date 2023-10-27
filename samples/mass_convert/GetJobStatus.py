from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.mass_convert import MassConvertOperations, GetJobStatusParam, ResponseWrapper, \
    APIException


class GetJobStatus(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_job_Status(job_id):
        mass_convert_operations = MassConvertOperations()
        param_instance = ParameterMap()
        param_instance.add(GetJobStatusParam.job_id, job_id)
        response = mass_convert_operations.get_job_status(param_instance)
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
                    print("MassConvert TotalCount: " + str(status1.get_total_count()))
                    print("MassConvert ConvertedCount: " + str(status1.get_converted_count()))
                    print("MassConvert NotConvertedCount: " + str(status1.get_not_converted_count()))
                    print("MassConvert FailedCount: " + str(status1.get_failed_count()))
                    print("MassConvert Status: " + str(status1.get_status()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


job_id = 440248001480019
GetJobStatus.initialize()
GetJobStatus.get_job_Status(job_id)