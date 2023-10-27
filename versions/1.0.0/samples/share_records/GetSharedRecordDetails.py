from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.share_records import ShareRecordsOperations, GetSharedRecordDetailsParam, \
    ResponseWrapper, APIException


class GetSharedRecordDetails:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_shared_record_details(module_api_name, record_id):
        """
        This method is used to get the details of a shared record and print the response.
        :param module_api_name: The API Name of the module to get shared record details.
        :param record_id: The ID of the record to be obtain shared information
        :return:
        """
        """
        example
        module_api_name = Contacts
        record_id = 3409643002112011
        """
        shared_records_operations = ShareRecordsOperations(record_id, module_api_name)
        param_instance = ParameterMap()
        # Possible parameters of Get Shared Record Details operation
        # Allowed values - summary, manage
        param_instance.add(GetSharedRecordDetailsParam.view, 'summary')
        # param_instance.add(GetSharedRecordDetailsParam.sharedto, 34096430302031)
        # Call get_shared_record_details method that takes ParameterMap instance as parameter
        response = shared_records_operations.get_shared_record_details(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    share_records_list = response_object.get_share()
                    for share_record in share_records_list:
                        print("ShareRecord ShareRelatedRecords: " + str(share_record.get_share_related_records()))
                        shared_through = share_record.get_shared_through()
                        if shared_through is not None:
                            module = shared_through.get_module()
                            if module is not None:
                                print("ShareRecord SharedThrough Module ID: " + str(module.get_id()))
                                print("ShareRecord SharedThrough Module Name: " + str(module.get_name()))
                            print("ShareRecord SharedThrough ID: " + str(shared_through.get_id()))
                        print("ShareRecord Permission: " + str(share_record.get_permission()))
                        print("ShareRecord SharedTime: " + str(share_record.get_shared_time()))
                        shared_by = share_record.get_shared_by()
                        if shared_by is not None:
                            print("ShareRecord SharedBy-ID: " + str(shared_by.get_id()))
                            print("ShareRecord SharedBy-FullName: " + str(shared_by.get_full_name()))
                            print("ShareRecord SharedBy-Zuid: " + str(shared_by.get_zuid()))
                        user = share_record.get_user()
                        if user is not None:
                            print("ShareRecord User-ID: " + str(user.get_id()))
                            print("ShareRecord User-FullName: " + str(user.get_full_name()))
                            print("ShareRecord User-Zuid: " + str(user.get_zuid()))
                    shareable_users = response_object.get_shareable_user()
                    if shareable_users is not None:
                        for shareable_user in shareable_users:
                            print("Shareable User-ID: " + str(shareable_user.get_id()))
                            print("Shareable User-FullName: " + str(shareable_user.get_full_name()))
                            print("Shareable User-Zuid: " + str(shareable_user.get_zuid()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


module_api_name = "Leads"
record_id = 440248001483007
GetSharedRecordDetails.initialize()
GetSharedRecordDetails.get_shared_record_details(module_api_name, record_id)