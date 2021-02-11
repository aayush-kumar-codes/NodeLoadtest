import time
from locust import HttpUser, task, between,TaskSet
import config


class EventsLoadTesting(TaskSet):
    wait_time = between(1, 2)
    
    @task
    def CreateAntakshriEvent(self):
        payload='eventType=ONLINE_GENERAL&title=Anshu%20New%20Event&onlineEventType=LIVE_STREAM&privacy=2&time=3%3A24&date=2020-10-28&defaultImage='
        headers = {
        '_id': str(config.user_id),
        'applanguage': str(config.appLanguage),
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        url = "/api/v1/event/createAntakshriEvent"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    
    @task
    def CreateEvent(self):
        payload='eventType=ONLINE_GENERAL&title=Anshu%20New%20Event&onlineEventType=LIVE_STREAM&privacy=2&time=3%3A24&date=2020-10-28&defaultImage=https%3A%2F%2Fwww.google.com%2Furl%3Fsa%3Di%26url%3Dhttps%253A%252F%252Fwww.freepik.com%252Ffree-photos-vectors%252Fbackground%26psig%3DAOvVaw0Q1V8wD8EO-NptF0eCpK1_%26ust%3D1602162377893000%26source%3Dimages%26cd%3Dvfe%26ved%3D0CAIQjRxqFwoTCLi4q43GouwCFQAAAAAdAAAAABAD'
        headers = {
        '_id': str(config.user_id),
        'applanguage': str(config.appLanguage),
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        url = "/api/v1/event/createEvent"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    @task
    def EventHosted(self):
        payload="{\n    \"limit\": 100\n}"
        headers = {
        '_id': str(config.user_id),
        'applanguage': str(config.appLanguage),
        'Content-Type': 'application/json'
        }
        url = "/api/v1/event/eventHosted"

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response


    @task
    def NetworkEventList(self):
        payload="{\n    \"limit\": 100\n}"
        headers = {
        '_id': str(config.user_id),
        'applanguage': str(config.appLanguage),
        'Content-Type': 'application/json'
        }
        url = "/api/v1/event/networkEventList"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
