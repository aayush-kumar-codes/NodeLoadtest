import time
from locust import HttpUser, task, between,TaskSet
import config


class UsersLoadTesting(TaskSet):
    wait_time = between(1, 2)


    @task
    def ShowProfile(self):
        payload={}
        headers = {
        '_id': str(config.user_id),
        'appLanguage': str(config.appLanguage)
        }
        url = "/api/v1/user/showMyProfile/"+str(config.user_id)

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
    

    @task
    def BlockList(self):
        payload='friendId='+str(config.friendId)
        headers = {
        '_id': str(config.user_id),
        'appLanguage': str(config.appLanguage),
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        url = "/api/v1/user/myBlockUserList"

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
    
    @task
    def FriendList(self):
        payload='friendId='+str(config.friendId)
        headers = {
        '_id': str(config.user_id),
        'appLanguage': str(config.appLanguage),
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        url = "/api/v1/user/getFriendList"

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    
    @task
    def InterestList(self):
        payload={}
        headers = {
        '_id': str(config.user_id),
        'appLanguage': str(config.appLanguage),
        }
        url = "/api/v1/user/interestList"

        response = self.client.get(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    
    @task
    def AddBasicInfo(self):
        payload={}
        headers = {
        '_id': str(config.user_id),
        'appLanguage': str(config.appLanguage),
        }
        url = "/api/v1/user/addBasicInfo"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    
    @task
    def SocialLogin(self):
        payload='loginType=Facebook&socialId='+str(config.social_id)
        headers = {
        '_id': str(config.user_id),
        'appLanguage': str(config.appLanguage),
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        url = "/api/v1/user/socialLogin"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
    
    #commented due to sms will go
    
    @task
    def SentOtp(self):
        payload='applanguage='+str(config.appLanguage)+'&countryCode='+str(config.countryCode)+'&mobileNumber='+str(config.mobileNumber)
        headers = {
        '_id': str(config.user_id),
        'appLanguage': str(config.appLanguage),
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        url = "/api/v1/user/otpSent"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    
    @task
    def ResentSentOtp(self):
        payload='applanguage='+str(config.appLanguage)+'&countryCode='+str(config.countryCode)+'&mobileNumber='+str(config.mobileNumber)
        headers = {
            'appLanguage': str(config.appLanguage),
            'platform': str(config.platform),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        url = "/api/v1/user/resendOtp"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
    
    
    @task
    def BlockUnblockUserProfile(self):
        payload=payload="{\n  \"blockedUser\": [\n    {\n      \"name\": \"asd\",\n      \"profilePic\": \"https://res.cloudinary.com/dvbqexh6f/image/upload/v1606258034/pnwqai4pu4qb4a077t9f.jpg\",\n      \"userId\": \""+str(config.user_id)+"\"\n    }\n  ],\n  \"status\": \"BLOCK\"\n}"
        headers = {
            '_id': str(config.user_id),
            'appLanguage': str(config.appLanguage),
            'Content-Type': 'application/json'
        }
        url = "/api/v1/user/blockUnblockUserProfile"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    
    @task
    def ApplicationSearch(self):
        payload='type=1&search=%40jo'
        headers = {
        '_id': str(config.user_id),
        'appLanguage': str(config.appLanguage),
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        url = "/api/v1/user/applicationSearch"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
    
    
    @task
    def AddFriend(self):
        payload="{\n  \"friends\": [\n    {\n      \"friendId\": \""+str(config.user_id)+"\"\n    }\n  ]\n}"
        headers = {
        '_id': str(config.user_id),
        'Content-Type': 'application/json'
        }

        url = "/api/v1/user/addFriend"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response

    
    @task
    def SendFriendRequest(self):
        payload='friendId='+str(config.user_id)
        headers = {
        '_id': str(config.user_id),
        'appLanguage': str(config.appLanguage),
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        url = "/api/v1/user/sendFriendRequest"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
    

    @task
    def ActionToFriendRequest(self):
        payload='friendRequestUserId='+str(config.user_id)+'&response=ACCEPT'
        headers = {
        '_id': str(config.user_id),
        'appLanguage': str(config.appLanguage),
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        url = "/api/v1/user/actionToFriendRequest"

        response = self.client.post(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
    
    @task
    def EditProfile(self):
        payload={'aboutMe': 'This is about me','name': 'Anshu','surName': 'Dagar'}
        headers = {
        '_id': str(config.user_id),
        'appLanguage': 'en'
        }

        url = "/api/v1/user/editProfile"
        files=[
                ('backImage',(str(config.image_name),open(str(config.image_path),'rb'),'image/jpeg')),
                ('image',(str(config.image_name),open(str(config.image_path),'rb'),'image/jpeg'))
                ]
        response = self.client.put(url,headers=headers,data=payload)
        assert response.status_code == 200
        assert response
