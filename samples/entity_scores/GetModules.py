from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.entity_scores import EntityScoresOperations, ResponseWrapper, APIException


class GetModules(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_modules():
        entity_scores_operations = EntityScoresOperations("Positive_Score")
        response = entity_scores_operations.get_modules()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                response_wrapper = response_object
                data = response_wrapper.get_data()
                if data is not None:
                    for score in data:
                        print("Score : " + str(score.get_score()))
                        print("PositiveScore : " + str(score.get_positive_score()))
                        print("TouchPointScore : " + str(score.get_touch_point_score()))
                        print("NegativeScore : " + str(score.get_negative_score()))
                        print("touchPointNegativeScore : " + str(score.get_touch_point_negative_score()))
                        print("touchPointPositiveScore : " + str(score.get_touch_point_positive_score()))
                        print("Id : " + str(score.get_id()))
                        print("ZiaVisions : " + str(score.get_zia_visions()))
                        scoringRule = score.get_scoring_rule()
                        if scoringRule is not None:
                            print("ScoringRule Id : " + str(scoringRule.get_id()))
                            print("ScoringRule Name : " + scoringRule.get_name())
                            fieldStates = score.get_field_states()
                            for field in fieldStates:
                                print("fieldStates : " + field)
                info = response_wrapper.get_info()
                if info is not None:
                    if info.get_per_page() is not None:
                        print("Info PerPage: " + str(info.get_per_page()))
                    if info.get_count() is not None:
                        print("Info Count: " + str(info.get_count()))
                    if info.get_page() is not None:
                        print("Info Page: " + str(info.get_page()))
                    if info.get_more_records() is not None:
                        print("Info MoreRecords: " + str(info.get_more_records()))

            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


GetModules.initialize()
GetModules.get_modules()