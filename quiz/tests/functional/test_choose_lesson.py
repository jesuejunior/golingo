# coding=utf-8
"""Choose a lesson feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/choose_lesson.feature', 'Choose a lesson of dificulty easy')
def test_choose_a_lesson_of_dificulty_easy():
    """Choose a lesson of dificulty easy."""


@scenario('features/choose_lesson.feature', 'Choose a lesson of dificulty hard')
def test_choose_a_lesson_of_dificulty_hard():
    """Choose a lesson of dificulty hard."""


@scenario('features/choose_lesson.feature', 'Choose a lesson of dificulty medium')
def test_choose_a_lesson_of_dificulty_medium():
    """Choose a lesson of dificulty medium."""



