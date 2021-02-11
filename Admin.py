import time
from locust import HttpUser, task, between,TaskSet
import config


class AdminLoadTesting(TaskSet):
    wait_time = between(1, 2)
    
    @task
    def AdminLoginEvent(self):
        payload={'email': 'no-umairkhan@mobiloitte.com',
        'password': 'Mobiloitte1'}
        files=[
        ]
        headers = {}
        url = "/api/v1/admin/login"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
