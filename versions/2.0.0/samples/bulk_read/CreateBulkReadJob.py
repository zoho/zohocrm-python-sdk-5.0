from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.bulk_read import BulkReadOperations, RequestWrapper, CallBack, Query, Criteria, \
    ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.fields import MinifiedField
from zohocrmsdk.src.com.zoho.crm.api.modules import MinifiedModule
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class CreateBulkReadJob(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_bulk_read_job(module_api_name):
        """
        This method is used to create a bulk read job to export records.
        :param module_api_name: The API Name of the record's module
        """
        """
        example
        module_api_name = 'Leads'
        """
        bulk_read_operations = BulkReadOperations()
        request = RequestWrapper()
        call_back = CallBack()
        call_back.set_url("https://www.example.com/callback")
        call_back.set_method(Choice('post'))
        # The Bulk Read Job's details is posted to this URL on successful completion / failure of the job.
        request.set_callback(call_back)
        query = Query()
        # Specifies the API Name of the module to be read.
        module = MinifiedModule()
        module.set_api_name(module_api_name)
        query.set_module(module)
        # Specifies the unique ID of the custom view, whose records you want to export.
        # query.set_cvid('34096430087501')
        # List of field names
        field_api_names = ['Last_Name']
        # Specifies the API Name of the fields to be fetched
        # query.set_fields(field_api_names)
        # To set page value, By default value is 1.
        query.set_page(1)
        criteria = Criteria()
        # To set comparator(eg: equal, greater_than)
        criteria.set_group_operator(Choice('or'))
        criteria_array = []
        group11 = Criteria()
        group11.set_group_operator(Choice("and"))
        group_array11 = []
        group111 = Criteria()
        field1 = MinifiedField()
        field1.set_api_name("Company")
        group111.set_field(field1)
        group111.set_comparator(Choice("equal"))
        group111.set_value("Zoho")
        group_array11.append(group111)
        group112 = Criteria()
        field2 = MinifiedField()
        field2.set_api_name("Owner")
        group112.set_field(field2)
        group112.set_comparator(Choice("in"))
        group112.set_value(["34770610173021"])
        group_array11.append(group112)
        group11.set_group(group_array11)
        criteria_array.append(group11)
        group12 = Criteria()
        group12.set_group_operator(Choice("or"))
        group_array12 = []
        group121 = Criteria()
        field3 = MinifiedField()
        field3.set_api_name("Paid")
        group121.set_field(field3)
        group121.set_comparator(Choice("equal"))
        group121.set_value(True)
        group_array12.append(group121)
        group122 = Criteria()
        field4 = MinifiedField()
        field4.set_api_name("Created_Time")
        group122.set_field(field4)
        group122.set_comparator(Choice("between"))
        time = ["2020-06-03T17:31:48+05:30", "2020-06-03T17:31:48+05:30"]
        # To set the value to be compared
        group122.set_value(time)
        group_array12.append(group122)
        group12.set_group(group_array12)
        criteria_array.append(group12)
        criteria.set_group(criteria_array)
        # To filter the records to be exported
        query.set_criteria(criteria)
        request.set_query(query)
        # Specify the value for this key as "ics" to export all records in the Events module as an ICS file.
        # request.set_file_type(Choice('ics'))
        # Call create_bulk_read_job method that takes RequestWrapper instance as parameter
        response = bulk_read_operations.create_bulk_read_job(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_data()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message().get_value())
                        elif isinstance(action_response, APIException):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message().get_value())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


module_api_name = "Leads"
CreateBulkReadJob.initialize()
CreateBulkReadJob.create_bulk_read_job(module_api_name)