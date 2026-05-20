Feature: I want to test zen portal Login

Scenario: Successful Login
  Given User navigates to zen portal login
  When User enters valid username "rajyashreelrl96@gmail.com" and password "Marcheight0821"
  And User clicks login button
  Then user should be logged in successfully


  Scenario: Unsuccessful login
    Given User navigates to zen portal login
    When User Enters invalid username and password
    And User clicks login button
    Then Error message should be displayed

  Scenario: Validate username and password fields
    Given User navigates to zen portal login
    When User enters valid username and password
    Then Login button should be clickable

  Scenario: Validate Submit button
    Given User navigates to zen portal login
    Then Login button should be clickable

  Scenario: Functionality of the Logout button
    Given User navigates to zen portal login
    When user logged in
    Then Logout button should be clickable