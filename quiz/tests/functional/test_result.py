# coding=utf-8
from django.contrib.auth.models import User
from model_mommy import mommy
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    parsers
)
from quiz.models import Lesson, Result

DOMAIN = 'http://localhost:8000'


def connect(browser):
    browser.visit(DOMAIN)
    browser.fill('username', 'test_result')
    browser.fill('password', 'test_result')
    browser.find_by_xpath('//input[@type="submit"]')[0].click()


@given('Jack has a username test_result & password test_result')
def background(browser):
    User.objects.create_user(username='test_result', password='test_result')
    connect(browser)


@given('Jack submitted lesson 1 having 2 questions')
def _background():
    mommy.make(Lesson, name='Lesson 1')


@given(parsers.parse('{wrong:d} answers are wrong and {correct:d} answers are correct'))
def submit_answers(wrong, correct):
    Result.objects.create(
        user_id=1,
        lesson_id=1,
        correct=correct,
        wrong=wrong
    )


@then('Jack should receive a list with his score (0%)')
def jack_should_receive_the_message_score_0(browser):
    browser.visit('%s/results/%s' % (DOMAIN, 1))
    scores = browser.find_by_xpath('//tbody/tr').text

    assert 'Lesson 1' in scores
    assert '0' in scores
    assert '2' in scores


@pytest.mark.django_db
@scenario('features/result.feature', 'Score 0%')
def test_score_0(browser):
    assert browser.url == 'http://localhost:8000/results/1'


@then('Jack should receive a list with his score (50%)')
def jack_should_receive_the_message_score_50(browser):
    browser.visit('%s/results/%s' % (DOMAIN, 1))
    scores = browser.find_by_xpath('//tbody/tr').text

    assert 'Lesson 1' in scores
    assert '1' in scores
    assert '1' in scores


@pytest.mark.django_db
@scenario('features/result.feature', 'Score 50%')
def test_score_50(browser):
    assert browser.url == 'http://localhost:8000/results/1'


@then('Jack should receive a list with his score (100%)')
def jack_should_receive_the_message_score_100(browser):
    browser.visit('%s/results/%s' % (DOMAIN, 1))
    scores = browser.find_by_xpath('//tbody/tr').text

    assert 'Lesson 1' in scores
    assert '0' in scores
    assert '2' in scores


@pytest.mark.django_db
@scenario('features/result.feature', 'Score 100%')
def test_score_100(browser):
    assert browser.url == 'http://localhost:8000/results/1'


# @scenario('features/result.feature', 'E-mail of lesson\'s resume')
# def test_email_of_lessons_resume():
#     """E-mail of lesson's resume."""


# @given('Jack has submitted his answers')
# def jack_has_submitted_his_answers():
#     """Jack has submitted his answers."""


# @then('Jack can choose to receive an e-mail with his results')
# def jack_can_choose_to_receive_an_email_with_his_results():
#     """Jack can choose to receive an e-mail with his results."""


# @then('an e-mail must be delivered to Jack\'s inbox with his results')
# def an_email_must_be_delivered_to_jacks_inbox_with_his_results():
#     """an e-mail must be delivered to Jack's inbox with his results."""




