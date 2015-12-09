# coding=utf-8
"""Signup in the application feature tests."""
import pytest
from django.contrib.auth.models import User
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@pytest.mark.django_db
@scenario('features/signup.feature', 'Can\'t signup with blank e-mail')
def test_cant_signup_with_blank_email():
    """Can't signup with blank e-mail."""


@pytest.mark.django_db
@scenario('features/signup.feature', 'Can\'t signup with blank password')
def test_cant_signup_with_blank_password():
    """Can't signup with blank password."""


@pytest.mark.django_db
@scenario('features/signup.feature', 'Can\'t signup with blank password_confirmation')
def test_cant_signup_with_blank_password_confirmation():
    """Can't signup with blank password_confirmation."""


@pytest.mark.django_db
@scenario('features/signup.feature', 'Can\'t signup with blank username')
def test_cant_signup_with_blank_username():
    """Can't signup with blank username."""


@pytest.mark.django_db
@scenario('features/signup.feature', 'Can\'t signup with different password and password_confirmation')
def test_cant_signup_with_different_password_and_password_confirmation():
    """Can't signup with different password and password_confirmation."""


@pytest.mark.django_db
@scenario('features/signup.feature', 'Can\'t signup with existing e-mail')
def test_cant_signup_with_existing_email():
    """Can't signup with existing e-mail."""


@pytest.mark.django_db
@scenario('features/signup.feature', 'Can\'t signup with existing username')
def test_cant_signup_with_existing_username():
    """Can't signup with existing username."""


@pytest.mark.django_db
@scenario('features/signup.feature', 'Successful signup')
def test_successful_signup():
    """Successful signup."""


@given('An user with email "carol@hotmail.com"')
def an_user_with_email_carolhotmailcom(browser):
    """An user with email "carol@hotmail.com"."""
    User.objects.create_user(username='carol', password='114455', email='carol@hotmail.com')


@given('An user with username "neko"')
def an_user_with_username_neko(browser):
    """An user with username "neko"."""
    User.objects.create_user(username='neko', password='123456')


@given('Caroline is a student and wants to learn english')
def caroline_is_a_student_and_wants_to_learn_english(browser):
    """Caroline is a student and wants to learn english."""
    browser.visit('http://localhost:8000/accounts/register/')


@given('Fernando is preparing himself to travel to USA and wants to learn english')
def fernando_is_preparing_himself_to_travel_to_usa_and_wants_to_learn_english(browser):
    """Fernando is preparing himself to travel to USA and wants to learn english."""
    browser.visit('http://localhost:8000/accounts/register/')


@given('Roberto doesn\'t know english and find golingo')
def roberto_doesnt_know_english_and_find_golingo(browser):
    """Roberto doesn't know english and find golingo."""
    browser.visit('http://localhost:8000/accounts/register/')


@when('Filling the form he leave the password input blank')
def filling_the_form_he_leave_the_password_input_blank(browser):
    """Filling the form he leave the password input blank."""
    browser.fill('password1', '')


@when('Filling the form he leave the password_confirmation input blank')
def filling_the_form_he_leave_the_password_confirmation_input_blank(browser):
    """Filling the form he leave the password_confirmation input blank."""
    browser.fill('password2', '')


@when('Filling the form he leave the username input blank')
def filling_the_form_he_leave_the_username_input_blank(browser):
    """Filling the form he leave the username input blank."""
    browser.fill('username', '')


@when('Filling the form he type in the username input "neko"')
def filling_the_form_he_type_in_the_username_input_neko(browser):
    """Filling the form he type in the username input "neko"."""
    browser.fill('username', 'neko')


@when('Filling the form she does not type in the email input')
def filling_the_form_she_does_not_type_in_the_email_input(browser):
    """Filling the form she does not type in the email input."""
    browser.fill('email', '')


@when('Filling the form she type in the email input "carol@hotmail"')
def filling_the_form_she_type_in_the_email_input_carolhotmail(browser):
    """Filling the form she type in the email input "carol@hotmail"."""
    browser.fill('email', 'carol@hotmail')


@when('He goes to the signup form and in the <field> he types <input>')
def he_goes_to_the_signup_form_and_in_the_field_he_types_input(browser):
    """He goes to the signup form and in the <field> he types <input>."""
    browser.visit('http://localhost:8000/accounts/register/')


@then('He sees "We already have an user using this username"')
def he_sees_we_already_have_an_user_using_this_username(browser):
    """He sees "We already have an user using this username"."""
    browser.fill('username', 'neko')
    browser.find_by_id('submit').first.click()
    assert browser.is_text_present("We already have an user using this username") is True


@then('He sees "Password Confirmation: - This field is required."')
def he_sees_password_confirmation__this_field_is_required(browser):
    """He sees "Password Confirmation: - This field is required."."""
    browser.fill('username', 'nicolas')
    browser.fill('password1', '123asd')
    browser.find_by_id('submit').first.click()
    assert browser.is_text_present("This field is required.") is True


@then('He sees "Password confirmation:  - The two password fields didn\'t match."')
def he_sees_password_confirmation___the_two_password_fields_didnt_match(browser):
    """He sees "Password confirmation:  - The two password fields didn't match."."""
    browser.fill('username', 'flavio')
    browser.fill('password1', 'q1w2e3')
    browser.fill('password2', 'q1w2e3s')
    browser.find_by_id('submit').first.click()
    assert browser.is_text_present("The two password fields didn't match.") is True


@then('He sees "Password: - This field is required."')
def he_sees_password__this_field_is_required(browser):
    """He sees "Password: - This field is required."."""
    browser.fill('username', 'teste')
    browser.fill('password2', '445e')
    browser.find_by_id('submit').first.click()
    assert browser.is_text_present("This field is required") is True


@then('He sees "Username: - This field is required."')
def he_sees_username__this_field_is_required(browser):
    """He sees "Username: - This field is required."."""
    browser.fill('password1', 'thiago123')
    browser.fill('password2', 'thiago123')
    browser.find_by_id('submit').first.click()
    assert browser.is_text_present("This field is required") is True


@then('He succesfuly singup and is redirect to the home page')
def he_succesfuly_singup_and_is_redirect_to_the_home_page(browser):
    """He succesfuly singup and is redirect to the home page."""
    browser.find_by_id('submit').first.click()
    assert 'http://localhost:8000' in browser.url


@then('She sees "Email: - This field is required."')
def she_sees_email__this_field_is_required(browser):
    """She sees "Email: - This field is required."."""
    browser.find_by_id('submit').first.click()
    assert browser.is_text_present("This field is required.") is True


@then('She sees "We already have an user using this email"')
def she_sees_we_already_have_an_user_using_this_email(browser):
    """She sees "We already have an user using this email"."""
    browser.find_by_id('submit').first.click()
    assert browser.is_text_present("We already have an user using this email") is True


@then('| e-mail               | roberto@gemail.com|')
def _email________________robertogemailcom(browser):
    """| e-mail               | roberto@gemail.com|."""
    browser.fill('email', 'roberto@gemail.com')


@then('| password             | q1w2e3|')
def _password______________q1w2e3(browser):
    """| password             | q1w2e3|."""
    browser.fill('password1', 'q1w2e3')


@then('| password_confirmation| q1w2e3|')
def _password_confirmation_q1w2e3(browser):
    """| password_confirmation| q1w2e3|."""
    browser.fill('password2', 'q1w2e3')


@then('| username             | roberto_roberto|')
def _username______________roberto_roberto(browser):
    """| username             | roberto_roberto|."""
    browser.fill('username', 'roberto_roberto')
