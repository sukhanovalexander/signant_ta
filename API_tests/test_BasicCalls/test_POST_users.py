from API_tests import api_common as api, setup
import variables
import pytest


def decorate_one_user_added(wrapped_function):
    """Checks that number of users incremented by one"""
    def wrapper(*args, **kwargs):
        list_code, userlist = api.get_users(variables.techuser_token)
        return_value = wrapped_function(*args, **kwargs)
        list_code, userlist2 = api.get_users(variables.techuser_token)
        assert len(userlist2) == len(userlist) + 1
        return return_value
    return wrapper


def decorate_no_user_added(wrapped_function):
    """Checks that number of users incremented by one"""
    def wrapper(*args, **kwargs):
        list_code, userlist = api.get_users(variables.techuser_token)
        return_value = wrapped_function(*args, **kwargs)
        list_code, userlist2 = api.get_users(variables.techuser_token)
        assert len(userlist2) == len(userlist)
        return return_value
    return wrapper


@decorate_one_user_added
def test_create_user_positive():
    code = api.post_user(variables.apirand1)
    assert code == 201
    list_code, userlist = api.get_users(variables.techuser_token)
    assert variables.apirand1['username'] in userlist


@decorate_one_user_added
def test_create_user_no_phone():
    data = variables.new_random_user()
    data['phone'] = ''
    code = api.post_user(data)
    assert code == 201


@decorate_one_user_added
def test_create_user_no_lastname():
    data = variables.new_random_user()
    data['lastname'] = ''
    code = api.post_user(data)
    assert code == 201


@decorate_one_user_added
def test_create_user_no_firstname():
    data = variables.new_random_user()
    data['firstname'] = ''
    code = api.post_user(data)
    assert code == 201


@decorate_no_user_added
def test_create_user_no_password():
    data = variables.new_random_user()
    data['password'] = ''
    code = api.post_user(data)
    assert code >= 400


@decorate_no_user_added
def test_create_user_no_username():
    data = variables.new_random_user()
    data['username'] = ''
    code = api.post_user(data)
    assert code >= 400


@decorate_no_user_added
def test_create_user_empty_data():
    data = {}
    code = api.post_user(data)
    assert code >= 400