import pytest


def was_ui_executed():
    pass


@pytest.mark.skipif(not was_ui_executed())
def test_login_ui():
    pass