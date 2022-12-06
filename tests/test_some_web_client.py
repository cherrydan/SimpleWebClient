import datetime

import responses

from libs import some_resource_client


@responses.activate
def test_some_web_client():
    valid_json_data = {"lastActionTime": 1670327258, "timeDiff": 1232}
    responses.add(responses.GET, url='https://avito.ru/web/user/get-status/177068588',
                  json=valid_json_data, status=200)

    some_client = some_resource_client.SomeResourceClient('https://avito.ru')

    res = some_client.get_user_last_action_time(177068588)
    assert res == datetime.datetime.fromtimestamp(valid_json_data['lastActionTime'] - valid_json_data['timeDiff'])
