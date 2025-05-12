Feature: User Registration

  Scenario: User can register successfully
    Given I am on the registration page
    When I fill in valid registration details
    And I submit the form
    Then I should be redirected to the dashboard


