Feature: Login in the application

  Scenario: Successful login
    Given Jack, an user with password 1234
    When Jack logs in with password 1234
    Then he sees the foo blah

  Scenario: Login fails for unregistred user
    When Jack logs in with password 1234
    Then login fails

  Scenario: Login fails for invalid user
    Given Jack, an user with password 1234
    When Jack logs in with password errado
    Then login fails
