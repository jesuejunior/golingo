Feature: Submit a lesson
  In order to improve English skills
  Users should be able to practice their skills answering English lessons

  Scenario: Start a lesson
    Given Jack selects Lesson 1
    Then Jack receives the first question of Lesson 1

  Scenario: Answer the first question of a lesson
    Given Jack receives the first question of Lesson 1
    When Jack chooses an answer to the question
    Then Jack receives the next question of Lesson 1

  Scenario: Answer the final question of a lesson
    Given Jack receives the last question of Lesson 1
    When Jack chooses an answer to the question
    Then Jack receives the result of Lesson 1
