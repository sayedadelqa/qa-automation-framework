@bdd @ui
Feature: Login
  As a shopper
  I want to log in to the store
  So that I can see products and place orders

  @smoke
  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user logs in with valid credentials
    Then the products page is displayed

  @regression
  Scenario Outline: Login is rejected for invalid credentials
    Given the user is on the login page
    When the user logs in with username "<username>" and password "<password>"
    Then the error message contains "<message>"

    Examples:
      | username        | password        | message                                  |
      | locked_out_user | secret_sauce    | Sorry, this user has been locked out.    |
      | standard_user   | wrong_password  | Username and password do not match       |
      |                 | secret_sauce    | Username is required                     |
      | standard_user   |                 | Password is required                     |
