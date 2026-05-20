Feature: As a QA
  I want test login functionality
  so that i can verify the working of the  functionality
 # Scenario: Test login functonality with valid username and password
  #Given User navigates to url
 # When User enter username in the username field "standard_user"
  #When User enter password in the password field "secret_sauce"
 # And User clicks on the login button
  #And User should be navigated to the landing page

#  @positive
#  Scenario Outline: Test login functionality with different user credentials
#    Given User is able to reach login url (# prerequisite step)
#    When User enters username in the username field "<username>"
#    And  User enters password in the password field "<password>"
#    And  User clicks on the login button
#    Then User should be navigated to the landing page
#    Examples:
#    |  username                   |    password         |
#    |  standard_user              |    secret_sauce     |
#    |  locked_out_user            |    secret_sauce     |
#    |  problem_user               |    secret_sauce     |
#    |  performance_glitch_user    |    secret_sauce     |
#    |  error_user                 |    secret_sauce     |
#    |  visual_user                |    secret_sauce     |
  @negative
  Scenario Outline: Test login functionality with wrong users
    Given User is able to reach login url (#prerequisite step)
    When User enters username in the username field "<username>"
    And  User enters password in the password field "<password>"
    And  User clicks on the login button
    Then User should not be navigated to the login page
    Examples:
    |  username                   |    password         |
    |  standard_users              |    secret_sauce     |
    |  problem_users               |    secret_sauce     |
