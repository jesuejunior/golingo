# -*- coding: utf-8 -*-
from behave import given, then, when
from model_mommy import mommy
from django.contrib.auth.models import User


@given(u'Barbudao, an user')
def step_impl(context):
    mommy.make(User, username='barbudao', email='barbudao@barbudao.com',
               password='1234')

    assert User.objects.count() == 1


@when(u'Barbudao logs in')
def step_impl(context):
    br = context.browser
    response = br.get(context.browser_url('/accounts/login/'))
    assert response.status_code

    # br.select_form(nr=0)
    # br.form['username'] = 'barbudao'
    # br.form['password'] = '1234'
    # br.submit()


@then(u'he sees the foo blah')
def step_impl(context):
    assert False
