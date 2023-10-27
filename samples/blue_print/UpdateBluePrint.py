from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.blueprint import BlueprintOperations, BodyWrapper, BluePrint, SuccessResponse, \
    APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import Record


class UpdateBluePrint(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_blueprint(module_api_name, record_id, transition_id):
        """
        This method is used to update a single record's Blueprint details with ID and print the response.
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to update Blueprint
        :param transition_id: The ID of the Blueprint transition Id
        """
        """
        example
        module_api_name = "Leads"
        record_id = 3409643002469044
        transition_id = 3409643001172075
        """
        blue_print_operations = BlueprintOperations(record_id, module_api_name)
        request = BodyWrapper()
        # List to contain BluePrint instances
        blue_print_list = []
        blue_print = BluePrint()
        blue_print.set_transition_id(transition_id)
        data = Record()
        lookup = dict()
        lookup['id'] = '8940372937'
        data.add_key_value('Data_3', lookup)
        data.add_key_value('Phone', '8940372937')
        data.add_key_value("Notes", "Updated via blueprint")
        check_list_item = {'item1': True}
        check_list_item_2 = {'item1': True}
        check_list_item_3 = {'item1': True}
        check_lists = [check_list_item, check_list_item_2, check_list_item_3]
        data.add_key_value("CheckLists", check_lists)
        blue_print.set_data(data)
        # Add BluePrint instance to the list
        blue_print_list.append(blue_print)
        request.set_blueprint(blue_print_list)
        # Call update_blueprint method that takes BodyWrapper instance as parameter
        response = blue_print_operations.update_blueprint(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, SuccessResponse):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


module = "Leads"
record_id = 440248001560044
transition_id = 4402480258363
UpdateBluePrint.initialize()
UpdateBluePrint.update_blueprint(module, record_id, transition_id)