Feature: Get result of a lesson

  Scenario: Score 0%
    Given Jack submitted lesson 1 questions
    Then Jack should receive a list with your score (0%)

  Scenario: Score 50%
    Given Jack submitted the following questions
    Then Jack should receive a list with your score (50%)

  Scenario: Score 100%
    Given Jack submitted the following questions
    Then Jack should receive a list with your score (100%)

#  Scenario: E-mail of lesson's resume
#    Given Jack has submitted his answers
#    Then Jack can choose to receive an e-mail with his results
#    And an e-mail must be delivered to Jack's inbox with his results

