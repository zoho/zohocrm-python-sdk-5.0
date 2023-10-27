from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.layouts import LayoutsOperations, GetLayoutsParam, ResponseWrapper, APIException


class GetLayouts:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_layouts(module_api_name):
        """
        This method is used to get metadata about all the layouts of a module and print the response.
        :param module_api_name: The API Name of the module to get layouts.
        """
        """
        example
        module_api_name = "Leads";
        """
        layouts_operations = LayoutsOperations()
        param_instance = ParameterMap()
        param_instance.add(GetLayoutsParam.module, module_api_name)
        # Call get_layouts method
        response = layouts_operations.get_layouts(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    layouts_list = response_object.get_layouts()
                    for layout in layouts_list:
                        if layout.get_created_time() is not None:
                            print('Layout CreatedTime: ' + str(layout.get_created_time()))
                        if layout.get_convert_mapping() is not None:
                            convert_mapping = layout.get_convert_mapping()
                            accounts = convert_mapping.get_accounts()
                            contacts = convert_mapping.get_contacts()
                            deals = convert_mapping.get_deals()
                        if layout.get_modified_time() is not None:
                            print('Layout ModifiedTime: ' + str(layout.get_modified_time()))
                        print("Layout Visible: " + str(layout.get_visible()))
                        created_for = layout.get_created_for()
                        if created_for is not None:
                            print("Layout Created For - Name: " + created_for.get_name())
                            print("Layout Created For - ID: " + str(created_for.get_id()))
                        print("Layout Name: " + layout.get_name())
                        modified_by = layout.get_modified_by()
                        if modified_by is not None:
                            print("Layout Modified By - Name: " + modified_by.get_name())
                            print("Layout Modified By - ID: " + str(modified_by.get_id()))
                        profiles = layout.get_profiles()
                        if profiles is not None:
                            for profile in profiles:
                                print("Layout Profile Default: " + str(profile.get_default()))
                                print("Layout Profile Name: " + profile.get_name())
                                print("Layout Profile ID: " + str(profile.get_id()))
                                default_view = profile.get_defaultview()
                                if default_view is not None:
                                    print("Layout Profile DefaultView Name:")
                                    print(default_view.get_name())
                                    print("Layout Profile DefaultView ID:")
                                    print(default_view.get_id())
                                    print("Layout Profile DefaultView Type:")
                                    print(default_view.get_type())
                        print("Layout ID: " + str(layout.get_id()))
                        created_by = layout.get_created_by()
                        if created_by is not None:
                            print("Layout Created By - Name: " + created_by.get_name())
                            print("Layout Created By - ID: " + str(created_by.get_id()))
                        sections = layout.get_sections()
                        if sections is not None:
                            for section in sections:
                                print("Layout Section DisplayLabel: " + section.get_display_label())
                                print("Layout Section SequenceNumber: " + str(section.get_sequence_number()))
                                print("Layout Section Issubformsection: " + str(section.get_issubformsection()))
                                print("Layout Section TabTraversal: " + str(section.get_tab_traversal()))
                                print("Layout Section APIName: " + section.get_api_name())
                                print("Layout Section Name: " + section.get_name())
                                print("Layout Section type: " + section.get_type())
                                print("\n Section type:")
                                print(section.get_type())
                                print("Layout Section ColumnCount: " + str(section.get_column_count()))
                                print("Layout Section GeneratedType: " + section.get_generated_type())
                                fields = section.get_fields()
                                if fields is not None:
                                    for field in fields:
                                        GetLayouts.print_field(field)
                                properties = section.get_properties()
                                if properties is not None:
                                    print(
                                        "Layout Section Properties ReorderRows: " + str(properties.get_reorder_rows()))
                                    tool_tip = properties.get_tooltip()
                                    if tool_tip is not None:
                                        print("Layout Section Properties ToolTip Name: " + tool_tip.get_name())
                                        print("Layout Section Properties ToolTip Value: " + str(tool_tip.get_value()))
                                    print(
                                        "Layout Section Properties MaximumRows: " + str(properties.get_maximum_rows()))
                        print("Layout Status: " + str(layout.get_status()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())

    @staticmethod
    def print_field(field):
        print('Field ID: ' + str(field.get_id()))
        print("Field SystemMandatory: " + str(field.get_system_mandatory()))
        print("Field Webhook: " + str(field.get_webhook()))
        print("Field JsonType: " + str(field.get_json_type()))
        crypt = field.get_crypt()
        if crypt is not None:
            print("Crypt Details")
            print("Mode: " + str(crypt.get_mode()))
            print("Column: " + str(crypt.get_column()))
            print("Table: " + str(crypt.get_table()))
            print("Status: " + str(crypt.get_status()))
            enc_fld_ids = crypt.get_enc_fld_ids()
            if enc_fld_ids is not None:
                print("\nEncFldIds : ")
                for enc_fld_id in enc_fld_ids:
                    print(enc_fld_id)
            print("\nField Crypt Notify:")
            print(crypt.get_notify())
        print("Field FieldLabel: " + str(field.get_field_label()))
        multi_user_lookup = field.get_multiuserlookup()
        if multi_user_lookup is not None:
            print("DisplayLabel: " + str(multi_user_lookup.get_display_label()))
            print("LinkingModule: " + str(multi_user_lookup.get_linking_module()))
            print("LookupApiname: " + str(multi_user_lookup.get_lookup_apiname()))
            print("APIName: " + str(multi_user_lookup.get_api_name()))
            print("ConnectedlookupApiname: " + str(multi_user_lookup.get_connectedlookup_apiname()))
            print("ID: " + str(multi_user_lookup.get_id()))
            print("Connected Module: " + str(multi_user_lookup.get_connected_module()))
        private_info = field.get_private()
        if private_info is not None:
            print("\nField Private Type: ")
            print(private_info.get_type())
            print("\nField Private Export: ")
            print(private_info.get_export())
            print("\nField Private Restricted: ")
            print(private_info.get_restricted())
        if field.get_external() is not None:
            external = field.get_external()
            print("External Show: " + str(external.get_show()))
            print("External Type: " + str(external.get_type()))
            print("External Type: " + str(external.get_allow_multiple_config()))
        profiles = field.get_profiles()
        for profile in profiles:
            print("\n Field Profile PermissionType: ")
            print(profile.get_permission_type())
            print("\n Field Profile Name: ")
            print(profile.get_name())
            print("\n Field Profile ID: ")
            print(profile.get_id())
        tool_tip = field.get_tooltip()
        if tool_tip is not None:
            print("Field ToolTip Name: " + tool_tip.get_name())
            print("Field ToolTip Value: " + tool_tip.get_value())
        print("Field CreatedSource: " + field.get_created_source())
        print("Field FieldReadOnly: " + str(field.get_field_read_only()))
        print("Field DisplayLabel: " + field.get_display_label())
        print("Field ReadOnly: " + str(field.get_read_only()))
        print("\n Field is Private :")
        print(field.get_private())
        print("\n Field is UiType :")
        print(field.get_ui_type())
        print("\n Field  PickListValuesSortedLexically :")
        print(field.get_pick_list_values_sorted_lexically())
        multi_module_lookup = field.get_multi_module_lookup()
        if multi_module_lookup is not None:
            print("Lookup api_name : " + str(multi_module_lookup.get_api_name()))
            module = multi_module_lookup.get_modules()
            if module is not None:
                print("module Id: " + str(module.get_id()))
                print("module Id: " + module.get_api_name())
        association_details = field.get_association_details()
        if association_details is not None:
            lookup_field = association_details.get_lookup_field()
            if lookup_field is not None:
                print("Field AssociationDetails LookupField ID: " + str(lookup_field.get_id()))
                print('Field AssociationDetails LookupField Name: ' + lookup_field.get_name())
            related_field = association_details.get_related_field()
            if related_field is not None:
                print("Field AssociationDetails RelatedField ID: " + str(related_field.get_id()))
                print('Field AssociationDetails RelatedField Name: ' + related_field.get_name())
        if field.get_quick_sequence_number() is not None:
            print('Field QuickSequenceNumber: ' + str(field.get_quick_sequence_number()))
        if field.get_businesscard_supported() is not None:
            print('Field BusinesscardSupported: ' + str(field.get_businesscard_supported()))
        currency = field.get_currency()
        if currency is not None:
            print("Field Currency RoundingOption: " + str(currency.get_rounding_option()))
            if currency.get_precision() is not None:
                print("Field Currency Precision: " + str(currency.get_precision()))
        if field.get_custom_field() is not None:
            print("Field CustomField: " + str(field.get_custom_field()))
        lookup = field.get_lookup()
        if lookup is not None:
            print("Field ModuleLookup DisplayLabel: " + str(lookup.get_display_label()))
            print("Field ModuleLookup APIName: " + str(lookup.get_api_name()))
            print("Field ModuleLookup Module: " + str(lookup.get_module()))
            if lookup.get_id() is not None:
                print("Field ModuleLookup ID: " + str(lookup.get_id()))
        if field.get_visible() is not None:
            print("Field Visible: " + str(field.get_visible()))
        if field.get_length() is not None:
            print("Field Length: " + str(field.get_length()))
        view_type = field.get_view_type()
        if view_type is not None:
            print("Field ViewType View: " + str(view_type.get_view()))
            print("Field ViewType Edit: " + str(view_type.get_edit()))
            print("Field ViewType Create: " + str(view_type.get_create()))
            print("Field ViewType QuickCreate: " + str(view_type.get_quick_create()))
        subform = field.get_subform()
        if subform is not None:
            layout = subform.get_layout()
            if layout is not None:
                print("Field Subform Layout ID: " + str(layout.get_id()))
                print("Field Subform Layout Name: " + str(layout.get_name()))
            print("Field Subform DisplayLabel: " + str(subform.get_display_label()))
            print("Field Subform APIName: " + str(subform.get_api_name()))
            print("Field Subform Module: " + str(subform.get_module()))
            if subform.get_id() is not None:
                print("Field Subform ID: " + str(subform.get_id()))
        print("Field APIName : " + field.get_api_name())
        pick_list_values = field.get_pick_list_values()
        if pick_list_values is not None:
            for pick_list_value in pick_list_values:
                GetLayouts.print_pick_list_value(pick_list_value)
        unique = field.get_unique()
        if unique is not None:
            print("Field Unique Casesensitive : " + str(unique.get_casesensitive()))
        if field.get_history_tracking() is not None:
            history_tracking = field.get_history_tracking()
            module = history_tracking.get_module()
            if module is not None:
                module_layout = module.get_layout()
                if module_layout is not None:
                    print("Module layout id: " + str(module_layout.get_id()))
                print("Module display label: " + str(module.get_api_name()))
                print("Module api name: " + str(module.get_id()))
                print("Module module: " + str(module.get_module()))
                print("Module module name: " + str(module.get_module_name()))
            duration_configured = history_tracking.get_duration_configured_field()
            if duration_configured is not None:
                print("historytracking duration configured field: " + str(duration_configured.get_id()))
        print("Field DataType: " + field.get_data_type().get_value())
        formula = field.get_formula()
        if formula is not None:
            print('Field Formula ReturnType : ' + str(formula.get_return_type()))
            if formula.get_expression() is not None:
                print("Field Formula Expression : " + str(formula.get_expression()))
        if field.get_decimal_place() is not None:
            print("Field DecimalPlace: " + str(field.get_decimal_place()))
        print("Field MassUpdate: " + str(field.get_mass_update()))
        if field.get_blueprint_supported() is not None:
            print("Field BlueprintSupported: " + str(field.get_blueprint_supported()))
        multi_select_lookup = field.get_multiselectlookup()
        if multi_select_lookup is not None:
            print("Field MultiSelectLookup DisplayLabel: " + str(multi_select_lookup.get_display_label()))
            print("Field MultiSelectLookup LinkingModule: " + str(multi_select_lookup.get_linking_module()))
            print("Field MultiSelectLookup LookupApiname: " + str(multi_select_lookup.get_lookup_apiname()))
            print("Field MultiSelectLookup APIName: " + str(multi_select_lookup.get_api_name()))
            print("Field MultiSelectLookup ConnectedlookupApiname: " + str(
                multi_select_lookup.get_connectedlookup_apiname()))
            print("Field MultiSelectLookup ID: " + str(multi_select_lookup.get_id()))
            print("Field MultiSelectLookup connected module: " + str(multi_select_lookup.get_connected_module()))
        pick_list_values = field.get_pick_list_values()
        if pick_list_values is not None:
            for plv in pick_list_values:
                GetLayouts.print_pick_list_value(plv)
        auto_number = field.get_auto_number()
        if auto_number is not None:
            print('Prefix: ' + str(auto_number.get_prefix()))
            print('Suffix: ' + str(auto_number.get_suffix()))
            if auto_number.get_start_number() is not None:
                print('Start Number: ' + str(auto_number.get_start_number()))
        if field.get_default_value() is not None:
            print("Field DefaultValue: " + str(field.get_default_value()))
        if field.get_display_type() is not None:
            print("Field display_type: " + str(field.get_display_type()))
        if field.get_validation_rule() is not None:
            for key, value in field.get_validation_rule().items():
                print(key + " : " + value)
    @staticmethod
    def print_pick_list_value(pick_list_value):
        print("\n DisplayValue:")
        print(pick_list_value.get_display_value())
        print("\n SequenceNumber:")
        print(pick_list_value.get_sequence_number())
        print("\n ExpectedDataType:")
        print(pick_list_value.get_expected_data_type())
        print("\n ActualValue :")
        print(pick_list_value.get_actual_value)
        if pick_list_value.get_maps() is not None:
            for map in pick_list_value.get_maps():
                print("\n")
                print(map)
                pick_list_values = map.get_pick_list_values
                if pick_list_values is not None:
                    for plv in pick_list_values:
                        GetLayouts.print_pick_list_value(plv)
        print("\nField PickListValue SysRefName: ")
        print(pick_list_value.get_sys_ref_name())
        print("\nField PickListValue Type: ")
        print(pick_list_value.get_type())


module = "Leads"
GetLayouts.initialize()
GetLayouts.get_layouts(module)