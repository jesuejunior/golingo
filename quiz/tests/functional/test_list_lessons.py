# coding=utf-8
"""List lesson feature tests."""
import pytest
from django.contrib.auth.models import User
from model_mommy import mommy
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from quiz.models import Unity, Lesson, Result


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


@given('Lessons available are:')
def lessons_available_are():
    """Lessons available are:."""


@given('| Unity   | Lesson   | Dificulty |')
def _unity____lesson____dificulty_():
    """| Unity   | Lesson   | Dificulty |."""


@given('| Unity 1 | Lesson 1 | Easy      |')
def _unity_1__lesson_1__easy______():
    """| Unity 1 | Lesson 1 | Easy      |."""
    unity = mommy.make(Unity, name='Unity 1', level=1)
    mommy.make(Lesson, id=78, name='Lesson OR', unity=unity)
    assert Unity.objects.filter(name='Unity 1').exists()


@given('| Unity 2 | Lesson 2 | Medium    |')
def _unity_2__lesson_2__medium____():
    """| Unity 2 | Lesson 2 | Medium    |."""
    unity = mommy.make(Unity, name='Unity 2', level=2)
    mommy.make(Lesson, name='Lesson AND', unity=unity)
    assert Unity.objects.filter(name='Unity 2').exists()


@when('Jack is in the home page')
def jack_is_in_the_home_page(browser):
    """Jack is in the home page."""
    assert 'http://localhost:8000/' in browser.url


@then('Jack gets a list of available lessons')
def jack_gets_a_list_of_available_lessons(browser):
    """Jack gets a list of available lessons."""
    browser.reload()
    browser.is_text_present('Level 1 - Unity 1') is True
    browser.is_text_present('Level 2 - Unity 2') is True


@then('Jack sees that "Lesson 1" is completed')
def jack_sees_that_lesson_1_is_completed(browser):
    """Jack sees that "Lesson 1" is completed."""
    mommy.make(Result, lesson=Lesson.objects.get(id=78), user=User.objects.get(username='jack'))
    browser.reload()
    bool(browser.find_by_xpath("//i[@class='fui-check-inverted']")) is True
