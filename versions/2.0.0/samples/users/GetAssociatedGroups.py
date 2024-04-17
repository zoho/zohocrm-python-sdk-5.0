from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.users import UsersOperations, AssociatedGroupsWrapper, APIException


class GetAssociatedGroups(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_associated_groups(user_id):
        user_opeerations = UsersOperations()
        response = user_opeerations.get_associated_groups(user_id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, AssociatedGroupsWrapper):
                associated_groups_wrapper = response_object
                user_groups = associated_groups_wrapper.get_user_groups()
                if user_groups is not None:
                    for userGroup in user_groups:
                        print("AssociateGroup ID : " + str(userGroup.get_id()))
                        print("AssociateGroup Name : " + userGroup.get_name())
                        print("AssociateGroup Description : " + userGroup.get_description())
                        print("AssociateGroup CreatedTime : " + str(userGroup.get_created_time()))
                        print("AssociateGroup ModifiedTime : " + str(userGroup.get_modified_time()))
                        createdBy = userGroup.get_created_by()
                        if createdBy is not None:
                            print("AssociateGroup CreatedBy ID : " + str(createdBy.get_id()))
                            print("AssociateGroup CreatedBy Name : " + createdBy.get_name())
                            print("AssociateGroup CreatedBy Email : " + str(createdBy.get_email()))
                        modifiedBy = userGroup.get_modified_by()
                        if modifiedBy is not None:
                            print("AssociateGroup modifiedBy ID : " + str(modifiedBy.get_id()))
                            print("AssociateGroup modifiedBy Name : " + modifiedBy.get_name())
                            print("AssociateGroup modifiedBy Email : " + str(modifiedBy.get_email()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


GetAssociatedGroups.initialize()
GetAssociatedGroups.get_associated_groups(user_id=4402480254001)