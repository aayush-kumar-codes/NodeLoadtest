import time
from locust import HttpUser, task, between,TaskSet
import config


class CommonLoadTesting(TaskSet):
    wait_time = between(1, 2)
    
    @task
    def CommonConfig(self):
        payload={}
        headers = {
            '_id': str(config.user_id),
            'platform': 'android',
            'version': '1.0'
        }
        url = "/api/v2/common/config"

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    @task
    def CommonSendSMS(self):
        payload='mobile=%2B447947853178&message=Jigrr%3A%20Final%20OTP%20message'
        headers = {
        '_id': str(config.user_id),
        'platform': 'android',
        'version': '1.0',
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        url = "/api/v2/common/sendSMS"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

