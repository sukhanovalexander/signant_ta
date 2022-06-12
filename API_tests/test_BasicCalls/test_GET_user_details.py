from API_tests import api_common as api, setup
import variables
import pytest


def test_get_details_positive(new_user2):
    token_code, token = api.get_token(new_user2['username'], new_user2['password'])
    assert token_code < 400, "Failed to get token in GET_user_details test set"
    det_code, details = api.get_user_details(token, new_user2['username'])
    assert new_user2['firstname'] == details['firstname'] and new_user2['lastname'] == details['lastname'] \
           and new_user2['phone'] == details['phone'] and det_code < 400


def test_get_details_no_token(new_user2):
    det_code, details = api.get_user_details('', new_user2['username'])
    assert det_code >= 400 and len(details) == 0


def test_get_details_wrong_token(new_user2):
    det_code, details = api.get_user_details('definetly_not_a_token', new_user2['username'])
    assert det_code >= 400 and len(details) == 0


def test_get_details_valid_other_token(new_user1, new_user2):
    token_code1, token1 = api.get_token(new_user1['username'], new_user1['password'])
    token_code2, token2 = api.get_token(new_user2['username'], new_user2['password'])
    assert token_code1 < 400 and token_code2 < 400, "Failed to get token in GET_user_details test set"
    det_code1, details1 = api.get_user_details(new_user1['username'], token2)
    det_code2, details2 = api.get_user_details(new_user2['username'], token1)
    assert det_code2 >= 400 and det_code2 >= 400 and len(details2) == 0 and len(details2) == 0


