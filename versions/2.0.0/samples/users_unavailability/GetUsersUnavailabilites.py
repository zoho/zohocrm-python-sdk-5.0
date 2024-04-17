from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.users_unavailability import UsersUnavailabilityOperations, \
    GetUsersUnavailabilityParam, ResponseWrapper, APIException
import json


class GetUsersUnavailabilites(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_users_unavailabilities():
        user_operations = UsersUnavailabilityOperations()
        param_instance = ParameterMap()
        param_instance.add(GetUsersUnavailabilityParam.group_ids, "324123432132")
        param_instance.add(GetUsersUnavailabilityParam.include_inner_details, "56xxx8")
        param_instance.add(GetUsersUnavailabilityParam.role_ids, "324231232")
        param_instance.add(GetUsersUnavailabilityParam.territory_ids, "32323213123")
        filters = {"group_operator": "or"}
        group = []
        criteria1 = {"comparator": "between"}
        criteria1Field = {"api_name": "from"}
        criteria1["field"] = criteria1Field
        criteria1Value = ["2021-02-18T19:00:00+05:30", "2021-02-19T19:00:00+05:30"]
        criteria1["value"] = criteria1Value
        group.append(criteria1)
        criteria2 = {"comparator": "between"}
        criteria2Field = {"api_name": "to"}
        criteria2["field"] = criteria2Field
        criteria2Value = ["2021-02-18T20:00:00+05:30", "2021-02-19T20:00:00+05:30"]
        criteria2["value"] = criteria2Value
        group.append(criteria2)
        filters["group"] = group
        param_instance.add(GetUsersUnavailabilityParam.filters, json.dumps(filters))
        response = user_operations.get_users_unavailability(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                users = response_object.get_users_unavailability()
                for users_unavailability in users:
                    print("UsersUnavailability Comments: " + users_unavailability.get_comments())
                    print("UsersUnavailability From: " + str(users_unavailability.get_from()))
                    print("UsersUnavailability Id: " + str(users_unavailability.get_id()))
                    print("UsersUnavailability to: " + str(users_unavailability.get_to()))
                    user = users_unavailability.get_user()
                    if user is not None:
                        print("UsersUnavailability User-Name: " + user.get_name())
                        print("UsersUnavailability User-Id: " + str(user.get_id()))
                        print("UsersUnavailability User-ZuId: " + str(user.get_zuid()))
                info = response_object.get_info()
                if info is not None:
                    if info.get_per_page() is not None:
                        print("User Info PerPage: " + str(info.get_per_page()))
                    if info.get_count() is not None:
                        print("User Info Count: " + str(info.get_count()))
                    if info.get_page() is not None:
                        print("User Info Page: " + str(info.get_page()))
                    if info.get_more_records() is not None:
                        print("User Info MoreRecords: " + str(info.get_more_records()))

            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message().get_value())


GetUsersUnavailabilites.initialize()
GetUsersUnavailabilites.get_users_unavailabilities()