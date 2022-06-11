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

