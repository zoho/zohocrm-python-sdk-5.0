from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.tags import TagsOperations, GetRecordCountForTagParam, APIException, \
    CountResponseWrapper


class GetRecordCountForTag:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)
        
    @staticmethod
    def get_record_count_for_tag(module_api_name, tag_id):
        """
        This method is used to get the total number of records under a tag and print the response.
        :param module_api_name: The API Name of the module.
        :param tag_id: The ID of the tag to get the count
        """
        """
        example
        module_api_name = "Leads"
        tag_id = 34096430661047
        """
        tags_operations = TagsOperations()
        param_instance = ParameterMap()
        # Possible parameters for Get Record Count operation
        param_instance.add(GetRecordCountForTagParam.module, module_api_name)
        # Call get_record_count_for_tag method that takes param_instance and tag_id as parameter
        response = tags_operations.get_record_count_for_tag(tag_id, param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, CountResponseWrapper):
                    print("Tag Count: " + response_object.get_count())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


GetRecordCountForTag.initialize()
GetRecordCountForTag.get_record_count_for_tag(module_api_name="Leads", tag_id=440248001390027)