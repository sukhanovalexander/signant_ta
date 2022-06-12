from API_tests import api_common as api, setup
import variables
import pytest
import threading


def test_full_cycle():
    data = variables.new_random_user()
    post_code = api.post_user(data)
    assert post_code == 201, "User was not created"
#    post_code_again = api.post_user(data)
#    assert post_code_again >= 400

    token_code, token = api.get_token(data['username'], data['password'] + 'mistake')
    assert token_code >= 400 and len(token) == 0

    token_code, token = api.get_token(data['username'], data['password'] + 'mistake2')
    assert token_code >= 400 and len(token) == 0
    token_code, token = api.get_token(data['username'], data['password'] + 'mistake3')
    assert token_code >= 400 and len(token) == 0

    token_code, token = api.get_token(data['username'], data['password'])
    assert token_code == 200 and len(token)  # 4 attempts to remember password

    list_code, user_list = api.get_users(token)
    assert list_code < 400 and len(user_list) >= 1

    det_code, det_list = api.get_user_details(token, data['username'])
    assert data['firstname'] == det_list['firstname'] and data['lastname'] == det_list['lastname'] \
           and data['phone'] == det_list['phone'] and det_code < 400

    new_data = {'phone': f'updated_full'}
    put_code = api.put_user_data(token, data['username'], new_data)
    det_code2, det_list2 = api.get_user_details(token, data['username'])
    assert put_code == 201 and det_list2['phone'] == 'updated_full'


def test_multiple_users():
    threads = list()
    for index in range(15):
        x = threading.Thread(target=test_full_cycle, args=[])
        threads.append(x)
        x.start()
    x.join()


