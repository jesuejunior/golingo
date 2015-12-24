# coding=utf-8
"""Submit a lesson feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/submit_lesson.feature',
          'Answer the final question of a lesson')
def test_answer_the_final_question_of_a_lesson():
    """Answer the final question of a lesson."""


@scenario('features/submit_lesson.feature',
          'Answer the first question of a lesson')
def test_answer_the_first_question_of_a_lesson():
    """Answer the first question of a lesson."""


@scenario('features/submit_lesson.feature', 'Start a lesson')
def test_start_a_lesson():
    """Start a lesson."""


@given('Jack receives the first question of Lesson 1')
def jack_receives_the_first_question_of_lesson_1():
    """Jack receives the first question of Lesson 1."""


@given('Jack receives the last question of Lesson 1')
def jack_receives_the_last_question_of_lesson_1():
    """Jack receives the last question of Lesson 1."""


@given('Jack selects Lesson 1')
def jack_selects_lesson_1():
    """Jack selects Lesson 1."""


@when('Jack chooses an answer to the question')
def jack_chooses_an_answer_to_the_question():
    """Jack chooses an answer to the question."""


@then('Jack receives the next question of Lesson 1')
def jack_receives_the_next_question_of_lesson_1():
    """Jack receives the next question of Lesson 1."""


@then('Jack receives the result of Lesson 1')
def jack_receives_the_result_of_lesson_1():
    """Jack receives the result of Lesson 1."""
