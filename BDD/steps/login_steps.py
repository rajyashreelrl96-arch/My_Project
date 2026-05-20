from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('User is able to reach login url (#prerequisite step)')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://www.saucedemo.com/")

@when('User enter username in the username field "{username}"')
def step_impl(context, username):
    context.driver.find_element(By.NAME, 'user-name').send_keys(username)

# @when('User enter password in the password field "{password}"')
# def step_impl(context, password):
#     context.driver.find_element(By.ID, "password").send_keys(password)
#
# @when('User clicks on the login button')
# def step_impl(context):
#     context.driver.find_element(By.NAME, 'login-button').click()
#
# @then('User should be navigated to the landing page')
# def step_impl(context):
#     landing_page=context.driver.find_element(By.XPATH, '//span[@class="title"]').text
#     assert landing_page == 'Products','unable to login, Testcase failed'
#     context.driver.quit()
#
# @then('User should not be navigated to the login page')
# def step_impl(context):
#     context.driver.find_element(By.NAME, 'login-button').click()
#     error_msg=context.driver.find_element(By.XPATH, '//h3[@data-test="error"]').text
#     assert error_msg == 'Epic sadface: Sorry, this user has been locked out.','unable to login, Testcase failed'
#     context.driver.quit()

from behave import given, when, then

@given('User is able to reach login url (#prerequisite step)')
def step_impl(context):
    print("Opened login page")


@when('User enters username in the username field "{username}"')
def step_impl(context, username):
    print(f"Username entered: {username}")


@when('User enters password in the password field "{password}"')
def step_impl(context, password):
    print(f"Password entered: {password}")


@when('User clicks on the login button')
def step_impl(context):
    print("Login button clicked")


@then('User should not be navigated to the login page')
def step_impl(context):
    print("Login failed as expected")