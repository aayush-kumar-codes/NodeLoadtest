import time
from locust import HttpUser, task, between,TaskSet
import config


class FeedsLoadTesting(TaskSet):
    wait_time = between(1, 2)
    
    @task
    def FeedsSearch(self):
        payload={}
        headers = {
            '_id': str(config.user_id),
            'platform': 'android',
            'version': '1.0'
        }
        url = "/api/v2/feeds/search"

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    @task
    def FeedsTimeline(self):
        payload={}
        headers = {
        '_id': '5faa72ffc85f364f6808f102',
        'platform': 'android',
        'version': '1.0.0'
        }
        url = "/api/v2/feeds/timeline?type=feeds"

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response


    @task
    def FeedsPost(self):
        payload={'type': 'post',
        'privacy': '1',
        'content': 'hello'}
        files=[

        ]
        headers = {
        'platform': 'android',
        'version': '1.0.0',
        'language': 'en',
        '_id': str(config.user_id)
        }
        url = "/api/v2/feeds/post"

        response = self.client.post(url,headers=headers,data=payload,files=files)
        assert response.status_code == 200
        assert response




    """
    @task
    def FeedsDetails(self):
        payload={}
        headers = {
            '_id': str(config.user_id1),
            'platform': 'android',
            'version': '1.0'
        }
        url = "/api/v2/feeds/search"

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
    """