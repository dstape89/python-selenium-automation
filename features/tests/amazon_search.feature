# Created by dstap at 4/26/2021

  Feature: Amazon Search Test

  Scenario: User can search for a product
    Given Open Google page
    When Input Jewelry into search field
    And Click on search icon
    Then Product results for Jewelry are shown on Amazon
    And First result contains Jewelry