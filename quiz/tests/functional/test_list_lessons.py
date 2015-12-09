# coding=utf-8
"""List lesson feature tests."""
import pytest
from django.contrib.auth.models import User
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@pytest.mark.django_db
@scenario('features/list_lessons.feature', 'Lesson\'s compelted must be shown')
def test_lessons_compelted_must_be_shown():
    """Lesson's compelted must be shown."""

@pytest.mark.django_db
@scenario('features/list_lessons.feature', 'Lesson\'s dificulty must be shown')
def test_lessons_dificulty_must_be_shown():
    """Lesson's dificulty must be shown."""

@pytest.mark.django_db
@scenario('features/list_lessons.feature', 'List lessons available')
def test_list_lessons_available():
    """List lessons available."""


@given('Jack has completed "Lesson 1"')
def jack_has_completed_lesson_1(browser):
    """Jack has completed "Lesson 1"."""


@given('Jack, an logged user in our system')
def jack_an_logged_user_in_our_system(browser):
    """Jack, an logged user in our system."""
    User.objects.create_user(username='jack', password='q1w2e3')
    browser.visit('http://localhost:8000')
    browser.fill('username', 'jack')
    browser.fill('password', 'q1w2e3')
    browser.find_by_id('submit').first.click()
    import ipdb; ipdb.set_trace()


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
def jack_is_in_the_home_page(browser):
    """Jack is in the home page."""
    assert 'http://localhost:8000/' in browser.url


@then('Jack gets a list of available lessons')
def jack_gets_a_list_of_available_lessons(browser):
    """Jack gets a list of available lessons."""
    assert 'Level 1 - Present Continuous (I am doing)' in browser.find_by_xpath("//tr[@class='success']/th")
    assert 'Level 2 - Past Continuos' in browser.find_by_xpath("//tr[@class='warning']/th")
    assert 'Level 3 - Presente Perfect' in browser.find_by_xpath("//tr[@class='danger']/th")


@then('Jack sees that "Lesson 1" is completed')
def jack_sees_that_lesson_1_is_completed(browser):
    """Jack sees that "Lesson 1" is completed."""
    assert 'fui-check-inverted' in browser.find_by_xpath("//i[@class='fui-check-inverted']/@class")

