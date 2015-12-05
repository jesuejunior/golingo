# -*- coding: utf-8 -*-
from behave import given, then, when
from model_mommy import mommy
from django.contrib.auth.models import User


@given('{username}, an user with password {password}')
def step_impl(context, username, password):
    mommy.make(User, username=username, email=username + '@domain.com', password=password)

    assert User.objects.count() == 1


@when('{username} logs in with password {password}')
def step_impl(context, username, password):
    browser = context.browser

    browser.visit(context.browser_url('/accounts/login/'))
    browser.fill('username', username)
    browser.fill('password', username)

    browser.find_by_value('login').first.click()


@then('he sees the foo blah')
def step_impl(context):
    browser = context.browser
    assert browser.is_element_present_by_text('Atividades')


@then('login fails')
def step_impl(context):
    browser = context.browser
    assert browser.is_element_present_by_text('Entrar')
