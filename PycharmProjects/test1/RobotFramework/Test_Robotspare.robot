*** Settings ***
Documentation        RobotSparesIndustries
Library              SeleniumLibrary

*** Variables ***
${Browser}           chrome
${URL}               https://robotsparebinindustries.com/
${Username}          maria
${Password}          thoushallnotpass

*** Test Cases ***
Open Browser and Navigate the Application
    Open Browser      ${URL}      ${Browser}
    Maximize Browser Window
    Set Selenium Implicit Wait    3s


Input Valid credentials and Submit the form
    Open Browser        https://robotsparebinindustries.com/
    Log To Console      Login Page loaded for RobotSpareBin website
    Input Text          id:username              maria
    Input Password      id:password              thoushallnotpass
    Click Button        xpath=//button[@type='submit']
    Close Browser


Verify the Login
    Open Browser        ${URL}            ${Browser}
    Log To Console      Login page loaded for RobotSpareBin website
    Set Selenium Implicit Wait    2 seconds
    Element Should Be Visible    id:username        Username field is visible
    Input Text            id:username               ${Username}
    Element Should Be Visible    name:password        Password field is visible
    Input Text              name:password           ${Password}
    Element Should Be Visible    xpath=//button[@type='submit']      submit button is visible
    Click Button            xpath=//button[@type='submit']
    Close Browser

Logout of the Application
     Open Browser        ${URL}            ${Browser}
    Log To Console      Login page loaded for RobotSpareBin website
    Set Selenium Implicit Wait    2 seconds
    Element Should Be Visible    id:username        Username field is visible
    Input Text            id:username               ${Username}
    Element Should Be Visible    name:password        Password field is visible
    Input Text              name:password           ${Password}
    Element Should Be Visible    xpath=//button[@type='submit']      submit button is visible
    Click Button            xpath=//button[@type='submit']
    Click Button                           xpath=//button[text()='Log out']
    Close Browser