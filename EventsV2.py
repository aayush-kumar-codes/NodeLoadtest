import time
from locust import HttpUser, task, between,TaskSet
import config


class EventsV2LoadTesting(TaskSet):
    wait_time = between(1, 2)
    
    @task
    def EventMatch(self):
        payload={}
        headers = {
            '_id': str(config.user_id),
            'platform': 'android',
            'version': '1.0'
        }
        url = "/api/v2/events/match/search?eventType=ONLINE_GENERAL&gender=any&topicId=5fee388101082d6d02c5dc75&age="

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response