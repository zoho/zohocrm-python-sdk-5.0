from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.inventory_templates import InventoryTemplatesOperations, ResponseWrapper, \
    APIException


class GetInventoryTemplates:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_inventory_templates():
        """
        This method is used to get a inventory_templates' details with ID and print the response.
        """
        inventory_templates_operations = InventoryTemplatesOperations()
        # Call get_inventory_templates method that takes ParameterMap instance as parameter
        response = inventory_templates_operations.get_inventory_templates()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    inventory_templates_list = response_object.get_inventory_templates()
                    for inventory_template in inventory_templates_list:
                        print(" ID " + str(inventory_template.get_id()))
                        print("Name: " + str(inventory_template.get_name()))
                        print("Modified Time: " + str(inventory_template.get_modified_time()))
                        print("Created Time: " + str(inventory_template.get_created_time()))
                        print("Type: " + str(inventory_template.get_type()))
                        print("Last Usage Time: " + str(inventory_template.get_last_usage_time()))
                        print("Content: " + str(inventory_template.get_content()))
                        print("EditorMode: " + str(inventory_template.get_editor_mode()))
                        created_by = inventory_template.get_created_by()
                        if created_by is not None:
                            print("Created By - Name: " + created_by.get_name())
                            print("Created By - ID: " + str(created_by.get_id()))
                            print("Created By - email: " + str(created_by.get_email()))
                        folder = inventory_template.get_folder()
                        if folder is not None:
                            print("InventoryTemplate folder ID: " + folder.get_name())
                            print("InventoryTemplate folder Name:" + str(folder.get_id()))
                        # get module
                        module = inventory_template.get_module()
                        if module is not None:
                            print("Module - API Name: " + module.get_api_name())
                            print("Module - ID: " + str(module.get_id()))
                        modified_by = inventory_template.get_modified_by()
                        if modified_by is not None:
                            print("Modified By - Name: " + modified_by.get_name())
                            print("Modified By - ID: " + str(modified_by.get_id()))
                            print("Modified By - ID: " + str(modified_by.get_email()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    if details is not None:
                        if details is not None:
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


GetInventoryTemplates.initialize()
GetInventoryTemplates.get_inventory_templates()
