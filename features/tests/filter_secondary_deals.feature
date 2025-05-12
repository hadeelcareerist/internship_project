
Feature: Filter Secondary Deals by "Want to Buy" Option

  Scenario: User can filter the Secondary deals by "Want to Buy" option
    Given Open the Reelly main page
    And Log in to the page
    When Click on the "Secondary" option at the left side menu
    Then Verify the right page opens
    When Click on Filters
    And Filter the products by “want to buy”
    And Click on Apply Filter
    Then Verify all cards have a “Want to buy” tag


