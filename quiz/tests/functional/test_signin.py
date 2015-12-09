# coding=utf-8
"""Login in the application feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

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


@when('Jack logs in with password 1234')
def jack_logs_in_with_password_1234(browser):
    """Jack logs in with password 1234."""
    # browser.visit('http://localhost:8000')
    # browser.fill('username', 'jack')
    # browser.fill('password', 'errado')
    # browser.find_by_id('submit').first.click()


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

    assert 'Level 1 - Present Continuous (I am doing)' in browser.find_by_xpath("//tr[@class='success']/th/text()")
    assert 'Level 2 - Past Continuos' in browser.find_by_xpath("//tr[@class='warning']/th/text()")
    assert 'Level 3 - Presente Perfect' in browser.find_by_xpath("//tr[@class='danger']/th/text()")
    # browser.is_element_present_by_text('Level 1 - Present Continuous (I am doing)')
    # browser.is_element_present_by_text('Level 2 - Past Continuos')
    # browser.is_element_present_by_text('Level 3 - Presente Perfect')


@then('login fails')
def login_fails(browser):
    """login fails."""
    assert 'Level 1 - Present Continuous (I am doing)' not in browser.find_by_xpath("//tr[@class='success']/th/text()")
    assert 'Level 2 - Past Continuos' not in browser.find_by_xpath("//tr[@class='warning']/th/text()")
    assert 'Level 3 - Presente Perfect' not in browser.find_by_xpath("//tr[@class='danger']/th/text()")
    # browser.is_element_not_present_by_text('Level 1 - Present Continuous (I am doing)')
    # browser.is_element_not_present_by_text('Level 2 - Past Continuos')
    # browser.is_element_not_present_by_text('Level 3 - Presente Perfect')
    assert 'http://localhost:8000/accounts/login/?next=/' in browser.url


