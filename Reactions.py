import time
from locust import HttpUser, task, between,TaskSet
import config


class ReactionsLoadTesting(TaskSet):
    wait_time = between(1, 2)
    """
    @task
    def ReactionList(self):
        payload='entityId=5f74c053a6362c05b77b0afc&entityType=topic&reaction=1'
        headers = {
            '_id': str(config.user_id),
            'platform': 'android',
            'version': '1.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        url = "/api/v2/reaction/add"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
    """

    @task
    def AddReaction(self):
        payload='entityId=5f74c053a6362c05b77b0afc&entityType=topic&reaction=1'
        headers = {
            '_id': str(config.user_id),
            'platform': 'android',
            'version': '1.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        url = "/api/v2/reaction/add"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response




