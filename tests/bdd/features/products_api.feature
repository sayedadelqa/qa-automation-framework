@bdd @api
Feature: Products API
  As an API consumer
  I want to read and change products
  So that client applications can rely on the service

  @smoke
  Scenario: Retrieve a list of products
    When I send a GET request to "/products?limit=5"
    Then the response status is 200
    And the response contains 5 products

  @regression
  Scenario: Retrieve a single product
    When I send a GET request to "/products/1"
    Then the response status is 200
    And the response has the fields "id, title, price, category"

  @regression
  Scenario: Create a product
    When I send a POST request to "/products/add" with title "qa test"
    Then the response status is 201
    And the response title is "qa test"

  @regression
  Scenario: An unknown product is not found
    When I send a GET request to "/products/99999"
    Then the response status is 404
