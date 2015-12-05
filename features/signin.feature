Feature: Logging in the application

  Scenario: Log into system and sees the foo blah
    Given Nicolas, an user
    When Nicolas logs in
    Then he sees the foo blah