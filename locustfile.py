

import time
from locust import HttpUser, task, between,TaskSet
from Users import UsersLoadTesting
from Events import EventsLoadTesting
from UsersV2 import UsersV2LoadTesting
from Topics import TopicsLoadTesting
from Reactions import ReactionsLoadTesting
from Reward import RewardsLoadTesting
from Feeds import FeedsLoadTesting
from Common import CommonLoadTesting
from EventsV2 import EventsV2LoadTesting
from Admin import AdminLoadTesting


class MainLoadTesting(HttpUser):
    #tasks = [TopicsLoadTesting,UsersLoadTesting,EventsLoadTesting,UsersV2LoadTesting,ReactionsLoadTesting,RewardsLoadTesting,FeedsLoadTesting,CommonLoadTesting,EventsV2LoadTesting,AdminLoadTesting]
    tasks = [EventsV2LoadTesting]