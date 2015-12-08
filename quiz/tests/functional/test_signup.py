# coding=utf-8
"""Signup in the application feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/signup.feature', 'Can\'t signup with blank e-mail')
def test_cant_signup_with_blank_email():
    """Can't signup with blank e-mail."""


@scenario('features/signup.feature', 'Can\'t signup with blank password')
def test_cant_signup_with_blank_password():
    """Can't signup with blank password."""


@scenario('features/signup.feature', 'Can\'t signup with blank password_confirmation')
def test_cant_signup_with_blank_password_confirmation():
    """Can't signup with blank password_confirmation."""


@scenario('features/signup.feature', 'Can\'t signup with blank username')
def test_cant_signup_with_blank_username():
    """Can't signup with blank username."""


@scenario('features/signup.feature', 'Can\'t signup with different password and password_confirmation')
def test_cant_signup_with_different_password_and_password_confirmation():
    """Can't signup with different password and password_confirmation."""


@scenario('features/signup.feature', 'Can\'t signup with existing e-mail')
def test_cant_signup_with_existing_email():
    """Can't signup with existing e-mail."""


@scenario('features/signup.feature', 'Can\'t signup with existing username')
def test_cant_signup_with_existing_username():
    """Can't signup with existing username."""


@scenario('features/signup.feature', 'Successful signup')
def test_successful_signup():
    """Successful signup."""


@given('An user with email "carol@hotmail.com"')
def an_user_with_email_carolhotmailcom():
    """An user with email "carol@hotmail.com"."""


@given('An user with username "neko"')
def an_user_with_username_neko():
    """An user with username "neko"."""


@given('Caroline is a student and wants to learn english')
def caroline_is_a_student_and_wants_to_learn_english():
    """Caroline is a student and wants to learn english."""


@given('Fernando is preparing himself to travel to USA and wants to learn english')
def fernando_is_preparing_himself_to_travel_to_usa_and_wants_to_learn_english():
    """Fernando is preparing himself to travel to USA and wants to learn english."""


@given('Roberto doesn\'t know english and find golingo')
def roberto_doesnt_know_english_and_find_golingo():
    """Roberto doesn't know english and find golingo."""


@when('Filling the form he leave the password input blank')
def filling_the_form_he_leave_the_password_input_blank():
    """Filling the form he leave the password input blank."""


@when('Filling the form he leave the password_confirmation input blank')
def filling_the_form_he_leave_the_password_confirmation_input_blank():
    """Filling the form he leave the password_confirmation input blank."""


@when('Filling the form he leave the username input blank')
def filling_the_form_he_leave_the_username_input_blank():
    """Filling the form he leave the username input blank."""


@when('Filling the form he type in the username input "neko"')
def filling_the_form_he_type_in_the_username_input_neko():
    """Filling the form he type in the username input "neko"."""


@when('Filling the form she does not type in the email input')
def filling_the_form_she_does_not_type_in_the_email_input():
    """Filling the form she does not type in the email input."""


@when('Filling the form she type in the email input "carol@hotmail"')
def filling_the_form_she_type_in_the_email_input_carolhotmail():
    """Filling the form she type in the email input "carol@hotmail"."""


@when('He goes to the signup form and in the <field> he types <input>')
def he_goes_to_the_signup_form_and_in_the_field_he_types_input():
    """He goes to the signup form and in the <field> he types <input>."""


@then('He sees "He already have an user using this username"')
def he_sees_he_already_have_an_user_using_this_username():
    """He sees "He already have an user using this username"."""


@then('He sees "Password Confirmation: - This field is required."')
def he_sees_password_confirmation__this_field_is_required():
    """He sees "Password Confirmation: - This field is required."."""


@then('He sees "Password confirmation:  - The two password fields didn\'t match."')
def he_sees_password_confirmation___the_two_password_fields_didnt_match():
    """He sees "Password confirmation:  - The two password fields didn't match."."""


@then('He sees "Password: - This field is required."')
def he_sees_password__this_field_is_required():
    """He sees "Password: - This field is required."."""


@then('He sees "Username: - This field is required."')
def he_sees_username__this_field_is_required():
    """He sees "Username: - This field is required."."""


@then('He succesfuly singup and is redirect to the home page')
def he_succesfuly_singup_and_is_redirect_to_the_home_page():
    """He succesfuly singup and is redirect to the home page."""


@then('She sees "Email: - This field is required."')
def she_sees_email__this_field_is_required():
    """She sees "Email: - This field is required."."""


@then('She sees "He already have an user using this email"')
def she_sees_he_already_have_an_user_using_this_email():
    """She sees "He already have an user using this email"."""


@then('| e-mail               | roberto@gemail.com|')
def _email________________robertogemailcom():
    """| e-mail               | roberto@gemail.com|."""


@then('| field                | input |')
def _field_________________input_():
    """| field                | input |."""


@then('| password             | q1w2e3|')
def _password______________q1w2e3():
    """| password             | q1w2e3|."""


@then('| password_confirmation| q1w2e3|')
def _password_confirmation_q1w2e3():
    """| password_confirmation| q1w2e3|."""


@then('| username             | roberto_roberto|')
def _username______________roberto_roberto():
    """| username             | roberto_roberto|."""

