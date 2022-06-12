from API_tests import api_common as api, setup
import variables
from time import time
import pytest


def test_put_update_firstname(new_user3):
    new_data = {'firstname': f'updated_{int(time())}'}
    code, token = api.get_token(new_user3['username'], new_user3['password'])
    assert code == 200 and len(token) > 0, "GET token error in PUT test module"
    det_code1, det_list1 = api.get_user_details(token, new_user3['username'])
    put_code = api.put_user_data(token, new_user3['username'], new_data)
    det_code2, det_list2 = api.get_user_details(token, new_user3['username'])
    assert put_code == 201 and det_list1['firstname'] != det_list2['firstname']


def test_put_update_lastname(new_user3):
    new_data = {'lastname': f'updated_{int(time())}'}
    code, token = api.get_token(new_user3['username'], new_user3['password'])
    assert code == 200 and len(token) > 0, "GET token error in PUT test module"
    det_code1, det_list1 = api.get_user_details(token, new_user3['username'])
    put_code = api.put_user_data(token, new_user3['username'], new_data)
    det_code2, det_list2 = api.get_user_details(token, new_user3['username'])
    assert put_code == 201 and det_list1['lastname'] != det_list2['lastname']


def test_put_update_phone(new_user3):
    new_data = {'phone': f'updated_{int(time())}'}
    code, token = api.get_token(new_user3['username'], new_user3['password'])
    assert code == 200 and len(token) > 0, "GET token error in PUT test module"
    det_code1, det_list1 = api.get_user_details(token, new_user3['username'])
    put_code = api.put_user_data(token, new_user3['username'], new_data)
    det_code2, det_list2 = api.get_user_details(token, new_user3['username'])
    assert put_code == 201 and det_list1['phone'] != det_list2['phone']


def test_put_update_password(new_user3):
    new_data = {'password': 'mynewpass'}
    code, token = api.get_token(new_user3['username'], new_user3['password'])
    assert code == 200 and len(token) > 0, "GET token error in PUT test module"
    put_code = api.put_user_data(token, new_user3['username'], new_data)
    code, token = api.get_token(new_user3['username'], new_user3['password'])
    assert code >= 400, "old password should be invalid after change"


def test_put_update_data_other_token(new_user1, new_user3):
    new_data = {'firstname': 'you_are_hacked', f'lastname': f'hacked_by_{new_user1["username"]}'}
    code, token1 = api.get_token(new_user1['username'], new_user1['password'])
    code, token3 = api.get_token(new_user3['username'], new_user3['password'])
    assert code == 200 and len(token1) > 0, "GET token error in PUT test module"
    assert code == 200 and len(token3) > 0, "GET token error in PUT test module"
    det_code1, det_list1 = api.get_user_details(token3, new_user3['username'])
    put_code = api.put_user_data(token1, new_user3['username'], new_data)
    det_code2, det_list2 = api.get_user_details(token3, new_user3['username'])
    assert det_list2['firstname'] != 'you_are_hacked'


def test_put_update_data_no_token(new_user3):
    new_data = {'lastname': f'updated_wo_token_{int(time())}'}
    code, token = api.get_token(new_user3['username'], new_user3['password'])
    assert code == 200 and len(token) > 0, "GET token error in PUT test module"
    det_code1, det_list1 = api.get_user_details(token, new_user3['username'])
    put_code = api.put_user_data('', new_user3['username'], new_data)
    det_code2, det_list2 = api.get_user_details(token, new_user3['username'])
    assert put_code >= 400 and det_list1['lastname'] == det_list2['lastname']


def test_put_update_data_invalid_token(new_user3):
    new_data = {'lastname': f'updated_wrong_token_{int(time())}'}
    code, token = api.get_token(new_user3['username'], new_user3['password'])
    assert code == 200 and len(token) > 0, "GET token error in PUT test module"
    det_code1, det_list1 = api.get_user_details(token, new_user3['username'])
    put_code = api.put_user_data('not_a_token', new_user3['username'], new_data)
    det_code2, det_list2 = api.get_user_details(token, new_user3['username'])
    assert put_code >= 400 and det_list1['lastname'] == det_list2['lastname']

