from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.fields import PickListValue
from zohocrmsdk.src.com.zoho.crm.api.pipeline import PipelineOperations, Pipeline, BodyWrapper, ActionWrapper, \
    SuccessResponse, APIException


class UpdatePipelines:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)
        
    @staticmethod
    def update_pipelines(layout_id):
        # layout_id = 35240330091055
        pipeline_operations = PipelineOperations(layout_id)
        pipeline = Pipeline()
        pipeline_id = 3652397006815
        pipeline.set_display_value("Pipeline2")
        pipeline.set_default(True)
        pipeline.set_id(pipeline_id)
        map = PickListValue()
        map.set_sequence_number(1)
        map.set_id(3652397006815)
        map.set_display_value("Closed Won")
        maps = [map]
        pipeline.set_maps(maps)
        request = BodyWrapper()
        request.set_pipeline([pipeline])
        response = pipeline_operations.update_pipelines(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_pipeline()
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


layout_id = 324234234324
UpdatePipelines.initialize()
UpdatePipelines.update_pipelines(layout_id)