from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.pipeline import PipelineOperations, BodyWrapper, APIException


class GetPipelines:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_pipelines(layout_id):
        # layout_id = 35240330091055
        pipeline_operations = PipelineOperations(layout_id)
        response = pipeline_operations.get_pipelines()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, BodyWrapper):
                    pipelines_list = response_object.get_pipeline()
                    for pipeline in pipelines_list:
                        print("ID: " + str(pipeline.get_id()))
                        print("Display value: " + str(pipeline.get_display_value()))
                        print("Actual value: " + str(pipeline.get_actual_value()))
                        print("default: " + str(pipeline.get_default()))
                        print("child available: " + str(pipeline.get_child_available()))
                        parent = pipeline.get_parent()
                        if parent is not None:
                            print("pipeline parent: " + str(parent.get_id()))
                        maps = pipeline.get_maps()
                        for map_instance in maps:
                            print("PickListValue Actual Value: " + str(map_instance.get_actual_value()))
                            print("PickListValue delete Value: " + str(map_instance.get_delete()))
                            print("PickListValue Display Value: " + str(map_instance.get_display_value()))
                            print("PickListValue forecast type: " + str(map_instance.get_forecast_type()))
                            forecast_category = map_instance.get_forecast_category()
                            if forecast_category is not None:
                                print("Forecast Category Name: " + str(forecast_category.get_name()))
                                print("Forecast Category ID: " + str(forecast_category.get_id()))
                            print("PickListValue id: " + str(map_instance.get_id()))
                            print("PickListValue sequence number: " + str(map_instance.get_sequence_number()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


layout_id = 4402480173
GetPipelines.initialize()
GetPipelines.get_pipelines(layout_id)