
import requests
import json
import setup
import logging
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


def get_request(url, headers=None, auth=None):
    temphead = {**setup.head, **headers} if headers else setup.head  # merge arrays, setup.head used as basic header
    return requests.get(url, headers=temphead, auth=auth)


def post_request(url, headers=None, json=None):
    temphead = {**setup.head, **headers} if headers else setup.head  # merge arrays, setup.head used as basic header
    return requests.post(url, headers=temphead, json=json)


def put_request(url, headers=None, json=None):
    temphead = {**setup.head, **headers} if headers else setup.head  # merge arrays, setup.head used as basic header
    return requests.put(url, headers=temphead, json=json)


def get_token(uname, passwd):  # (status code, token)
    res = get_request(setup.host + setup.token_route, auth=(uname, passwd))
    return res.status_code, json.loads(res.content)['token']


def get_users(token):
    res = get_request(setup.host + setup.user_route, headers={'token': token})
    return res.status_code, json.loads(res.content)['payload']


def post_user(data):
    res = post_request(setup.host + setup.user_route, json=data)
    return res.status_code


def get_user_details(token, uname):
    res = get_request(setup.host + setup.user_route + '/' + uname, headers={'token': token})
    return res.status_code, json.loads(res.content)['text']


def put_user_data(token, uname, data):
    res = put_request(setup.host + setup.user_route + '/' + uname, headers={'token': token}, json=data)
    return res.status_code

if __name__ == '__main__':
    target = setup.host + setup.user_route
    userdata = get_request(target, headers={'token': 'lolnotatoken'})
    print(json.loads(userdata.content)['payload'])

    target = setup.host + setup.user_route
    data = {'username': 'apiuser4', 'password': 'check12', "firstname": None, "lastname": 'None', "phone": None}
    response1 = post_request(target, json=data)
    print(response1)

    target = setup.host + setup.token_route
    data = {'username': 'apiuser4', 'password': 'check12'}
    response2 = get_request(target, auth=('apiuser4', 'check12'))
    print(response2)
    print(json.loads(response2.content)['token'])

    target = setup.host + setup.user_route + '/apiuser4'
    response = get_request(target, headers={'token': json.loads(response2.content)['token']})
    print(response)
    pass