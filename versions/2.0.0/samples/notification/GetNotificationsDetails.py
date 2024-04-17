from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.notifications import NotificationsOperations, GetNotificationsParam, \
    ResponseWrapper, APIException


class GetNotificationDetails:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_notification_details():
        """
        This method is used to get details of the Notification and print the response.
        """
        notification_operations = NotificationsOperations()
        param_instance = ParameterMap()
        param_instance.add(GetNotificationsParam.module, 'Deals')
        param_instance.add(GetNotificationsParam.page, 1)
        param_instance.add(GetNotificationsParam.per_page, 20)
        param_instance.add(GetNotificationsParam.channel_id, 1006800211)
        # Call get_notification_details method that takes param_instance as parameter
        response = notification_operations.get_notifications(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    notification_list = response_object.get_watch()
                    for notification in notification_list:
                        print("Notification NotifyOnRelatedAction: " + str(notification.get_notify_on_related_action()))
                        print("Notification ChannelExpiry: " + str(notification.get_channel_expiry()))
                        print("Notification ResourceUri: " + notification.get_resource_uri())
                        print("Notification ResourceId: " + notification.get_resource_id())
                        print("Notification ResourceName: " + notification.get_resource_name())
                        print("Notification ChannelId: " + str(notification.get_channel_id()))
                        print("Notification NotifyUrl: " + notification.get_notify_url())
                        events = notification.get_events()
                        if events is not None:
                            for event in events:
                                print("Notification Events: " + event)
                        print("Notification Token: " + notification.get_token())
                    info = response_object.get_info()
                    if info is not None:
                        if info.get_per_page() is not None:
                            print('Notification Info PerPage: ' + str(info.get_per_page()))
                        if info.get_page() is not None:
                            print('Notification Info Page: ' + str(info.get_page()))
                        if info.get_count() is not None:
                            print('Notification Info Count: ' + str(info.get_count()))
                        if info.get_more_records() is not None:
                            print('Notification Info MoreRecords: ' + str(info.get_more_records()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


GetNotificationDetails.initialize()
GetNotificationDetails.get_notification_details()
