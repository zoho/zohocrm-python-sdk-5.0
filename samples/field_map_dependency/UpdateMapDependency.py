from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.field_map_dependency import FieldMapDependencyOperations, BodyWrapper, \
    MapDependency, Parent, Child, PickListMapping, PicklistMap, APIException, SuccessResponse, ActionWrapper


class UpdateMapDependency(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_map_dependency(layout_id, module, dependency_id):
        field_map_dependency_operations = FieldMapDependencyOperations(layout_id, module)
        body_wrapper = BodyWrapper()
        map_dependencies = []
        map_dependnecy = MapDependency()
        parent = Parent()
        parent.set_api_name("Lead_Status")
        parent.set_id(3323032493483)
        map_dependnecy.set_parent(parent)
        child = Child()
        child.set_api_name("Lead_Source")
        child.set_id(3345243354342)
        map_dependnecy.set_child(child)
        pick_list_values = []
        pick_list_value = PickListMapping()
        pick_list_value.set_display_value("-None-")
        pick_list_value.set_id(333452343242343)
        pick_list_value.set_actual_value("-None-")
        pick_list_maps = []
        pick_list_map = PicklistMap()
        pick_list_map.set_id(34234234234234)
        pick_list_map.set_actual_value("Option 1")
        pick_list_map.set_display_value("Option 1")
        pick_list_maps.append(pick_list_map)
        pick_list_map = PicklistMap()
        pick_list_map.set_id(34500302342)
        pick_list_map.set_actual_value("-None-")
        pick_list_map.set_display_value("-None-")
        pick_list_maps.append(pick_list_map)
        pick_list_value.set_maps(pick_list_maps)
        pick_list_values.append(pick_list_value)
        map_dependnecy.set_pick_list_values(pick_list_values)
        map_dependencies.append(map_dependnecy)
        response = field_map_dependency_operations.update_map_dependency(dependency_id, body_wrapper)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_map_dependency()
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


module_api_name = "Leads"
layout_id = 3424123124322
dependency_id = 32534534412312
UpdateMapDependency.initialize()
UpdateMapDependency.update_map_dependency(layout_id, module_api_name, dependency_id)