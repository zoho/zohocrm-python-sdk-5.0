from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.fields import FieldsOperations, GetFieldsParam, BodyWrapper, APIException


class GetFields:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_fields(module_api_name):
        """
        This method is used to get metadata about all the fields of a module and print the response.
        :param module_api_name: The API Name of the module to get fields
        """
        """
        example
        module_api_name = "Leads";
        """
        fields_operations = FieldsOperations()
        param_instance = ParameterMap()
        # Possible parameters for get_fields operation
        param_instance.add(GetFieldsParam.module, module_api_name)
        response = fields_operations.get_fields(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code()
                                      == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, BodyWrapper):
                    fields_list = response_object.get_fields()
                    for field in fields_list:

                        print("Webhook: " + str(field.get_webhook()))
                        print("JsonType: " + str(field.get_json_type()))
                        print("DisplayLabel: " + field.get_display_label())
                        print("SystemMandatory: " +
                              str(field.get_system_mandatory()))
                        print("\n Field is Private :")
                        print(field.get_private())
                        print("\n Field is UiType :")
                        print(field.get_ui_type())
                        print("\n Field  PickListValuesSortedLexically :")
                        print(field.get_pick_list_values_sorted_lexically())
                        print("DataType: " + field.get_data_type().get_value())
                        print("ColumnName: " + str(field.get_column_name()))
                        print("ID: " + str(field.get_id()))
                        print("Sortable: " + str(field.get_sortable()))
                        if field.get_external() is not None:
                            external = field.get_external()
                            print("External Show: " +
                                  str(external.get_show()))
                            print("External Type: " +
                                  str(external.get_type()))
                            print("External Type: " +
                                  str(external.get_allow_multiple_config()))
                        if field.get_unique() is not None:
                            print(
                                "Mandatory: ")
                            print(field.get_unique().get_casesensitive())
                        if field.get_history_tracking() is not None:
                            history_tracking = field.get_history_tracking()
                            module = history_tracking.get_module()
                            if module is not None:
                                module_layout = module.get_layout()
                                if module_layout is not None:
                                    print("Module layout id: " +
                                          str(module_layout.get_id()))
                                    print("Module display label: " +
                                          str(module.get_api_name()))
                                    print("Module api name: " +
                                          str(module.get_id()))
                                    print("Module module: " +
                                          str(module.get_module()))
                                    print("Module module name: " +
                                          str(module.get_module_name()))
                            duration_configured = history_tracking.get_duration_configured_field()
                            if duration_configured is not None:
                                print(
                                    "historytracking duration configured field: " + str(duration_configured.get_id()))
                        print("APIName : " + str(field.get_api_name()))
                        crypt = field.get_crypt()
                        if crypt is not None:
                            print("Crypt Details")
                            print("Mode: " + crypt.get_mode())
                            print("Column: ")
                            print(crypt.get_column())
                            print("Table: ")
                            print(crypt.get_table())
                            print("Status: ")
                            print(crypt.get_status())
                            print("\n Crypt Notify:")
                            print(crypt.get_notify())
                            enc_fld_ids = crypt.get_encfldids()
                            if enc_fld_ids is not None:
                                print("\nEncFldIds : ")
                                for enc_fld_id in enc_fld_ids:
                                    print(enc_fld_id)
                        print("FieldLabel: " + str(field.get_field_label()))
                        tool_tip = field.get_tooltip()
                        if tool_tip is not None:
                            print("ToolTip Name: " + tool_tip.get_name())
                            print("ToolTip Value: " + tool_tip.get_value())
                        currency = field.get_currency()
                        if currency is not None:
                            print("Currency RoundingOption: ")
                            print(currency.get_rounding_option())
                            print("Currency Precision: ")
                            print(currency.get_precision())
                        print("CreatedSource: " +
                              str(field.get_created_source()))
                        if field.get_display_type() is not None:
                            print("Field DisplayType: ")
                            print(field.get_display_type())
                        print("FieldReadOnly: " +
                              str(field.get_field_read_only()))
                        print("Filterable: " + str(field.get_filterable()))
                        if field.get_read_only() is not None:
                            print("ReadOnly: " + str(field.get_read_only()))
                        association_details = field.get_association_details()
                        if association_details is not None:
                            lookup_field = association_details.get_lookup_field()
                            if lookup_field is not None:
                                print(
                                    "AssociationDetails LookupField ID: " + lookup_field.get_id())
                                print(
                                    'AssociationDetails LookupField Name: ' + lookup_field.get_name())
                            related_field = association_details.get_related_field()
                            if related_field is not None:
                                print(
                                    "AssociationDetails RelatedField ID: " + related_field.get_id())
                                print(
                                    'AssociationDetails RelatedField Name: ' + related_field.get_name())
                        if field.get_quick_sequence_number() is not None:
                            print('QuickSequenceNumber: ' +
                                  str(field.get_quick_sequence_number()))
                        print("DisplayLabel: " + field.get_display_label())
                        if field.get_custom_field() is not None:
                            print("CustomField: " +
                                  str(field.get_custom_field()))
                        if field.get_visible() is not None:
                            print("Visible: " + str(field.get_visible()))
                        if field.get_length() is not None:
                            print("Length: " + str(field.get_length().get_value()))
                        if field.get_decimal_place() is not None:
                            print("DecimalPlace: " +
                                  str(field.get_decimal_place()))
                        print("Field BusinesscardSupported :" + str(field.get_businesscard_supported()))
                        view_type = field.get_view_type()
                        if view_type is not None:
                            print("View: " + str(view_type.get_view()))
                            print("Edit: " + str(view_type.get_edit()))
                            print("Create: " + str(view_type.get_create()))
                            print("QuickCreate: " +
                                  str(view_type.get_quick_create()))
                        pick_list_values = field.get_pick_list_values()
                        if pick_list_values is not None:
                            for pick_list_value in pick_list_values:
                                GetFields.print_pick_list_value(pick_list_value)
                        multi_module_lookup = field.get_multi_module_lookup()
                        if multi_module_lookup is not None:
                            print("Lookup apiname: " +
                                  str(multi_module_lookup.get_api_name()))
                            module = multi_module_lookup.get_modules()
                            if module is not None:
                                print("module Id: " + module.get_id())
                                print("module Id: " +
                                      module.get_api_name())
                        multi_select_lookup = field.get_multiselectlookup()
                        if multi_select_lookup is not None:
                            print(
                                "DisplayLabel: " + str(multi_select_lookup.get_display_label()))
                            print(
                                "LinkingModule: " + str(multi_select_lookup.get_linking_module()))
                            print(
                                "LookupApiname: " + str(multi_select_lookup.get_lookup_apiname()))
                            print("APIName: " +
                                  str(multi_select_lookup.get_api_name()))
                            print(
                                "ConnectedlookupApiname: " + str(multi_select_lookup.get_connectedlookup_apiname()))
                            print("ID: " + str(multi_select_lookup.get_id()))
                            print(
                                "Connected Module: " + str(multi_select_lookup.get_connected_module()))
                        multi_user_lookup = field.get_multiuserlookup()
                        if multi_user_lookup is not None:
                            print("DisplayLabel: " +
                                  str(multi_user_lookup.get_display_label()))
                            print("LinkingModule: " +
                                  str(multi_user_lookup.get_linking_module()))
                            print("LookupApiname: " +
                                  str(multi_user_lookup.get_lookup_apiname()))
                            print("APIName: " +
                                  str(multi_user_lookup.get_api_name()))
                            print(
                                "ConnectedlookupApiname: " + str(multi_user_lookup.get_connectedlookup_apiname()))
                            print("ID: " + str(multi_user_lookup.get_id()))
                            print("Connected Module: " +
                                  str(multi_user_lookup.get_connected_module()))
                        lookup = field.get_lookup()
                        if lookup is not None:
                            module = lookup.get_module()
                            if module is not None:
                                print("Field ModuleLookup Module APIName: " + module.get_api_name())
                                print("Field ModuleLookup Module Id: " + str(module.get_id()))
                            query_details = lookup.get_query_details()
                            if query_details is not None:
                                print("Field ModuleLookup QueryDetails Query Id: " + str(query_details.get_query_id()))
                            print("Field ModuleLookup DisplayLabel: ")
                            print(lookup.get_display_label())
                            print("Field ModuleLookup APIName: ")
                            print(lookup.get_api_name())
                            print("Field ModuleLookup ID: ")
                            print(str(lookup.get_id()))
                        auto_number = field.get_auto_number()
                        if field.get_convert_mapping() is not None:
                            convert_mapping = field.get_convert_mapping()
                            print(convert_mapping.get_accounts())
                            print(convert_mapping.get_contacts())
                            print(convert_mapping.get_deals())
                        profiles = field.get_profiles()
                        for profile in profiles:
                            print("\n Field Profile PermissionType: ")
                            print(profile.get_permission_type())
                            print("\n Field Profile Name: ")
                            print(profile.get_name())
                            print("\n Field Profile ID: ")
                            print(profile.get_id())
                        if auto_number is not None:
                            print('Prefix: ' + str(auto_number.get_prefix()))
                            print('Suffix: ' + str(auto_number.get_suffix()))
                            if auto_number.get_start_number() is not None:
                                print('Start Number: ' +
                                      str(auto_number.get_start_number()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())

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
                        GetFields.print_pick_list_value(plv)
        print("\nField PickListValue SysRefName: ")
        print(pick_list_value.get_sys_ref_name())
        print("\nField PickListValue Type: ")
        print(pick_list_value.get_type())

    @staticmethod
    def print_criteria(criteria):
        if criteria.get_comparator() is not None:
            print('CustomView Criteria Comparator: ' + criteria.get_comparator().get_value())
        if criteria.get_field() is not None:
            print('CustomView Criteria Field: ' + criteria.get_field().get_api_name())
        if criteria.get_value() is not None:
            print('CustomView Criteria Value: ' + str(criteria.get_value()))
        criteria_group = criteria.get_group()
        if criteria_group is not None:
            for each_criteria in criteria_group:
                GetFields.print_criteria(each_criteria)
        if criteria.get_group_operator() is not None:
            print('CustomView Criteria Group Operator: ' + criteria.get_group_operator().get_value())


module_api_name = "Leads"
GetFields.initialize()
GetFields.get_fields(module_api_name)