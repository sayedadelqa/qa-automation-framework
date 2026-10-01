@bdd @ui
Feature: Shopping cart
  As a logged-in shopper
  I want to manage items in my cart
  So that I only buy what I need

  Background:
    Given the user is logged in

  @smoke
  Scenario: Adding an item updates the cart badge
    When the user adds "Sauce Labs Backpack" to the cart
    Then the cart badge shows 1

  @regression
  Scenario: Removing an item clears the cart badge
    When the user adds "Sauce Labs Backpack" to the cart
    And the user removes "Sauce Labs Backpack" from the cart
    Then the cart badge is not shown

  @regression
  Scenario: The cart lists every added item
    When the user adds "Sauce Labs Backpack" to the cart
    And the user adds "Sauce Labs Bike Light" to the cart
    And the user opens the cart
    Then the cart contains 2 items

  @regression
  Scenario: Products can be sorted by price from low to high
    When the user sorts products by price from low to high
    Then the prices are in ascending order
