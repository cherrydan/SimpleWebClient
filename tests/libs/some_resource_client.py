import datetime
import json

import requests


class SomeResourceClient:
    def __init__(self, url):
        self.url = url

    def __user_get_status(self, user_id): # private
        resp = requests.get(f'{self.url}/web/user/get-status/{user_id}')
        json_data = json.loads(resp.text)
        return json_data

    def get_user_last_action_time(self, user_id):
        res = self.__user_get_status(user_id)
        last_action_time = res['lastActionTime']
        time_diff = res['timeDiff']
        return datetime.datetime.fromtimestamp(last_action_time - time_diff)
