# AUTOMATION TESTING OF ED TECH PLATFORM WEB APPLICATION 

## Project Overview: ##

This project automates testing of the **GUVI website** using **Python, Selenium WebDriver, Pytest, and Page Object Model (POM)**.

The framework is designed to validate key user functionalities such as:

- Homepage verification
- Login functionality
- Invalid login validation
- Logout functionality
- UI element visibility checks

## Project Architecture: ##

The project follows **Page Object Model(POM)**

**Guvi Project**

|_Pages
  
 - base_page.py

 - home_page.py

 - login_page.py

|_tests

- test_home.py

- test_login.py

|_utils

- config.py

|_conftest.py

|_README.md

## Components Description ##

### 1.Pages

**Base_Page.py**

Common reusable Selenium methods:

- click()
- type()
- is_visible()
- wait methods

**Home_page.py**

- Click Login
- Click Signup
- Verify buttons visibility
- Verify menu items
- Verify chatbot widget

**Login_page.py**

- Enter Email
- Enter Password
- Login submission
- Invalid login validation
- Logout functionality

### 2.tests

**test_home.py**
- URL verification
- Title validation
- Login button visibility
- Signup button visibility
- Navigation checks
- Chat assistant validation

**test_login.py**
- Valid Login
- Invalid Login
- Logout verification

### 3. utils/

Contains reusable utilities and configuration files.

#### config.py

Stores:

- Base URL
- Valid credentials
- Test constants

### 4. conftest.py

Contains Pytest fixtures.
Responsible for:

- Browser setup
- ChromeDriver initialization
- Driver teardown
- Test environment configuration



## Test Scenarios Covered

### Homepage

- Verify URL
- Verify webpage title
- Verify login button visibility
- Verify signup button visibility
- Verify navigation menus
- Verify chatbot assistant

### Login

- Successful login validation
- Invalid login validation
- Logout functionality

### Features ###

- Selenium Web Driver Automation

- Pytest Framework

- Page Object Model Design Pattern

- Explicit Wait Implementation

- Reusable Base Page Methods

- Modular Test Design

- Configurable Test Data

### Technologies used ###

- Python 

- Selenium

- Pytest

- WebDriverManager

- ChromeDriver

- Page Object Model(POM)


