from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.notifications import NotificationsOperations, BodyWrapper, Notification, \
    ActionWrapper, SuccessResponse, APIException


class UpdateNotification:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_notification():
        """
        This method is used to update single Notification and print the response.
        """
        notification_operations = NotificationsOperations()
        body_wrapper = BodyWrapper()
        notifications = []
        notification = Notification()
        notification.set_channel_id("1006800211")
        # To subscribe based on particular operations on given modules.
        notification.set_events(['Leads.create'])
        # URL to be notified (POST request)
        notification.set_notify_url("https://www.zohoapis.com")
        notifications.append(notification)
        body_wrapper.set_watch(notifications)
        response = notification_operations.update_notification(body_wrapper)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_watch()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details: ")
                            if action_response.get_details() is not None:
                                for key, value in action_response.get_details().items():
                                    if isinstance(value, list):
                                        event_list = value
                                        for event in event_list:
                                            print("Notification ChannelExpiry: " + str(event.get_channel_expiry()))
                                            print("Notification ResourceUri: " + event.get_resource_uri())
                                            print("Notification ResourceId: " + event.get_resource_id())
                                            print("Notification ResourceName: " + event.get_resource_name())
                                            print("Notification ChannelId: " + str(event.get_channel_id()))
                                    else:
                                        print(key + ' : ' + str(value))
                                print("Message: " + action_response.get_message().get_value())
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


UpdateNotification.initialize()
UpdateNotification.update_notification()
