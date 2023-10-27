from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.related_lists import RelatedListsOperations, ResponseWrapper, APIException, \
    GetRelatedListsParam


class GetRelatedLists:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_related_lists(module_api_name, layout_id):
        """
        This method is used to get the related list data of a particular module and print the response.
        :param module_api_name: The API Name of the module to get related lists
        """
        """
        example
        module_api_name = "Leads";
        """
        related_lists_operations = RelatedListsOperations(layout_id)
        param_instance = ParameterMap()
        param_instance.add(GetRelatedListsParam.module, module_api_name)
        # Call get_related_lists method
        response = related_lists_operations.get_related_lists(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    related_lists = response_object.get_related_lists()
                    for related_list in related_lists:
                        print("RelatedList SequenceNumber: " + str(related_list.get_sequence_number()))
                        print("RelatedList DisplayLabel: " + str(related_list.get_display_label()))
                        print("RelatedList APIName: " + str(related_list.get_api_name()))
                        print("RelatedList Module: " + str(related_list.get_module()))
                        print("RelatedList Name: " + str(related_list.get_name()))
                        print("RelatedList Action: " + str(related_list.get_action()))
                        print("RelatedList ID: " + str(related_list.get_id()))
                        print("RelatedList Href: " + str(related_list.get_href()))
                        print("RelatedList Type: " + str(related_list.get_type()))
                        print("RelatedList Connectedmodule: " + str(related_list.get_connectedmodule()))
                        print("RelatedList Linkingmodule: " + str(related_list.get_linkingmodule()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


module = "Leads"
layout_id = 4402480167
GetRelatedLists.initialize()
GetRelatedLists.get_related_lists(module, layout_id)