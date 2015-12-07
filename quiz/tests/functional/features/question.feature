# Created by jesuejunior at 12/6/15
Feature: Make a question
  To improve English
  Users should be able to answer a question

  Scenario: Get a question
    Given user selected lesson 1
    When user receive a screen with the question about lesson 1
    Then user will click in answer
    And click in submit
