# Created by dstap at 6/2/2021
Feature: Test Scenarios for empty cart

  Scenario: User can verify that Amazon shopping cart is empty
    Given Open Amazon page
    When Clicks on cart icon
    Then Shopping cart is empty