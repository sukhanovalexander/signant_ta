from API_tests import api_common as api, setup
import variables


def test_get_token_positive(new_user1):
    code, token = api.get_token(new_user1['username'], new_user1['password'])
    assert code == 200 and len(token) > 0


def test_get_token_negative(new_user1):
    code, token = api.get_token(new_user1['username'], variables.apirand1['password'])
    assert code > 400 and len(token) == 0


def test_get_token_empty_password(new_user1):
    code, token = api.get_token(new_user1['username'], '')
    assert code > 400 and len(token) == 0


def test_get_token_empty_username(new_user1):
    code, token = api.get_token('', new_user1['password'])
    assert code > 400 and len(token) == 0


def test_get_token_empty_credentials():
    code, token = api.get_token('', '')
    assert code > 400 and len(token) == 0


def test_authorised_request(new_user1):
    code, token = api.get_token(new_user1['username'], new_user1['password'])
    code_det, userdet = api.get_user_details(token, new_user1['username'])
    assert code_det == 200


def test_token_reissue(new_user1):
    code, token = api.get_token(new_user1['username'], new_user1['password'])
    assert code == 200 and len(token) > 0
    code2, token2 = api.get_token(new_user1['username'], new_user1['password'])
    assert code2 == 200 and len(token2) > 0 and token2 != token


def test_token_reissue_old_invalid(new_user1):
    code, token = api.get_token(new_user1['username'], new_user1['password'])
    code2, token2 = api.get_token(new_user1['username'], new_user1['password'])
    code_det, userdet = api.get_user_details(token, new_user1['username'])
    assert code_det == 401


def test_token_reissue_new_valid(new_user1):
    code, token = api.get_token(new_user1['username'], new_user1['password'])
    code2, token2 = api.get_token(new_user1['username'], new_user1['password'])
    code_det, userdet = api.get_user_details(token2, new_user1['username'])
    assert code_det == 200


def test_token_another_user(new_user1, new_user2):
    code_u1, token_u1 = api.get_token(new_user1['username'], new_user1['password'])
    code_u2, token_u2 = api.get_token(new_user2['username'], new_user2['password'])
    code_u1_res, u1_det_res = api.get_user_details(token_u1, new_user2['username'])
    code_u2_res, u2_det_res = api.get_user_details(token_u2, new_user1['username'])
    assert code_u1_res == code_u2_res == 401
    assert len(u1_det_res) == len(u2_det_res) == 0

