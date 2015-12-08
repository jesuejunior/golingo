Feature: List lesson

  Background:
    Given Jack, an logged user in our system
    And Lessons available are:
    | Unity   | Lesson   | Dificulty |
    | Unity 1 | Lesson 1 | Easy      |
    | Unity 2 | Lesson 2 | Medium    |

  Scenario: List lessons available
    When Jack is in the home page
    Then Jack gets a list of available lessons

  Scenario: Lesson's dificulty must be shown
    When Jack is in the home page
    Then Jack gets a list of available lessons

  Scenario: Lesson's compelted must be shown
    Given Jack has completed "Lesson 1"
    When Jack is in the home page
    Then Jack sees that "Lesson 1" is completed
