Feature: As a user I want to log in to the system

  Scenario: simple login with correct credentials
    Given the user with username "admin" and password "pass1234" has been created
    And the user has logged out
    When the user navigates to the login page
    And the user tries to log in with username "admin" and password "pass1234"
    Then the user should be redirected to the home page

  Scenario: simple login with incorrect credentials
    Given the user with username "admin" and password "pass1234" has been created
    And the user has logged out
    When the user navigates to the login page
    And the user tries to log in with username "admin" and password "pass123"
    Then the error message should be displayed in the login page
