
import requests as r
import json
import setup
import logging
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


def get_request(url, headers=None, auth=None):
    temphead = {**setup.head, **headers} if headers else setup.head  # merge arrays, setup.head used as basic header
    return r.get(url, headers=temphead, auth=auth)


def post_request(url, headers=None):
    temphead = {**setup.head, **headers} if headers else setup.head  # merge arrays, setup.head used as basic header
    return r.post(url, headers=temphead)


def put_request(url, headers=None):
    temphead = {**setup.head, **headers} if headers else setup.head  # merge arrays, setup.head used as basic header
    return r.put(url, headers=temphead)


if __name__ == '__main__':
    target = setup.host + setup.token_route
    credentials = (setup.users['user1']['username'], setup.users['user1']['password'])
    get_token = get_request(target, auth=credentials)
    print(get_token.content)
    credentials = (setup.users['user2']['username'], setup.users['user2']['password'])
    get_token = get_request(target, auth=credentials)
    print(get_token.content)
    credentials = (setup.users['user1']['username'], setup.users['user1']['password'])
    get_token = get_request(target, auth=credentials)
    print(get_token.content)
