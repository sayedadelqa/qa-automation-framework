@bdd @ui
Feature: Checkout
  As a logged-in shopper
  I want to complete my purchase
  So that I receive my order

  Background:
    Given the user is logged in
    And the user adds "Sauce Labs Backpack" to the cart
    And the user opens the cart

  @smoke
  Scenario: Completing a purchase with valid information
    When the user starts checkout
    And the user submits valid checkout information
    And the user finishes the order
    Then the order confirmation says "Thank you for your order!"

  @regression
  Scenario: First name is required at checkout
    When the user starts checkout
    And the user submits checkout information with first name "" last name "Adel" and postal code "12345"
    Then the checkout error contains "First Name is required"
