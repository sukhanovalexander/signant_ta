from API_tests import api_common as api, setup
import variables
from time import time
import pytest


@pytest.mark.skipif(not variables.UI_tests_executed, reason='Please execute UI tests first')
class TestExistingUsers:
    def test_get_ui_token(self):
        code, token = api.get_token(variables.user1['username'], variables.user1['password'])
        assert code == 200 and len(token) > 0

    def test_get_ui_user_details(self):
        token_code, token = api.get_token(variables.user1['username'], variables.user1['password'])
        assert token_code < 400, "Failed to get token in API after UI test set"
        det_code, details = api.get_user_details(token, variables.user1['username'])
        assert variables.user1['firstname'] == details['firstname'] and \
               variables.user1['lastname'] == details['lastname'] and variables.user1['phone'] == details['phone'] and \
               det_code < 400

    def test_update_ui_user_details(self):
        new_data = {'firstname': f'updated_{int(time())}', 'lastname': f'updated_{int(time())}'}
        code, token = api.get_token(variables.user1['username'], variables.user1['password'])
        assert code == 200 and len(token) > 0, "Failed to get token in API after UI test set"
        det_code1, det_list1 = api.get_user_details(token, variables.user1['username'])
        put_code = api.put_user_data(token, variables.user1['username'], new_data)
        det_code2, det_list2 = api.get_user_details(token, variables.user1['username'])
        assert put_code == 201 and det_list1['firstname'] != det_list2['firstname']
        variables.user1['firstname'] = new_data['firstname']
        variables.user1['lastname'] = new_data['lastname']

    def test_create_new_user_over_ui(self):
        list_code, userlist = api.get_users(variables.techuser_token)
        assert variables.user1['username'] in userlist
        new_user_data = variables.new_random_user()
        new_user_data['username'] = variables.user1['username']
        code = api.post_user(new_user_data)
        assert code >= 400
        list_code2, userlist2 = api.get_users(variables.techuser_token)
        assert len(userlist2) == len(userlist)

