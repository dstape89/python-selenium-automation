# Created by dstap at 4/26/2021

  Feature: Amazon Search Test

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Jewelry into Amazon search field
    When Click on Amazon search icon
    Then Product results for jewelry are shown on Amazon