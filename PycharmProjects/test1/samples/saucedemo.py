from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#initialize Chrome driver
driver=webdriver.Chrome()
driver.maximize_window()
#open sauceDemo website
driver.get("https://www.saucedemo.com/")
time.sleep(10)
#login with valid credentials
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
time.sleep(10)
#fetch title of the webpage
title = driver.title
print("Title of the webpage",title)
#fetch current URL
current_url = driver.current_url
print("Current url",current_url)
#extract entire webpage
page_text =driver.page_source
#save webpage content to a text file
with open("webpage_text_11.txt", "w", encoding="utf-8") as file:
  file.write(page_text)
print("webpage content to a webpage_text_11.txt")
driver.quit()

#pytest based positive test case

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
def verify_title(setup):
    "verify title"
    assert setup.title == "Swag labs"
def current_url(setup):
    "current url"
    assert setup.current_url == "https://www.saucedemo.com/"
def verify_login(setup):
    "verify login"
    setup.find_element(By.ID,"username").send_keys("standard_user")
    setup.find_element(By.ID,"password").send_keys("secret_sauce")
    setup.find_element(By.ID,"login-button").click()
    time.sleep(3)

    assert "inventory" in setup.current_url

#pytest based negative test case
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.quit()
def verify_invalid_login(setup):
    "verify error message for invalid login"
    assert setup.find_element(By.ID,"user-name").send_keys("wrong_user")
    assert setup.find_element(By.ID,"password").send_keys("wrong_pwd")
    assert setup.find_element(By.ID,"login-button").click()
    time.sleep(3)

    error_msg = setup.find_element(By.XPATH,"//h3").text
    assert "epic sadface" in error_msg
def verify_without_login(setup):
    "verify URL is not accessible without login"
    setup.get("https://www.saucedemo.com/")
    time.sleep(3)
    assert setup.current_url == "https://www.saucedemo.com/"


