from API_tests import api_common as api, setup
import variables
import pytest


def test_check_existing_users(new_user1, new_user2):
    code, userlist = api.get_users(variables.techuser_token)
    assert new_user1['username'] in userlist and new_user2['username'] in userlist


def test_check_token_required():
    list_code, userlist = api.get_users('')
    assert list_code >= 400 and len(userlist) == 0


def test_check_positive(new_user1):
    token_code, token = api.get_token(new_user1['username'], new_user1['password'])
    assert token_code < 400, "Failed to get token in GET_users test set"
    list_code, userlist = api.get_users(token)
    assert list_code == 200 and len(userlist) >= 2  # at least techuser and new_user1


def test_check_incorrect_token():
    list_code, userlist = api.get_users('probably_not_a_token')
    assert list_code >= 400 and len(userlist) == 0
