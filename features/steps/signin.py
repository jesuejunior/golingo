# -*- coding: utf-8 -*-
from behave import given, then, when


@given(u'Nicolas, an user')
def step_impl(context):
    print('pass')


@when(u'Nicolas logs in')
def step_impl(context):
    print('pass')


@then(u'he sees the foo blah')
def step_impl(context):
    print('pass')