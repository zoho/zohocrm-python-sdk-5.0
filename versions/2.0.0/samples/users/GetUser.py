from datetime import datetime
from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.users import UsersOperations, GetUserHeader, ResponseWrapper, APIException


class GetUser:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_user(user_id):
        """
        This method is used to get the details of any specific user with ID
        :param user_id: The ID of the User to be obtained
        """
        """
        example
        user_id = 34096430302031
        """
        users_operations = UsersOperations()
        header_instance = HeaderMap()
        # Possible headers for Get User operation
        header_instance.add(GetUserHeader.if_modified_since, datetime.fromisoformat('2019-07-07T10:00:00+05:30'))
        # Call get_user method that takes HeaderMap instance and user_id as parameters
        response = users_operations.get_user(user_id, header_instance)
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
                        print("User DateFormat: " + str(user.get_date_format().get_value()))
                        print("User Status: " + str(user.get_status()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


user_id = 4402480015011
GetUser.initialize()
GetUser.get_user(user_id)