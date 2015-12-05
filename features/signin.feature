Feature: Login in the application

  Scenario: Successful Login
    Given Barbudao, an user
    When Barbudao logs in
    Then he sees the foo blah

  Scenario: Login fails for unregistred user


  Scenario: Login fails for invalid user