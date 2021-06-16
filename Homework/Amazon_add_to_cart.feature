# Created by dstap at 6/15/2021
Feature: Amazon cart

  Scenario: User can add a product to the cart and verify that it is there
    Given Open Amazon page
    When Input "coffee mug" into Amazon search field
    And Click on the first product
    And Click on add to cart button
    Then Verify cart has Amazon Basics Glass Coffee Mug, 13-Ounce, Set of 6 in it