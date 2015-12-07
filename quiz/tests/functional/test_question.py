# coding=utf-8
"""Make a question feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/question.feature', 'Get a question')
def test_get_a_question():
    """Get a question."""


@given('user selected lesson 1')
def user_selected_lesson_1():
    """user selected lesson 1."""


@when('user receive a screen with the question about lesson 1')
def user_receive_a_screen_with_the_question_about_lesson_1():
    """user receive a screen with the question about lesson 1."""


@then('click in submit')
def click_in_submit():
    """click in submit."""


@then('user will click in answer')
def user_will_click_in_answer():
    """user will click in answer."""

