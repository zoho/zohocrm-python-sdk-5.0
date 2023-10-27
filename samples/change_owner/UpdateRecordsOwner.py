from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.change_owner import ChangeOwnerOperations, MassWrapper, Owner, RelatedModules, \
    ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class UpdateRecordsOwner(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_records_owner(module_api_name):
        change_owner_operations = ChangeOwnerOperations(module_api_name)
        body_wrapper = MassWrapper()
        ids = [440248001409012,440248001409007]
        body_wrapper.set_ids(ids)
        owner = Owner()
        owner.set_id(4402480254001)
        body_wrapper.set_owner(owner)
        body_wrapper.set_notify(False)
        related_modules = []
        related_module = RelatedModules()
        related_module.set_id(440248001438054)
        related_module.set_api_name("Tasks")
        related_modules.append(related_module)
        related_module = RelatedModules()
        related_module.set_id(344798655243)
        related_module.set_api_name("Tasks")
        related_modules.append(related_module)
        body_wrapper.set_related_modules(related_modules)
        response = change_owner_operations.mass_update(body_wrapper)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_data()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message())
                        elif isinstance(action_response, APIException):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message())

                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


module= "Leads"
UpdateRecordsOwner.initialize()
UpdateRecordsOwner.update_records_owner(module)