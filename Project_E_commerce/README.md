SAUCEDEMO TESTING USING SELENIUM AUTOMATION FRAMEWORK 

Project Overview:

This project is an automated testing framework developed using:

*Python

*Selenium Web Driver

*Pytest

*Page Object Model(POM)

*Allure Report

The framework automates testing of the SauceDemo web application

Project Architecture:
Saucedemo

-->saucedemo.py   (Page object Model)

-->test_saucedemo.py  (Test Cases)

-->allure-attachment   (Allure results)

-->allure-report     (Generate HTML report)

-->README.md (Project Documentation)

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

Usage:

Run all Test Cases - pytest

Run Specific Test case - pytest test_saucedemo.py

Generate HTML Report: 

pytest Project-1/test_saucedemo.py --html=report.html 

Generate Allure Results:

pytest Project-1/test_saucedemo.py --alluredir=allure-reports

Generate Allure Report:

allure generate reports -o allure-report --clean

Open Allure Report:

allure open allure-report



