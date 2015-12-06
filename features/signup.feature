Feature: Signup in the application

  Background:
    * An user with username as "neko"
    * An user with email "carol@hotmail.com"

  Scenario: Successful signup
    * Roberto don't know english and find golingo
    * He goes to the signup form and in the <field> he types <input>
    * He succesfuly singup and is redirect to the home page

  Examples:
    | field                | input |
    | e-mail               | roberto@gemail.com|
    | username             | roberto_roberto|
    | password             | q1w2e3|
    | password_confirmation| q1w2e3|


  Scenario: Can't signup with blank e-mail

  Scenario: Can't signup with existing e-mail
    * Caroline is a student and wants to learn english
    * Filling the form she type in the email input "carol@hotmail"
    * She sees "E-mail já cadastrado"

  Scenario: Can't signup with blank username

  Scenario: Can't signup with existing username
    * Fernando is preparing himself to travel to USA and wants to learn english
    * Filling the form he type in the username input "neko"
    * He sees "Username já cadastrado"

  Scenario: Can't signup with blank password

  Scenario: Can't signup with blank password_confirmation

  Scenario: Can't signup with different password and password_confirmation
