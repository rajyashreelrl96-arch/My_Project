import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.chrome.service
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless")  # Optional: run in headless mode
    # service = selenium.webdriver.chrome.service.Service()
    # driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

# Positive Test Cases

def test_title(driver):
    """Verify title of the webpage"""
    assert driver.title == "Swag Labs"

def test_homepage_url(driver):
    """Verify current URL of the homepage"""
    assert driver.current_url == "https://www.saucedemo.com/"

def test_valid_login(driver):
    """Verify login with valid credentials"""
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    assert "inventory" in driver.current_url

def test_save_webpage_content(driver):
    """Extract and save webpage content after login"""
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    page_text = driver.page_source
    with open("webpage_text_11.txt", "w", encoding="utf-8") as file:
        file.write(page_text)
    assert len(page_text) > 0

# Negative Test Cases

def test_invalid_login(driver):
    """Verify error message for invalid login"""
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pwd")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    error_msg = driver.find_element(By.XPATH, "//h3").text
    assert "Epic sadface" in error_msg

def test_without_login_access(driver):
    """Verify URL is not redirected without login"""
    assert driver.current_url == "https://www.saucedemo.com/"