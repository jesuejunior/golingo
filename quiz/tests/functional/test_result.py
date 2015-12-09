# coding=utf-8
from pytest_bdd import (
    given,
    scenario,
    then,
)

DOMAIN = 'localhost:8000'


def connect(browser):
    browser.visit(DOMAIN)
    browser.fill('username', 'test_result')
    browser.fill('password', 'test_result')
    browser.find_by_xpath('//input[@type="submit"]')[0].click()


@given('Jack submitted the following questions')
def jack_submitted_the_following_questions(browser):
    connect(browser)


@then('Jack should receive a list with your score')
def jack_should_receive_the_message_score_0(browser):
    browser.visit('%s/results/%s' % (DOMAIN, 1))
    scores = [row.text for row in browser.find_by_xpath('//tbody/tr')]
    expected_score = 'Present Continuous (I am doing) Lesson 1 0 2 Dec. 9, 2015, 4:12 p.m.'

    assert len(scores) == 1
    assert scores == [expected_score]


@scenario('features/result.feature', 'Score 0%')
def test_score_0(browser):
    assert browser.url == 'http://localhost:8000/results/1'


@then('Jack should receive the message "Score: 50%"')
def jack_should_receive_the_message_score_50(browser):
    browser.visit('%s/results/%s' % (DOMAIN, 3))
    scores = [row.text for row in browser.find_by_xpath('//tbody/tr')]
    expected_score = 'Present Continuous (I am doing) Lesson 3 1 1 Dec. 9, 2015, 4:14 p.m.'

    assert len(scores) == 1
    assert scores == [expected_score]


@scenario('features/result.feature', 'Score 50%')
def test_score_50(browser):
    assert browser.url == 'http://localhost:8000/results/3'


@then('Jack should receive the message "Score: 100%"')
def jack_should_receive_the_message_score_100(browser):
    browser.visit('%s/results/%s' % (DOMAIN, 2))
    scores = [row.text for row in browser.find_by_xpath('//tbody/tr')]
    expected_score = 'Present Continuous (I am doing) Lesson 2 2 0 Dec. 9, 2015, 4:14 p.m.'

    assert len(scores) == 1
    assert scores == [expected_score]


@scenario('features/result.feature', 'Score 100%')
def test_score_100(browser):
    assert browser.url == 'http://localhost:8000/results/2'


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




