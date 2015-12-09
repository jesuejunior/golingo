Feature: Get result of a lesson

  Background:
    Given Jack has a username test_result & password test_result
    And Jack submitted lesson 1 having 2 questions

  Scenario: Score 0%
    Given 2 answers are wrong and 0 answers are correct
    Then Jack should receive a list with his score (0%)

  Scenario: Score 50%
    Given 1 answers are wrong and 1 answers are correct
    Then Jack should receive a list with his score (50%)

  Scenario: Score 100%
    Given 0 answers are wrong and 2 answers are correct
    Then Jack should receive a list with his score (100%)