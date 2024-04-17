from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.blueprint import BlueprintOperations, ResponseWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class GetBluePrint(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_blueprint(module_api_name, record_id):
        """
        This method is used to get a single record's Blueprint details with ID and print the response.
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to get Blueprint
        """
        """
        example
        module_api_name = "Leads"
        record_id = 3409643002469044
        """
        blue_print_operations = BlueprintOperations(record_id, module_api_name)
        # Call get_blueprint method
        response = blue_print_operations.get_blueprint()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code()
                                      == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    blue_print = response_object.get_blueprint()
                    process_info = blue_print.get_process_info()
                    if process_info is not None:
                        print("ProcessInfo ID: " + str(process_info.get_id()))
                        print("ProcessInfo Field-ID: " +
                              str(process_info.get_field_id()))
                        print("ProcessInfo isContinuous: " +
                              str(process_info.get_is_continuous()))
                        print("ProcessInfo API Name: " +
                              process_info.get_api_name())
                        print("ProcessInfo Continuous: " +
                              str(process_info.get_continuous()))
                        print("ProcessInfo FieldLabel: " +
                              process_info.get_field_label())
                        print("ProcessInfo Name: " + process_info.get_name())
                        print("ProcessInfo ColumnName: " +
                              process_info.get_column_name())
                        print("ProcessInfo FieldValue: " +
                              process_info.get_field_value())
                        print("ProcessInfo FieldName: " +
                              process_info.get_field_name())
                        print("ProcessInfo Escalation: " +
                              str(process_info.get_escalation()))
                        escalation = process_info.get_escalation()
                        if escalation is not None:
                            print("\n Escalation days: ")
                            print(escalation.get_days())
                            print("\n Escalation status: ")
                            print(escalation.get_status())
                    transitions = blue_print.get_transitions()
                    for transition in transitions:
                        next_transitions = transition.get_next_transitions()
                        for next_transition in next_transitions:
                            print("NextTransition ID: " +
                                  next_transition.get_id())
                            print("NextTransition Name: " +
                                  next_transition.get_name())
                            print("NextTransition criteria_matched: " +
                                  next_transition.get_criteria_matched())
                            print("NextTransition type: " +
                                  next_transition.get_type())
                        parent_transition = transition.get_parent_transition()
                        if parent_transition is not None:
                            print("\n Parenttransition ID: ")
                            print(parent_transition.get_id())
                        data = transition.get_data()
                        if data is not None:
                            print("Record ID: " + str(data.get_id()))
                            created_by = data.get_created_by()
                            if created_by is not None:
                                print("Record Created By - Name: " +
                                      created_by.get_name())
                                print("Record Created By - ID: " +
                                      created_by.get_id())
                            print("Record CreatedTime: " +
                                  str(data.get_created_time()))
                            if data.get_modified_time() is not None:
                                print("Record ModifiedTime: " +
                                      str(data.get_modified_time()))
                            modified_by = data.get_modified_by()
                            if modified_by is not None:
                                print("Record Modified By - Name: " +
                                      modified_by.get_name())
                                print("Record Modified By - ID: " +
                                      modified_by.get_id())
                            tags = data.get_tag()
                            if tags is not None:
                                for tag in tags:
                                    print("Record Tag Name: " + tag.get_name())
                                    print("Record Tag ID: " + tag.get_id())
                            for key, value in data.get_key_values().items():
                                print(key + " : " + str(value))
                        print("Transition NextFieldValue: " +
                              str(transition.get_next_field_value()))
                        print("Transition Name: " + str(transition.get_name()))
                        print("Transition CriteriaMatched: " +
                              str(transition.get_criteria_matched()))
                        print("Transition ID: " + str(transition.get_id()))
                        print("Transition Execution Time: " +
                              str(transition.get_execution_time()))
                        print("Transition CriteriaMessage: " +
                              str(transition.get_criteria_message()))
                        print('Transition PercentPartialSave: ')
                        print(transition.get_percent_partial_save())
                        print('Transition ExecutionTime: ')
                        print(transition.get_execution_time())
                        print('Transition Type: ')
                        print(transition.get_type())
                        fields = transition.get_fields()
                        print("Transition Fields")
                        for field in fields:
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
                            print("DataType: " + field.get_data_type())
                            print("ColumnName: " + str(field.get_column_name()))
                            print("PersonalityName: " +
                                  str(field.get_personality_name()))
                            print("ID: " + str(field.get_id()))
                            print("Sortable: " + str(field.get_sortable()))
                            print("TransitionSequence: " +
                                  str(field.get_transition_sequence()))
                            if field.get_mandatory() is not None:
                                print("Mandatory: " +
                                      str(field.get_mandatory()))
                            if field.get_external() is not None:
                                external = field.get_external()
                                print("External Show: " +
                                      str(external.get_show()))
                                print("External Type: " +
                                      str(external.get_type()))
                                print("External Type: " +
                                      str(external.get_allow_multiple_config()))
                            if field.get_unique() is not None:
                                print("Casesensitive: " +
                                      str(field.get_unique().get_casesensitive()))
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
                                        "historytracking duration configured field: " + str(
                                            duration_configured.get_id()))
                            layout = field.get_layouts()
                            if layout is not None:
                                print("Layout ID: " + str(layout.get_id()))
                                print("Layout Name: " + str(layout.get_name()))
                            print("APIName : " + str(field.get_api_name()))
                            print("Content: " + str(field.get_content()))
                            crypt = field.get_crypt()
                            if crypt is not None:
                                print("Crypt Details")
                                print("Mode: " + crypt.get_mode())
                                print("Column: " + crypt.get_column())
                                print("Table: " + crypt.get_table())
                                print("Status: " + str(crypt.get_status()))
                            print("FieldLabel: " + str(field.get_field_label()))
                            tool_tip = field.get_tooltip()
                            if tool_tip is not None:
                                print("ToolTip Name: " + tool_tip.get_name())
                                print("ToolTip Value: " + tool_tip.get_value())
                            currency = field.get_currency()
                            if currency is not None:
                                print("Currency RoundingOption: " +
                                      str(currency.get_rounding_option()))
                                print("Currency Precision: " +
                                      str(currency.get_precision()))
                            print("CreatedSource: " +
                                  str(field.get_created_source()))
                            if field.get_display_type() is not None:
                                print("Field DisplayType: " +
                                      str(field.get_display_type().get_value()))
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
                                print("Length: " + str(field.get_length()))
                            if field.get_decimal_place() is not None:
                                print("DecimalPlace: " +
                                      str(field.get_decimal_place()))
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
                                    GetBluePrint.print_pick_list_value(
                                        pick_list_value)
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
                            multi_module_lookup = field.get_multi_module_lookup()
                            if multi_module_lookup is not None:
                                module = multi_module_lookup.get_modules()
                                if module is not None:
                                    print("module Id: " + module.get_id())
                                    print("module Id: " +
                                          module.get_api_name())
                            lookup = field.get_lookup()
                            if lookup is not None:
                                formula = field.get_formula()
                                if formula is not None:
                                    print("\nField Formula ReturnType : ")
                                    print(formula.get_return_type())
                                    if formula.get_expression() is not None:
                                        print("\nField Formula Expression : ")
                                        print(formula.get_expression())
                                if field.get_decimal_place() is not None:
                                    print("\nField DecimalPlace: ")
                                    print(field.get_decimal_place())
                                print("Field ModuleLookup DisplayLabel: ")
                                print(lookup.get_display_label())
                                print("Field ModuleLookup APIName: ")
                                print(lookup.get_api_name())
                                print("Field ModuleLookup Module: ")
                                print(str(lookup.get_module()))
                                print("Field ModuleLookup ID: ")
                                print(lookup.get_id())
                            auto_number = field.get_auto_number()
                            profiles = field.get_profiles()
                            if profiles is not None:
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
                    print("Message: " + response_object.get_message().get_value())

    @staticmethod
    def print_criteria(criteria):
        if criteria.get_comparator() is not None:
            print('Field Criteria Comparator: ' +
                  criteria.get_comparator().get_value())
        if criteria.get_field() is not None:
            print('Field Criteria Field: ' + criteria.get_field())
        if criteria.get_value() is not None:
            print('Field Criteria Value: ' + str(criteria.get_value()))
        criteria_group = criteria.get_group()
        if criteria_group is not None:
            for each_criteria in criteria_group:
                GetBluePrint.print_criteria(each_criteria)
        if criteria.get_group_operator() is not None:
            print('Field Criteria Group Operator: ' +
                  criteria.get_group_operator().get_value())

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
        for map in pick_list_value.get_maps():
            print("\n")
            print(map)
            pick_list_values = map.get_pick_list_values
            if pick_list_values is not None:
                for plv in pick_list_values:
                    GetBluePrint.print_pick_list_value(plv)
        print("\nField PickListValue SysRefName: ")
        print(pick_list_value.get_sys_ref_name())
        print("\nField PickListValue Type: ")
        print(pick_list_value.get_type())


module = "Leads"
record_id = "44024001560044"
GetBluePrint.initialize()
GetBluePrint.get_blueprint(module, record_id)