from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.portals import PortalsOperations, ResponseWrapper, APIException


class GetPortal(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_portal(portal_name):
        portals_operations = PortalsOperations()
        response = portals_operations.get_portal(portal_name)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                response_wrapper = response_object
                portals = response_wrapper.get_portals()
                for portal in portals:
                    print("Portals CreatedTime: " + str(portal.get_created_time()))
                    print("Portals ModifiedTime: " + str(portal.get_modified_time()))
                    modified_by = portal.get_modified_by()
                    if modified_by is not None:
                        print("Portals ModifiedBy User-ID: " + str(modified_by.get_id()))
                        print("Portals ModifiedBy User-Name: " + modified_by.get_name())
                    created_by = portal.get_created_by()
                    if created_by is not None:
                        print("Portals CreatedBy User-ID: " + str(created_by.get_id()))
                        print("Portals CreatedBy User-Name: " + created_by.get_name())
                    print("Portals Zaid: " + str(portal.get_zaid()))
                    print("Portals Name: " + portal.get_name())
                    print("Portals Active: " + str(portal.get_active()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


portal_name = "PortalsAPITest101"
GetPortal.initialize()
GetPortal.get_portal(portal_name)
