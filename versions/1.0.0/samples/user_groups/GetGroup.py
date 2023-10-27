from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.user_groups import UserGroupsOperations, ResponseWrapper, APIException


class GetGroup(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_group(group_id):
        user_group_operations = UserGroupsOperations()
        response = user_group_operations.get_group(group_id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                users = response_object.get_user_groups()
                for user in users:
                    created_by = user.get_created_by()
                    if created_by is not None:
                        print("UserGroups Created By User-Name: " + created_by.get_name())
                        print("UserGroups Created By User-ID: " + str(created_by.get_id()))
                    modifiedBy = user.get_modified_by()
                    if modifiedBy is not None:
                        print("UserGroups Modified By User-Name: " + modifiedBy.get_name())
                        print("UserGroups Modified By User-ID: " + str(modifiedBy.get_id()))
                    print("User ModifiedTime: " + str(user.get_modified_time()))
                    print("User CreatedTime: " + str(user.get_created_time()))
                    print("UserGroups Description: " + user.get_description())
                    print("UserGroups Id: " + str(user.get_id()))
                    print("UserGroups Name: " + user.get_name())
                    sources = user.get_sources()
                    if sources is not None:
                        for source in sources:
                            print("user_groups sources type: " + source.get_type().get_value())
                            source1 = source.get_source()
                            if source1 is not None:
                                print("UserGroups Sources Id : " + str(source1.get_id()))
                            print("userGroups sources subprdinates: " + source1.get_subordinates())
                            print("userGroups Sources subTerritories : " + source.get_sub_territories())
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


GetGroup.initialize()
GetGroup.get_group(group_id=440248001219057)