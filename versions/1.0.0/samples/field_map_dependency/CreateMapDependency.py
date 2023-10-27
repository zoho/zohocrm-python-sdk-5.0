from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.field_map_dependency import FieldMapDependencyOperations, BodyWrapper, \
    MapDependency, Parent, Child, PickListMapping, PicklistMap, APIException, SuccessResponse, ActionWrapper


class CreateMapDependency(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_map_dependency(layout_id, module):
        field_map_dependency_operations = FieldMapDependencyOperations(layout_id, module)
        body_wrapper = BodyWrapper()
        map_dependencies = []
        map_dependnecy = MapDependency()
        parent = Parent()
        parent.set_api_name("Lead_Status")
        parent.set_id(4402480887)
        map_dependnecy.set_parent(parent)
        child = Child()
        child.set_api_name("Lead_Source")
        child.set_id(4402480885)
        map_dependnecy.set_child(child)
        pick_list_values = []
        pick_list_value = PickListMapping()
        pick_list_value.set_display_value("-None-")
        pick_list_value.set_id(4402480011340)
        pick_list_value.set_actual_value("-None-")
        pick_list_maps = []
        pick_list_map = PicklistMap()
        pick_list_map.set_id(4402480011274)
        pick_list_map.set_actual_value("Cold Call")
        pick_list_map.set_display_value("Cold Call")
        pick_list_maps.append(pick_list_map)
        pick_list_map = PicklistMap()
        pick_list_map.set_id(4402480011268)
        pick_list_map.set_actual_value("-None-")
        pick_list_map.set_display_value("-None-")
        pick_list_maps.append(pick_list_map)
        pick_list_value.set_maps(pick_list_maps)
        pick_list_values.append(pick_list_value)
        map_dependnecy.set_pick_list_values(pick_list_values)
        map_dependencies.append(map_dependnecy)
        body_wrapper.set_map_dependency(map_dependencies)
        response = field_map_dependency_operations.create_map_dependency(body_wrapper)
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
layout_id = 4402480167
CreateMapDependency.initialize()
CreateMapDependency.create_map_dependency(layout_id, module_api_name)