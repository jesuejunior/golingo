# coding=utf-8
"""Login in the application feature tests."""
from urllib.parse import urljoin
from django.conf import settings

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/signin.feature', 'Login fails for invalid user')
def test_login_fails_for_invalid_user(request, browser):
    """Login fails for invalid user."""
    browser.visit(urljoin(settings.URL, '/accounts/login'))
    assert browser.status_code == 200
    assert browser.url == 'http://127.0.0.1:8000/accounts/login/'


@scenario('features/signin.feature', 'Login fails for unregistred user')
def test_login_fails_for_unregistred_user():
    """Login fails for unregistred user."""


@scenario('features/signin.feature', 'Successful login')
def test_successful_login():
    """Successful login."""


@given('Jack, an user with password 1234')
def jack_an_user_with_password_1234():
    """Jack, an user with password 1234."""


@when('Jack logs in with password 1234')
def jack_logs_in_with_password_1234():
    """Jack logs in with password 1234."""


@when('Jack logs in with password errado')
def jack_logs_in_with_password_errado():
    """Jack logs in with password errado."""


@then('he sees the foo blah')
def he_sees_the_foo_blah():
    """he sees the foo blah."""


@then('login fails')
def login_fails():
    """login fails."""

