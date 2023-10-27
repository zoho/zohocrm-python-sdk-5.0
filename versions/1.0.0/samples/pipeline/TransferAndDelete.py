from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.pipeline import TransferPipelineWrapper, TransferPipeline, Pipeline, TPipeline, \
    Stages, PipelineOperations, ActionWrapper, SuccessResponse, APIException, TransferPipelineActionWrapper, \
    TransferPipelineSuccessResponse


class TransferAndDelete:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def transfer_and_delete(layout_id):
        transfer_and_delete_wrapper = TransferPipelineWrapper()
        transfer_pipeline = TransferPipeline()
        pipeline = TPipeline()
        pipeline.set_from(440248001538068)
        pipeline.set_to(440248001413033)
        stage = Stages()
        stage.set_to(4402480257)
        stage.set_from(4402480257)
        transfer_pipeline.set_pipeline(pipeline)
        transfer_pipeline.set_stages([stage])
        transfer_and_delete_wrapper.set_transfer_pipeline([transfer_pipeline])
        pipeline_operations = PipelineOperations(layout_id)
        response = pipeline_operations.transfer_pipelines(transfer_and_delete_wrapper)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, TransferPipelineActionWrapper):
                    action_response_list = response_object.get_transfer_pipeline()
                    for action_response in action_response_list:
                        if isinstance(action_response, TransferPipelineSuccessResponse):
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


layout_id = 4402480173
TransferAndDelete.initialize()
TransferAndDelete.transfer_and_delete(layout_id)