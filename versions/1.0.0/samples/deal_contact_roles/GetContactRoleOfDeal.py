from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.deal_contact_roles import DealContactRolesOperations, APIException, ContactRole, \
    BodyWrapper


class GetContactRoleOfDeal(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_contact_role_of_deal(contact_id, deal_id):
        contact_roles_operations = DealContactRolesOperations()
        response = contact_roles_operations.get_associated_contact_roles_specific_to_contact(contact_id, deal_id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, BodyWrapper):
                response_wrapper = response_object
                records = response_wrapper.get_data()
                for record in records:
                    print("Record ID: " + str(record.get_id()))
                    created_by = record.get_created_by()
                    if created_by is not None:
                        print("Record Created By User-ID: " + str(created_by.get_id()))
                        print("Record Created By User-Name: " + created_by.get_name())
                        print("Record Created By User-Email: " + created_by.get_email())
                    print("Record CreatedTime : " + str(record.get_created_time()))
                    modified_by = record.get_modified_by()
                    if modified_by is not None:
                        print("Record Modified By User-ID: " + str(modified_by.get_id()))
                        print("Record Modified By User-Name: " + modified_by.get_name())
                        print("Record Modified By User-Email: " + modified_by.get_email())
                    print("Record ModifiedTime: " + str(record.get_modified_time()))
                    # to get a particular field value
                    print("Record Field Value: " + record.get_key_value("Last_Name"))
                    print("Record KeyValues: ")

                    for key, value in record.get_key_values().items():
                        if isinstance(value, list):
                            print("Record keyName: " + key)
                            data_list = value
                            for data in data_list:
                                if isinstance(data, dict):
                                    print("Record KeyName : " + key + " - value : ")
                                    for key1, value1 in data:
                                        print(key1 + " : " + value1)
                                else:
                                    print(data)
                        elif isinstance(value, ContactRole):
                            contact_role = value
                            if contact_role is not None:
                                print("Record ContactRole Name: " + contact_role.get_name())
                                print("Record ContactRole Id: " + str(contact_role.get_id()))
                        elif isinstance(value, dict):
                            print("record keyName : " + key + " - value: ")
                            for key2, value2 in value.items():
                                print(key2 + " : " + str(value2))
                        else:
                            print("Record keyName : " + key + " - value : " + str(value))

                info = response_wrapper.get_info()
                if info is not None:
                    if info.get_count() is not None:
                        print("Record Info Count: " + str(info.get_count()))
                    if info.get_more_records() is not None:
                        print("Record Info MoreRecords: " + str(info.get_more_records()))

            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


deal_id = 440248001393069
contact_id = 440248001393062
GetContactRoleOfDeal.initialize()
GetContactRoleOfDeal.get_contact_role_of_deal(contact_id, deal_id)
