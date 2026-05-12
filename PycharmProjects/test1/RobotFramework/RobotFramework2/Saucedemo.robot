*** Settings ***
Documentation              My Saucedemo project
Library                    SeleniumLibrary

*** Variables ***
${URL}                      https://www.saucedemo.com/
${Browser}                  Chrome
${User_id}                  standard_user
${Password}                 secret_sauce

*** Test Cases ***
Verify that user lands on the product page
    Open Browser               ${URL}    ${Browser}
    Log To Console                 User lands on the product page
    Set Selenium Implicit Wait     5s
    Element Should Be Visible      id:user-name     Username Field is visible
    Input Text                     id:user-name            ${User_id}
    Element Should Be Visible      id:password
    Input Password                 id:password            ${Password}
    Element Should Be Visible      id:login-button        Submit button is visible
    Click Button                   id:login-button
    Page Should Contain            Sauce Labs Backpack
    Close Browser

Login with Invalid credentials and verify error message is displayed
    Open Browser                ${URL}             ${Browser}
    Log To Console              User gets error message for invalid credentials
    Set Selenium Implicit Wait    5s
    Element Should Be Visible    id:user-name        Username Field is visible
    Input Text                   id:user-name         wrong_user
    Element Should Be Visible    id:password
    Input Password               id:password          wrong_pass
    Element Should Be Visible    id:login-button        Submit button is visible
    Click Button                 id:login-button
    Wait Until Element Is Visible  //h3[@data-test='error']
    Element Should Contain        //h3[@data-test='error']   Epic sadface
    Close Browser

Verify the product is listed correctly
    Open Browser               ${URL}    ${Browser}
    Log To Console                 User lands on the product page
    Set Selenium Implicit Wait     5s
    Element Should Be Visible      id:user-name     Username Field is visible
    Input Text                     id:user-name            ${User_id}
    Element Should Be Visible      id:password
    Input Password                 id:password            ${Password}
    Element Should Be Visible      id:login-button        Submit button is visible
    Click Button                   id:login-button
    Page Should Contain            Sauce Labs Backpack
    Click Button                   //button[@id="add-to-cart-sauce-labs-backpack"]
    Click Element                  //a[@class='shopping_cart_link']
    Wait Until Element Is Visible  //div[@class='cart_item']
    Element Should Be Visible      //div[@class='cart_item']
    Close Browser

Add Multiple items to the Cart and proceed to the Checkout page
    Open Browser               ${URL}    ${Browser}
    Log To Console                 User lands on the product page
    Set Selenium Implicit Wait     3s
    Element Should Be Visible      id:user-name     Username Field is visible
    Input Text                     id:user-name            ${User_id}
    Element Should Be Visible      id:password
    Input Password                 id:password            ${Password}
    Element Should Be Visible      id:login-button        Submit button is visible
    Click Button                   id:login-button
    Page Should Contain            Sauce Labs Backpack
    Click Button                   //button[@id="add-to-cart-sauce-labs-backpack"]
    Click Button                   //button[@id='add-to-cart-sauce-labs-onesie']
    Click Element                  //a[@class='shopping_cart_link']
    Click Button                   //button[@id='checkout']
    Wait Until Element Is Visible  //div[@class='cart_item']
    Element Should Be Visible      //div[@class='cart_item']
    Close Browser
