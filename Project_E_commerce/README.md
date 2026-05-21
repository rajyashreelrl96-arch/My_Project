## SAUCEDEMO TESTING USING SELENIUM AUTOMATION FRAMEWORK 

# Project Overview:

This project is an **automated testing framework** developed using:

- Python

- Selenium Web Driver

- Pytest

- Page Object Model(POM)

- Allure Report

The framework automates testing of the **SauceDemo web application**

## Project Architecture:
### Project_E_commerce

|_pages
  - cart_page.py
  - checkout_page.py
  - inventory_page.py
  - login_page.py
  - menu_page.py

|_tests

  - test_checkout.py
  - test_inventory.py
  - test_login.py
  - test_reset_app.py

|_conftest.py

|_README.md

Features:

1.Automated Login Testing

2.Invalid Login Testing

3.Logout Validation

4.Cart Functionality Testing

5.Random Product Selection

6.Checkout workflow Testing

7.Product Sorting Validation

8.Reset App State Validation

9.Allure-Report

10.Parameterized Test Execution


#### Generate Allure Results:

pytest Project_E_commerce/tests --alluredir=allure-results

**Generate Allure Report:**

allure generate reports -o allure-report --clean

**Open Allure Report:**

allure open allure-report



