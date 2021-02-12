import time
from locust import HttpUser, task, between,TaskSet
import config


class RewardsLoadTesting(TaskSet):
    wait_time = between(1, 2)
    """
    @task
    def PostReward(self):
        payload="{\n    \"type\": \"post\",\n    \"data\": {\n        \"content\": \"kjnjnnjnjk\",\n        \"media\": [\n            {\n                \"type\": \"image\",\n                \"url\": \"idjndlmlkmklmklmklmklmmage-url\"\n            },\n            {\n                \"type\": \"video\",\n                \"url\": \"dvmmlllmllmm\"\n            }\n        ]\n    },\n    \"checkInGeoPoints\": [\n        28.459497,\n        77.026634\n    ],\n    \"checkInText\": \"Emaar Imperial Garden, Sector-102, Gurgaon, Haryana\",\n    \"taggedUsers\": [\n        \"jknjknjnjk\",\n        \"bbsahjbhsd\",\n        \"aNJKNJKASN\"\n    ]\n}"
        headers = {
        '_id': str(config.user_id),
        'platform': 'android',
        'version': '1.0',
        'Content-Type': 'application/json'
        }
        url = "/api/v2/rewards/admin/post"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
    """

    @task
    def GetTimeLine(self):
        payload={}
        headers = {
            '_id': str(config.user_id),
            'platform': 'android',
            'version': '1.0'
        }
        url = "/api/v2/rewards/timeline?type=gallerySet"

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response


    @task
    def RewardsStats(self):
        payload={}
        headers = {
        '_id': str(config.user_id),
        'platform': 'android',
        'version': '1.0'
        }
        url = "/api/v2/rewards/stats"

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
