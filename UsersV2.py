import time
from locust import HttpUser, task, between,TaskSet
import config


class UsersV2LoadTesting(TaskSet):
    wait_time = between(1, 2)
    
    @task
    def SyncContacts(self):
        payload="{\n    \"contacts\": [{\n        \"countryCode\": 44,\n        \"nationalNumber\": 3454656749,\n        \"contactName\": \"Josh Gulati\"\n    }, {\n        \"countryCode\": 44,\n        \"nationalNumber\": 4534568759,\n        \"contactName\": \"Abhijit Sagar\"\n    }, {\n        \"countryCode\": 91,\n        \"nationalNumber\": 9717778289,\n        \"contactName\": \"Anshu Singh\"\n    }, {\n        \"countryCode\": 91,\n        \"nationalNumber\": 8960419521,\n        \"contactName\": \"Ankit Himanshu\"\n    }]\n}"
        headers = {
            '_id': str(config.user_id),
            'platform': 'android',
            'version': '1.0',
            'Content-Type': 'application/json'
        }
        url = "/api/v2/users/syncContacts"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    '''
    @task
    def RandomUsers(self):
        payload={}
        headers = {
            '_id': str(config.user_id1),
            'platform': 'android',
            'version': '1.0'
        }

        url = "/api/v2/users/random?count=2"

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    
    @task
    def UsersDetails(self):
        payload={}
        headers = {
        '_id': str(config.user_id),
        'platform': 'android',
        'version': '1.0'
        }

        url = "/api/v2/users/detail?id="+str(config.user_id)

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    '''
    @task
    def FriendsSuggestions(self):
        payload={}
        headers = {
        '_id': str(config.user_id),
        'platform': 'android',
        'version': '1.2.0'
        }

        url = "/api/v2/users/friend/suggestions?page=1&keyword=josh"

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    
    @task
    def FriendsRequests(self):
        payload={}
        headers = {
            '_id': str(config.user_id),
            'platform': 'android',
            'version': '1.0'
        }

        url = "/api/v2/users/friend/requests?page=1&limit=10"

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    
    @task
    def ValidateUsername(self):
        payload={}
        headers = {
            '_id': str(config.user_id),
            'platform': 'android',
            'version': '1.0'
            }

        url = "/api/v2/users/validateUsername?username=anshu"

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
    

    @task
    def UserSocialLink(self):
        payload='type=Facebook&token=\'asdas6d54as567dasd\'&accountId=\'23424123213\''
        headers = {
            '_id': str(config.user_id),
            'platform': 'android',
            'version': '1.0',
            'Content-Type': 'application/x-www-form-urlencoded'
            }

        url = "/api/v2/users/social/link"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    
    @task
    def Mirrorfly(self):
        payload='mirroflyId=abcdef'
        headers = {
                '_id': str(config.user_id),
                'platform': 'android',
                'version': '1.0',
                'Content-Type': 'application/x-www-form-urlencoded'
                }


        url = "/api/v2/users/mirrorfly/linkUserId"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    @task
    def MirrorflyGetAll(self):
        payload='mirroflyId%5B%5D=919717778289%40xmpp-uat.jigrr.com&mirroflyId%5B%5D=447947853178%40xmpp-uat.jigrr.com'
        headers = {
            '_id': str(config.user_id),
            'platform': 'android',
            'version': '1.0.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }


        url = "/api/v2/users/mirrorfly/getAll"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    @task
    def MirrorflyGetAll(self):
        payload='mirroflyId%5B%5D=919717778289%40xmpp-uat.jigrr.com&mirroflyId%5B%5D=447947853178%40xmpp-uat.jigrr.com'
        headers = {
            '_id': str(config.user_id),
            'platform': 'android',
            'version': '1.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        url = "/api/v2/users/mirrorfly/getAll"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    
    @task
    def TimelineVisibility(self):
        payload="{\n    \"id\": \"3:3d\"\n}"
        headers = {
            'platform': 'android',
            'version': '1.0',
            '_id': str(config.user_id),
            'Content-Type': 'application/json'
        }

        url = "/api/v2/users/timeline/visibility"

        response = self.client.patch(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    
    @task
    def UsersReport(self):
        payload="{\n    \"userId\": \"5f9c6e10d53b0147756b8a22\",\n    \"type\": \"room\",\n    \"message\": \"Obscene content\"\n}"
        headers = {
        '_id': str(config.user_id),
        'platform': 'android',
        'version': '1.0',
        'Content-Type': 'application/json'
        }

        url = "/api/v2/users/report"

        response = self.client.patch(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
    

    @task
    def UserUnblock(self):
        payload='blockedUserId='+str(config.user_id)
        headers = {
            '_id': str(config.user_id),
            'platform': 'android',
            'version': '1.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        url = "/api/v2/users/unblock"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    
    @task
    def UserUnfriend(self):
        payload='friendId='+str(config.user_id)
        headers = {
            '_id': str(config.user_id),
            'platform': 'android',
            'version': '1.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        url = "/api/v2/users/unfriend"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    
    @task
    def UserSignout(self):
        payload='clevertapId=-v80bbd513194c4eb98ad4d2c7ffc8758e&deviceId=07614ab8a648a96c7dd063a85c9a028677d715df67544523da4457d948f3c65c'
        headers = {
            '_id': str(config.user_id),
            'platform': 'android',
            'version': '1.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        url = "/api/v2/users/signOut"

        response = self.client.patch(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
    
    @task
    def HomeSuggestions(self):
        payload={}
        headers = {
        '_id': str(config.user_id),
        'platform': 'android',
        'version': '1.2.0'
        }
        url = "/api/v2/users/home/suggestions"

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response


    @task
    def HomeSuggestions(self):
        payload={}
        headers = {
        '_id': str(config.user_id),
        'platform': 'android',
        'version': '1.2.0'
        }
        url = "/api/v2/users/home/suggestions"

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
