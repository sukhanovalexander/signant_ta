
import requests
import json
import setup
import logging
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


def get_request(url: str, headers: dict = None, auth: tuple = None) -> requests.Response:
    """Basic get wrap. URL, headers and auth tuple"""
    temphead = {**setup.head, **headers} if headers else setup.head  # merge arrays, setup.head used as basic header
    return requests.get(url, headers=temphead, auth=auth)


def post_request(url: str, headers: dict = None, payload: dict = None) -> requests.Response:
    """Basic post wrap. URL, headers and payload"""
    temphead = {**setup.head, **headers} if headers else setup.head  # merge arrays, setup.head used as basic header
    return requests.post(url, headers=temphead, json=payload)


def put_request(url: str, headers: dict = None, payload: dict = None) -> requests.Response:
    """Basic put wrap. URL, headers and payload"""
    temphead = {**setup.head, **headers} if headers else setup.head  # merge arrays, setup.head used as basic header
    return requests.put(url, headers=temphead, json=payload)


def get_token(uname: str, passwd: str, url: str = None) -> (int, str):
    """GET token, return (status, token)"""
    url = setup.host + setup.token_route if not url else url
    res = get_request(url, auth=(uname, passwd))
    token = json.loads(res.content)['token'] if 'token' in json.loads(res.content).keys() else ''
    return res.status_code, token


def get_users(token: str, url: str = None) -> (int, list):
    """GET users list, return (status, list)"""
    url = setup.host + setup.user_route if not url else url
    res = get_request(url, headers={'token': token})
    payload = json.loads(res.content)['payload'] if 'payload' in json.loads(res.content).keys() else []
    return res.status_code, payload


def post_user(data: dict, url: str = None) -> int:
    """POST new user, return status"""
    url = setup.host + setup.user_route if not url else url
    res = post_request(url, payload=data)
    return res.status_code


def get_user_details(token: str, uname: str, url: object = None) -> (int, dict):
    """GET user info, return dict"""
    url = setup.host + setup.user_route + '/' + uname if not url else url
    res = get_request(url, headers={'token': token})
    payload = json.loads(res.content)['payload'] if 'payload' in json.loads(res.content).keys() else []
    return res.status_code, payload


def put_user_data(token: str, uname: str, data: dict, url: str = None) -> int:
    """PUT updated user info, return code"""
    url = setup.host + setup.user_route + '/' + uname if not url else url
    res = put_request(url, headers={'token': token}, payload=data)
    return res.status_code


if __name__ == '__main__':
    #  post user
    #  get token
    #  list users
    #  get user details
    #  update user details
    post_code = post_user(setup.users['apirand1'])
    token_code, token1 = get_token(setup.users['apirand1']['username'], setup.users['apirand2']['password'])
    list_code, user_list = get_users(token1)
    det_code, user_det = get_user_details(token1, setup.users['apirand1']['username'])
    new_data = {'firstname': 'Firsname3', 'lastname': 'Lastname3', 'phone': 'Phone3'}
    update_code = put_user_data(token1, setup.users['apirand1']['username'], new_data)
    pass
