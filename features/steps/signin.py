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
    br = context.browser
    login_page = br.get(context.browser_url('/accounts/login/'))

    login_form = login_page.soup.select(".form-signin")[0]

    # login_form.select("#id_username")[0]['value'] = args.username
    # login_form.select("#id_password")[0]['value'] = args.password

    login_form.input({'id_username': username, 'id_password': password})

    # submit form
    response = br.submit(login_form, login_page.url)
    assert response.status_code == 200


@then('he sees the foo blah')
def step_impl(context):
    br = context.browser
    assert br.geturl().endswith('/home')


@then('login fails')
def step_impl(context):
    br = context.browser
    assert br.geturl().endswith('/accounts/login/')
