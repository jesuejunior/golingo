# coding=utf-8
"""Login in the application feature tests."""
import pytest
from django.contrib.auth.models import User
from model_mommy import mommy
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from quiz.models import Unity, Lesson


@pytest.mark.django_db
@scenario('features/signin.feature', 'Login fails for invalid user')
def test_login_fails_for_invalid_user():
    """Login fails for invalid user."""

@pytest.mark.django_db
@scenario('features/signin.feature', 'Login fails for unregistred user')
def test_login_fails_for_unregistred_user():
    """Login fails for unregistred user."""

@pytest.mark.django_db
@scenario('features/signin.feature', 'Successful login')
def test_successful_login():
    """Successful login."""


@given('Jack, an user with password 1234')
def jack_an_user_with_password_1234():
    """Jack, an user with password 1234."""
    User.objects.create_user(username='jack', password='1234')


@when('Jack logs in with password 1234')
def jack_logs_in_with_password_1234(browser):
    """Jack logs in with password 1234."""
    browser.visit('http://localhost:8000')
    browser.fill('username', 'jack')
    browser.fill('password', '1234')
    browser.find_by_id('submit').first.click()


@when('Jack logs in with password errado')
def jack_logs_in_with_password_errado(browser):
    """Jack logs in with password errado."""
    browser.visit('http://localhost:8000')
    browser.fill('username', 'jack')
    browser.fill('password', 'errado')
    browser.find_by_id('submit').first.click()


@then('he sees the list of lessons')
def he_sees_the_list_of_lessons(browser):
    """he sees the foo blah."""
    unity = mommy.make(Unity, name='Unity 2', level=2)
    mommy.make(Lesson, name='Lesson AND', unity=unity)
    browser.reload()

    assert browser.is_text_present('Level 2 - Unity 2') is True


@then('login fails')
def login_fails(browser):
    """login fails."""
    assert browser.is_text_present('Level 2 - Unity 2') is False
    assert 'http://localhost:8000/accounts/login/?next=/' in browser.url


