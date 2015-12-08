# coding=utf-8
"""List lesson feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/list_lessons.feature', 'Lesson\'s compelted must be shown')
def test_lessons_compelted_must_be_shown():
    """Lesson's compelted must be shown."""


@scenario('features/list_lessons.feature', 'Lesson\'s dificulty must be shown')
def test_lessons_dificulty_must_be_shown():
    """Lesson's dificulty must be shown."""


@scenario('features/list_lessons.feature', 'List lessons available')
def test_list_lessons_available():
    """List lessons available."""


@given('Jack has completed "Lesson 1"')
def jack_has_completed_lesson_1():
    """Jack has completed "Lesson 1"."""


@given('Jack, an logged user in our system')
def jack_an_logged_user_in_our_system():
    """Jack, an logged user in our system."""


@given('Lessons available are:')
def lessons_available_are():
    """Lessons available are:."""


@given('| Unity   | Lesson   | Dificulty |')
def _unity____lesson____dificulty_():
    """| Unity   | Lesson   | Dificulty |."""


@given('| Unity 1 | Lesson 1 | Easy      |')
def _unity_1__lesson_1__easy______():
    """| Unity 1 | Lesson 1 | Easy      |."""


@given('| Unity 2 | Lesson 2 | Medium    |')
def _unity_2__lesson_2__medium____():
    """| Unity 2 | Lesson 2 | Medium    |."""


@when('Jack is in the home page')
def jack_is_in_the_home_page():
    """Jack is in the home page."""


@then('Jack gets a list of available lessons')
def jack_gets_a_list_of_available_lessons():
    """Jack gets a list of available lessons."""


@then('Jack sees that "Lesson 1" is completed')
def jack_sees_that_lesson_1_is_completed():
    """Jack sees that "Lesson 1" is completed."""

