# Created by dstap at 6/15/2021
Feature: Amazon Best Sellers
  # Enter feature description here

  Scenario: User can verify that there are five links at the top of the Amazon Best Sellers page
    Given Open Amazon Best Sellers page
    Then There are 5 links at the top of the page