
import requests
import json
import setup
import logging
import variables
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def get_request(url: str, headers: dict = None, auth: tuple = None) -> requests.Response:
    """Basic get wrap. URL, headers and auth tuple"""
    temphead = {**setup.head, **headers} if headers else setup.head  # merge arrays, setup.head used as basic header
    logger.debug(f"sending GET request to {url}, auth={auth}, headers={headers}")
    return requests.get(url, headers=temphead, auth=auth)


def post_request(url: str, headers: dict = None, payload: dict = None) -> requests.Response:
    """Basic post wrap. URL, headers and payload"""
    temphead = {**setup.head, **headers} if headers else setup.head  # merge arrays, setup.head used as basic header
    logger.debug(f"sending POST request to {url}, payload={payload}, headers={headers}")
    return requests.post(url, headers=temphead, json=payload)


def put_request(url: str, headers: dict = None, payload: dict = None) -> requests.Response:
    """Basic put wrap. URL, headers and payload"""
    temphead = {**setup.head, **headers} if headers else setup.head  # merge arrays, setup.head used as basic header
    logger.debug(f"sending PUT request to {url}, payload={payload}, headers={headers}")
    return requests.put(url, headers=temphead, json=payload)


def get_token(uname: str, passwd: str, url: str = None) -> (int, str):
    """GET token, return (status, token)"""
    url = setup.host + setup.token_route if not url else url
    logger.debug(f"getting token {url}, uname={uname}, pwd={passwd}")
    res = get_request(url, auth=(uname, passwd))
    token = json.loads(res.content)['token'] if 'token' in json.loads(res.content).keys() else ''
    return res.status_code, token


def get_users(token: str, url: str = None) -> (int, list):
    """GET users list, return (status, list)"""
    url = setup.host + setup.user_route if not url else url
    logger.debug(f"getting user list {url}, token={token}")
    res = get_request(url, headers={'token': token})
    payload = json.loads(res.content)['payload'] if 'payload' in json.loads(res.content).keys() else []
    return res.status_code, payload


def post_user(data: dict, url: str = None) -> int:
    """POST new user, return status"""
    url = setup.host + setup.user_route if not url else url
    logger.debug(f"posting new user {url}, data={data}")
    res = post_request(url, payload=data)
    return res.status_code


def get_user_details(token: str, uname: str, url: object = None) -> (int, dict):
    """GET user info, return dict"""
    url = setup.host + setup.user_route + '/' + uname if not url else url
    logger.debug(f"getting user details {url}, uname={uname}, token={token}")
    res = get_request(url, headers={'token': token})
    payload = json.loads(res.content)['payload'] if 'payload' in json.loads(res.content).keys() else []
    return res.status_code, payload


def put_user_data(token: str, uname: str, data: dict, url: str = None) -> int:
    """PUT updated user info, return code"""
    url = setup.host + setup.user_route + '/' + uname if not url else url
    logger.debug(f"put new user info {url}, uname={uname}, data={data}, token={token}")
    res = put_request(url, headers={'token': token}, payload=data)
    return res.status_code


if __name__ == '__main__':
    #  post user
    #  get token
    #  list users
    #  get user details
    #  update user details
    post_code = post_user(variables.apirand1)
    post_code2 = post_user(variables.apirand2)
    token_code1, token1 = get_token(variables.apirand1['username'], variables.apirand1['password'])
    token_code2, token2 = get_token(variables.apirand2['username'], variables.apirand2['password'])
    #  list_code, user_list = get_users(token1)
    #  det_code, user_det = get_user_details(token1, setup.users['apirand1']['username'])
    new_data = {'firstname': 'Firsname3', 'lastname': 'Lastname3', 'phone': 'Phone3'}
    update_code = put_user_data(token1, variables.apirand1['username'], new_data)
    print(update_code)
    new_password = {'password': 'NEWPASS', 'firstname': 'Firsname3', 'lastname': 'Lastname3', 'phone': 'Phone3'}
    update_code2 = put_user_data(token2, variables.apirand2['username'], new_data)
    print(update_code2)
    new_username = {'username': 'NEWPASS', 'firstname': 'Firsname3', 'lastname': 'Lastname3', 'phone': 'Phone3'}
    update_code3 = put_user_data(token2, variables.apirand2['username'], new_data)
    print(update_code2)
    pass
