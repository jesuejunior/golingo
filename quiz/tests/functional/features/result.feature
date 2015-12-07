Feature: Get result of a lesson
  # Enter feature description here

  Background:
    Given "Lesson 1" has the following questions:
      | ID | Question                      | Option 1 | Option 2 | Option 3 |
      | 01 | What is the color of the sky? | Blue     | Green    | Yellow   |
      | 02 | What animal Jerry is?         | Rat      | Dog      | Cat      |

  Scenario: Score 100%
    Given Jack submitted the following questions:
      |Question | Answer |
      | 01      | Blue   |
      | 02      | Rat    |
    Then Jack should receive the message "Score: 100%"

  Scenario: Score 0%
    Given Jack submitted the following questions:
      |Question | Answer |
      | 01      | Green  |
      | 02      | Dog    |
    Then Jack should receive the message "Score: 0%"

  Scenario: Score 50%
    Given Jack submitted the following questions:
      |Question | Answer |
      | 01      | Blue   |
      | 02      | Dog    |
    Then Jack should receive the message "Score: 50%"

  Scenario: E-mail of lesson's resume
    Given Jack has submitted his answers
    Then Jack can choose to receive an e-mail with his results
    And an e-mail must be delivered to Jack's inbox with his results

