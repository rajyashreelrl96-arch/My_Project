from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from Feature.features.login_page import Login

URL = "https://zenclass.in/login"

@given('User navigates to zen portal login')
def step_open_url(context):
    context.driver = webdriver.Chrome()
    context.driver.get(URL)
    context.login_page = Login(context.driver)

@when('User enters valid username "{username}" and password "{password}"')
def step_valid_login(context, username, password):
    context.driver.find_element(By.NAME, "email").send_keys(username)
    context.driver.find_element(By.NAME, "password").send_keys(password)

@when('User clicks login button')
def step_click_login(context):
    context.login_page.click_login()


@when('User enters valid username and password')
def step_valid_login(context):
    context.driver.find_element(By.NAME, "email").send_keys("rajyashreelrl96@gmail.com")
    context.driver.find_element(By.NAME, "password").send_keys("Marcheight0821")

@when('User clicks login button')
def step_click_login(context):
    context.login_page.click_login()

@then('user should be logged in successfully')
def step_success(context):
    assert "dashboard" in context.driver.current_url.lower()

@when('User Enters invalid username and password')
def step_invalid_login(context):
    context.driver.find_element(By.NAME, "email").send_keys("wrongemail")
    context.driver.find_element(By.NAME, "password").send_keys("wrongpass")

@then("Error message should be displayed")
def step_error_message(context):
    assert "Invalid" in context.login_page.error_message()

@then("Login button should be clickable")
def step_login_button_clickable(context):
    assert context.login_page.is_login_button_enabled()

@when("user logged in")
def step_user_logged_in(context):
    step_open_url(context)
    step_valid_login(context)
    step_click_login(context)

@then("Logout button should be clickable")
def step_logout_button_clickable(context):
    context.login_page.click_logout()
