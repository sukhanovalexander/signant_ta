from API_tests import api_common as api, setup
import variables
import pytest


@pytest.fixture(scope='session')
def new_user1():
    data = variables.new_random_user()
    api.post_user(data)
    return data


@pytest.fixture(scope='session')
def new_user2():
    data = variables.new_random_user()
    api.post_user(data)
    return data


@pytest.fixture(scope='session')
def new_user3():
    data = variables.new_random_user()
    api.post_user(data)
    return data


def pytest_sessionstart(session):
    api.post_user(variables.techuser)
    code, variables.techuser_token = api.get_token(variables.techuser['username'], variables.techuser['password'])
    code, existing_users = api.get_users(variables.techuser_token)
    variables.UI_tests_executed = True if variables.user1['username'] in existing_users and \
                                          variables.user2['username'] in existing_users else False

    code, user1_token = api.get_token(variables.user1['username'], variables.user1['password'])
    code, data = api.get_user_details(user1_token, variables.user1['username'])
    if data:
        variables.API_after_UI_executed = True if 'updated' in data['firstname'] else False


