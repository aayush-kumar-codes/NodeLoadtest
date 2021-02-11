import time
from locust import HttpUser, task, between,TaskSet
import config


class TopicsLoadTesting(TaskSet):
    wait_time = between(1, 2)
    """
    @task
    def TopicList(self):
        payload={}
        files={}
        headers = {
            '_id': '5ff5c25505ee39449b24e39f',
            'platform': 'android',
            'version': '1.0.0'
        }

        url = "/api/v2/topics/list?language=en"

        response = self.client.get(url,headers=headers,data=payload,files=files)
        assert response.status_code == 200
        assert response
    """

    @task
    def AddTopic(self):
        payload={'topic': 'Manchester United fan? Give your prediction for the next match - hear other fan\'s view',
        'language': 'en',
        'imageSizes': '[{"width": 100, "height": 120}, {"width": 200, "height": 320}]'}
        files=[
        ('image',('file',open(str(config.image_path),'rb'),'application/octet-stream'))
        ]
        headers = {
        '_id': str(config.user_id),
        'platform': 'android',
        'version': '1.0.0'
        }

        url = "/api/v2/topics/add"

        response = self.client.post(url,headers=headers,data=payload,files=files)
        assert response.status_code == 200
        assert response


    @task
    def UpdateTopic(self):
        payload='topic=This%20is%20topic&language=en&image=https%3A%2F%2Fimages.myguide-cdn.com%2Fmd%2Fcommon%2Flarge%2F5db8905deea80-630078.jpg&id=5f733fe8762f6d66767d0dde'
        headers = {
            '_id': str(config.user_id),
            'platform': 'android',
            'version': '1.0.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        url = "/api/v2/topics/edit"

        response = self.client.put(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response


    @task
    def DeleteTopic(self):
        payload={}
        headers = {
        '_id': '5faa72ffc85f364f6808f102',
        'platform': 'android',
        'version': '1.0.0'
        }
        url = "/api/v2/topics/delete?id=5ff17e0c15c4c22981f62bdb&platform=android&version=1.0.0"

        response = self.client.delete(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
