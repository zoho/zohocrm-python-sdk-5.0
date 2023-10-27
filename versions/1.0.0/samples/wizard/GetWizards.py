from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.wizards import WizardsOperations, ResponseWrapper, APIException


class GetWizards:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)
        
    @staticmethod
    def get_wizards():
        """
        This method is used to get a wizard' details with ID and print(the response.
        """
        wizard_operations = WizardsOperations()
        # Possible parameters for Get Wizard Operation
        # Call get_wizard method that takes ParameterMap instance as parameter
        response = wizard_operations.get_wizards()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    wizard_list = response_object.get_wizards()
                    for wizard in wizard_list:
                        print(" ID " + str(wizard.get_id()))
                        print("Name: " + str(wizard.get_name()))
                        print("Modified Time: " + str(wizard.get_modified_time()))
                        print("Created Time: " + str(wizard.get_created_time()))
                        print("Draft: " + str(wizard.get_draft()))
                        print("active: " + str(wizard.get_active()))
                        created_by = wizard.get_created_by()
                        if created_by is not None:
                            print("Created By - Name: " + created_by.get_name())
                            print("Created By - ID: " + str(created_by.get_id()))
                            print("Created By - email: " + str(created_by.get_email()))
                        parent_wizard = wizard.get_parent_wizard()
                        if parent_wizard is not None:
                            print("Wizard parent_wizard ID: " + parent_wizard.get_parent_wizard())
                            print("Wizard parent_wizard Name:" + str(parent_wizard.get_id()))
                        # get module
                        module = wizard.get_module()
                        if module is not None:
                            print("Module - API Name: " + module.get_api_name())
                            print("Module - ID: " + str(module.get_id()))
                        # get profiles
                        profiles = wizard.get_profiles()
                        for profile in profiles:
                            print("Wizard Profile ID: " + str(profile.get_id()))
                            print("Wizard Profile Name: " + profile.get_name())
                        modified_by = wizard.get_modified_by()
                        if modified_by is not None:
                            print("Modified By - Name: " + modified_by.get_name())
                            print("Modified By - ID: " + str(modified_by.get_id()))
                            print("Modified By - ID: " + str(modified_by.get_email()))
                        containers = wizard.get_containers()
                        if containers is not None:
                            for container in containers:
                                print("\n Container Id: " + str(container.get_id()))
                                layout = container.get_layout()
                                if layout is not None:
                                    print("\n Layout id" + str(layout.get_id()))
                                    print("\n Layout name" + layout.get_name())
                                chart_data = container.get_chart_data()
                                if chart_data is not None:
                                    nodes = chart_data.get_nodes()
                                    for node in nodes:
                                        print("\n Chart Data Node poistion y: ")
                                        print(node.get_pos_y())
                                        print("\n Chart Data Node poistion x: ")
                                        print(node.get_pos_x())
                                        print("\n Chart Data Node start node : ")
                                        print(node.get_start_node())
                                        node_screen = node.get_screen()
                                        if node_screen is not None:
                                            print("\n Screen id")
                                            print(node_screen.get_id())
                                            print("\n Screen display label")
                                            print(node_screen.get_display_label())
                                    connections = chart_data.get_connections()
                                    for connection in connections:
                                        connection_screen = connection.get_target_screen()
                                        if connection_screen is not None:
                                            print("\n connection_screen id")
                                            print(connection_screen.get_id())
                                            print("\n connection_screen display label")
                                            print(connection_screen.get_display_label())
                                        connection_button = connection_screen.get_source_button()
                                        if connection_button is not None:
                                            print("\n connection_button id")
                                            print(connection_button.get_id())
                                            print("\n connection_button display label")
                                            print(connection_button.get_display_label())
                                chart_data = container.get_chart_data()
                                if chart_data is not None:
                                    print("\n Chart Data Canvas width: ")
                                    print(chart_data.get_canvas_width())
                                    print("\n Chart Data Canvas height: ")
                                    print(chart_data.get_canvas_height())
                                screens = container.get_screens()
                                if screens is not None:
                                    for screen in screens:
                                        print("\n screen id")
                                        print(screen.get_id())
                                        print("\n screen display label")
                                        print(screen.get_display_label())
                                        segments = screen.get_segments()
                                        for segment in segments:
                                            print("\n segment id")
                                            print(segment.get_id())
                                            print("\n segment display label")
                                            print(segment.get_display_label())
                                            print("\n segment  sequence number")
                                            print(segment.get_sequence_number())
                                            print("\n segment type")
                                            print(segment.get_type())
                                            print("\n segment column count")
                                            print(segment.get_column_count())
                                            fields = segment.get_fields()
                                            for field in fields:
                                                print("\n field id")
                                                print(field.get_id())
                                                print("\n field api_name")
                                                print(field.get_api_name())
                                            buttons = segment.get_buttons()
                                            for button in buttons:
                                                criteria = button.get_criteria()
                                                if criteria is not None:
                                                    GetWizards.print_criteria(criteria)
                                                target_screen = button.get_target_screen()
                                                if target_screen is not None:
                                                    print("\n target screen id")
                                                    print(target_screen.get_id())
                                                    print("\n target screen display label")
                                                    print(target_screen.get_display_label())
                                                print("\n  Button display label:")
                                                print(button.get_display_label())
                                                print("\n  Button id:")
                                                print(button.get_id())
                                                print("\n  Button type:")
                                                print(button.get_type())
                                                print("\n  Button background color:")
                                                print(button.get_background_color())
                                                print("\n  Button sequence number:")
                                                print(button.get_sequence_number())
                                                print("\n  Button color:")
                                                print(button.get_color())
                                                print("\n  Button type:")
                                                print(button.get_type())
                                                print("\n  Button shape:")
                                                print(button.get_shape())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    if details is not None:
                        if details is not None:
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())

    @staticmethod
    def print_criteria(criteria):
        if criteria.get_comparator() is not None:
            print('Field Criteria Comparator: ' + criteria.get_comparator().get_value())
        if criteria.get_field() is not None:
            print('Field Criteria Field: ' + criteria.get_field())
        if criteria.get_value() is not None:
            print('Field Criteria Value: ' + str(criteria.get_value()))
        criteria_group = criteria.get_group()
        if criteria_group is not None:
            for each_criteria in criteria_group:
                GetWizards.print_criteria(each_criteria)
        if criteria.get_group_operator() is not None:
            print('Field Criteria Group Operator: ' + criteria.get_group_operator().get_value())


GetWizards.initialize()
GetWizards.get_wizards()