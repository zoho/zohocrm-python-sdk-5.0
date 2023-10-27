from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, ConversionOptionsResponseWrapper, APIException


class LeadConversionOptions:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def lead_conversion_options(record_id):
        record_operations = RecordOperations()
        module_api_name = "Leads"
        response = record_operations.lead_conversion_options(record_id, module_api_name)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ConversionOptionsResponseWrapper):
                conversion_option = response_object.get_conversionoptions()
                module = conversion_option.get_module_preference()
                if module is not None:
                    print("ConversionOptions ModulePreference API-Name: " + module.get_api_name())
                    print("ConversionOptions ModulePreference ID: " + str(module.get_id()))
                contacts = conversion_option.get_contacts()
                if contacts is not None:
                    for contact in contacts:
                        print("Record ID : " + str(contact.get_id()))
                        print("Record KeyValues: ")
                        for key, value in contact.get_key_values().items():
                            keyName = key
                            if isinstance(value, list):
                                print("Record KeyName : " + keyName)
                                dataList = value
                                for data in dataList:
                                    if isinstance(data, dict):
                                        print("Record KeyName : " + keyName + " - Value : ")
                                        for mapValue in data.items():
                                            print(mapValue[0] + " : " + str(mapValue[1]))
                                    else:
                                        print(data)
                            elif isinstance(value, dict):
                                print("Record KeyName : " + keyName + " - Value : ")
                                for mapValue in value.items():
                                    print(mapValue[0] + " : " + str(mapValue[1]))
                            else:
                                print("Record KeyName : " + keyName + " - Value : " + str(value))
                preference_field_matched_value = conversion_option.get_preference_field_matched_value()
                if preference_field_matched_value is not None:
                    contacts_preference_field = preference_field_matched_value.get_contacts()
                    if contacts_preference_field is not None:
                        for contact in contacts_preference_field:
                            print("Record ID: " + str(contact.get_id()))
                            print("Record KeyValues: ")
                            for key, value in contact.get_key_values().items():
                                if isinstance(value, dict):
                                    print("Record KeyName : " + key + " - Value : ")
                                    for mapKey, mapValue in value.items():
                                        print(mapKey + " : " + mapValue)
                                else:
                                    print("Record KeyName : " + key + " - Value : " + value)
                    accountsPreferenceField = preference_field_matched_value.get_accounts()
                    if accountsPreferenceField is not None:
                        for account in accountsPreferenceField:
                            print("Record ID: " + str(account.get_id()))
                            print("Record KeyValues: ")
                            for key, value in account.get_key_values().items():
                                if isinstance(value, dict):
                                    print("Record KeyName : " + key + " - Value : ")
                                    for mapKey, mapValue in value.items():
                                        print(mapKey + " : " + mapValue)
                                else:
                                    print("Record KeyName : " + key + " - Value : " + value)
                    deals_preference_field = preference_field_matched_value.get_deals()
                    if deals_preference_field is not None:
                        for deal in deals_preference_field:
                            print("Record ID: " + deal.get_id())
                            print("Record KeyValues: ")
                            for key, value in deal.get_key_values().items():
                                if isinstance(value, dict):
                                    print("Record KeyName : " + key + " - Value : ")
                                    for map_key, map_value in value.items():
                                        print(map_key + " : " + map_value)
                                else:
                                    print("Record KeyName : " + key + " - Value : " + value)
                accounts = conversion_option.get_accounts()
                if accounts is not None:
                    for account in accounts:
                        print("Record ID: " + str(account.get_id()))
                        print("Record KeyValues: ")
                        for key, value in account.get_key_values().items():
                            key_name = key
                            if isinstance(value, list):
                                print("Record KeyName : " + key_name)
                                for data in value:
                                    if isinstance(data, dict):
                                        print("Record KeyName : " + key_name + " - Value : ")
                                        for k, v in data.items():
                                            print(k + " : " + v)
                                    else:
                                        print(data)
                            elif isinstance(value, dict):
                                print("Record KeyName : " + key_name + " - Value : ")
                                for k, v in value.items():
                                    print(k + " : " + v)
                            else:
                                print("Record KeyName : " + key_name + " - Value : " + str(value))
                deals = conversion_option.get_deals()
                if deals is not None:
                    for deal in deals:
                        print("Record ID: " + str(deal.getId()))
                        print("Record KeyValues: ")
                        for key, value in deal.getKeyValues().items():
                            keyName = key
                            if isinstance(value, list):
                                print("Record KeyName : " + keyName)
                                for data in value:
                                    if isinstance(data, dict):
                                        print("Record KeyName : " + keyName + " - Value : ")
                                        for k, v in data.items():
                                            print(k + " : " + v)
                                    else:
                                        print(data)
                            elif isinstance(value, dict):
                                print("Record KeyName : " + keyName + " - Value : ")
                                for k, v in value.items():
                                    print(k + " : " + v)
                            else:
                                print("Record KeyName : " + keyName + " - Value : " + value)
                modules_with_multiple_layouts = conversion_option.get_modules_with_multiple_layouts()
                if modules_with_multiple_layouts is not None:
                    for module_1 in modules_with_multiple_layouts:
                        print("ConversionOptions ModulesWithMultipleLayouts API-Name: " + module_1.get_api_nName())
                        print("ConversionOptions ModulesWithMultipleLayouts ID: " + module_1.get_id())
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message().get_value())


record_id = 440248001507174
LeadConversionOptions.initialize()
LeadConversionOptions.lead_conversion_options(record_id)
