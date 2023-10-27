from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.field_map_dependency import FieldMapDependencyOperations, BodyWrapper, APIException


class GetMapDependency(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_map_dependency(layout_id, module, dependency_id):
        field_map_dependency_operations = FieldMapDependencyOperations(layout_id, module)
        response = field_map_dependency_operations.get_map_dependency(dependency_id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, BodyWrapper):
                response_wrapper = response_object
                map_dependencies = response_wrapper.get_map_dependency()
                for map_dependency in map_dependencies:
                    parent = map_dependency.get_parent()
                    if parent is not None:
                        print("MapDependency ParentId : " + str(parent.get_id()))
                        print("MapDependency Parent APIName: " + parent.get_api_name())
                    child = map_dependency.get_child()
                    if child is not None:
                        print("MapDependency Child ID: " + str(child.get_id()))
                        print("MapDependency Child APIName: " + child.get_api_name())
                        pick_list_values = map_dependency.get_pick_list_values()
                        if pick_list_values is not None:
                            for pickListValue in pick_list_values:
                                print("MapDependency PickListValue ID: " + str(pickListValue.get_id()))
                                print("MapDependency PickListValue ActualValue: " + pickListValue.get_actual_value())
                                print("MapDependency PickListValue DisplayValue: " + pickListValue.get_display_value())
                                picklistMaps = pickListValue.get_maps()
                                if picklistMaps is not None:
                                    for picklistMap in picklistMaps:
                                        print("MapDependency PickListValue Map ID: " + str(picklistMap.get_id()))
                                        print("MapDependency PickListValue Map ActualValue: " + picklistMap.get_actual_value())
                                        print("MapDependency PickListValue Map DisplayValue: " + picklistMap.get_display_value())
                        print("MapDependency Internal: " + str(map_dependency.get_internal()))
                        print("MapDependency Active: " + str(map_dependency.get_active()))
                        print("MapDependency ID: " + str(map_dependency.get_id()))
                        print("MapDependency Category: " + str(map_dependency.get_category()))
                        print("MapDependency Source: " + str(map_dependency.get_source()))
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
dependency_id = 440248001476004
GetMapDependency.initialize()
GetMapDependency.get_map_dependency(layout_id, module_api_name, dependency_id)