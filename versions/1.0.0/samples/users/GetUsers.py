from datetime import datetime
from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.users import UsersOperations, GetUsersParam, GetUsersHeader, ResponseWrapper, \
    APIException


class GetUsers:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_users():
        """
        This method is used to retrieve the users data specified in the API request.
        """
        users_operations = UsersOperations()
        param_instance = ParameterMap()
        # Possible parameters for Get Users operation
        # param_instance.add(GetUsersParam.page, 1)
        # param_instance.add(GetUsersParam.per_page, 200)
        param_instance.add(GetUsersParam.type, 'ActiveConfirmedUsers')
        header_instance = HeaderMap()
        # Possible headers for Get Users operation
        header_instance.add(GetUsersHeader.if_modified_since, datetime.fromisoformat('2019-07-07T10:00:00+05:30'))
        # Call get_users method that takes ParameterMap instance and HeaderMap instance as parameters
        response = users_operations.get_users(param_instance, header_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    user_list = response_object.get_users()
                    for user in user_list:
                        print("User Country: " + str(user.get_country()))
                        customize_info = user.get_customize_info()
                        if customize_info is not None:
                            if customize_info.get_notes_desc() is not None:
                                print("User CustomizeInfo NotesDesc: " + str(customize_info.get_notes_desc()))
                            if customize_info.get_show_right_panel() is not None:
                                print(
                                    "User CustomizeInfo ShowRightPanel: " + str(customize_info.get_show_right_panel()))
                            if customize_info.get_bc_view() is not None:
                                print("User CustomizeInfo BcView: " + str(customize_info.get_bc_view()))
                            if customize_info.get_show_home() is not None:
                                print("User CustomizeInfo ShowHome: " + str(customize_info.get_show_home()))
                            if customize_info.get_show_detail_view() is not None:
                                print(
                                    "User CustomizeInfo ShowDetailView: " + str(customize_info.get_show_detail_view()))
                            if customize_info.get_unpin_recent_item() is not None:
                                print("User CustomizeInfo UnpinRecentItem: " + str(
                                    customize_info.get_unpin_recent_item()))
                        role = user.get_role()
                        if role is not None:
                            print("User Role Name: " + str(role.get_name()))
                            print("User Role ID: " + str(role.get_id()))
                        print("User Signature: " + str(user.get_signature()))
                        print("User SortOrderPreference: " + str(user.get_sort_order_preference()))
                        print("User SandboxDeveloper: " + str(user.get_sandboxdeveloper()))
                        print("User City: " + str(user.get_city()))
                        print("User Language: " + str(user.get_language()))
                        print("User Locale: " + str(user.get_locale()))
                        print("User Microsoft: " + str(user.get_microsoft()))
                        if user.get_personal_account() is not None:
                            print("User PersonalAccount: " + str(user.get_personal_account()))
                        print("User DefaultTabGroup: " + str(user.get_default_tab_group()))
                        print("User Isonline: " + str(user.get_isonline()))
                        modified_by = user.get_modified_by()
                        if modified_by is not None:
                            print("User Modified By User-Name: " + str(modified_by.get_name()))
                            print("User Modified By User-ID: " + str(modified_by.get_id()))
                        print("User Street: " + str(user.get_street()))
                        print("User Currency: " + str(user.get_currency()))
                        print("User Alias: " + str(user.get_alias()))
                        theme = user.get_theme()
                        if theme is not None:
                            normal_tab = theme.get_normal_tab()
                            if normal_tab is not None:
                                print("User Theme NormalTab FontColor: " + str(normal_tab.get_font_color()))
                                print("User Theme NormalTab Background: " + str(normal_tab.get_background()))
                            selected_tab = theme.get_selected_tab()
                            if selected_tab is not None:
                                print("User Theme Selected Tab FontColor: " + str(selected_tab.get_font_color()))
                                print("User Theme Selected Tab Background: " + str(selected_tab.get_background()))
                            print("User Theme NewBackground: " + str(theme.get_new_background()))
                            print("User Theme Background: " + str(theme.get_background()))
                            print("User Theme Screen: " + str(theme.get_screen()))
                            print("User Theme Type: " + str(theme.get_type()))
                        print("User ID: " + str(user.get_id()))
                        print("User State: " + str(user.get_state()))
                        print("User Fax: " + str(user.get_fax()))
                        print("User CountryLocale: " + str(user.get_country_locale()))
                        print("User FirstName: " + str(user.get_first_name()))
                        print("User Email: " + str(user.get_email()))
                        reporting_to = user.get_reporting_to()
                        if reporting_to is not None:
                            print("User ReportingTo User-Name: " + str(reporting_to.get_name()))
                            print("User ReportingTo User-ID: " + str(reporting_to.get_id()))
                        print("User DecimalSeparator: " + str(user.get_decimal_separator()))
                        print("User Zip: " + str(user.get_zip()))
                        print("User CreatedTime: " + str(user.get_created_time()))
                        print("User Website: " + str(user.get_website()))
                        if user.get_modified_time() is not None:
                            print("User ModifiedTime: " + str(user.get_modified_time()))
                        print("User TimeFormat: " + str(user.get_time_format()))
                        print("User Offset: " + str(user.get_offset()))
                        profile = user.get_profile()
                        if profile is not None:
                            print("User Profile Name: " + str(profile.get_name()))
                            print("User Profile ID: " + str(profile.get_id()))
                        print("User Mobile: " + str(user.get_mobile()))
                        print("User LastName: " + str(user.get_last_name()))
                        print("User TimeZone: " + str(user.get_time_zone()))
                        print("Custom Field: " + str(user.get_key_value('Custom_Field')))
                        created_by = user.get_created_by()
                        if created_by is not None:
                            print("User Created By User-Name: " + str(created_by.get_name()))
                            print("User Created By User-ID: " + str(created_by.get_id()))
                        print("User Zuid: " + str(user.get_zuid()))
                        print("User Confirm: " + str(user.get_confirm()))
                        print("User FullName: " + str(user.get_full_name()))
                        print("User Phone: " + str(user.get_phone()))
                        print("User DOB: " + str(user.get_dob()))
                        print("User DateFormat: " + str(user.get_date_format()))
                        print("User Status: " + str(user.get_status()))
                    info = response_object.get_info()
                    if info is not None:
                        if info.get_per_page() is not None:
                            print("User Info PerPage: " + str(info.get_per_page()))
                        if info.get_count() is not None:
                            print("User Info Count: " + str(info.get_count()))
                        if info.get_page() is not None:
                            print("User Info Page: " + str(info.get_page()))
                        if info.get_more_records() is not None:
                            print("User Info MoreRecords: " + str(info.get_more_records()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


GetUsers.initialize()
GetUsers.get_users()