import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.guvi.in/"

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_link(driver):
    driver.get(URL)
    # live classes
    live_classes = driver.find_element(By.XPATH, "//*[@id='solutions']/p[text()='LIVE Classes']")
    assert live_classes.is_displayed()
    # courses
    courses = driver.find_element(By.XPATH, "//*[@id='solutions']/p[text()='Courses']")
    assert courses.is_displayed()
    # practice
    practice = driver.find_element(By.XPATH, "//*[@id='solutions']/p[text()='Practice']")
    assert practice.is_displayed()
    # resources
    resources = driver.find_element(By.XPATH, "//*[@id='solutions']/p[contains(text(),'Resources')]")
    assert resources.is_displayed()
    # sign up
    sign_up = driver.find_element(By.XPATH, "//*[@id='header-container']/div[1]/div[4]/div/button[text()='Sign up']")
    assert sign_up.is_displayed()
    # login
    login = driver.find_element(By.XPATH, "//*[@id='header-container']/div[1]/div[4]/div/button[text()='Login']")
    assert login.is_displayed()
    driver.quit()

def test_parent_child_xpath(driver):
    driver.get(URL)
    parent_live_classes = driver.find_element(By.XPATH, "//div[@id='solutions']")
    assert parent_live_classes.is_displayed()
    driver.quit()

def test_preceding_sibling_resources(driver):
    driver.get(URL)
    preceding_sibling_resources = driver.find_element(By.XPATH, "//p[text()='Resources']/preceding-sibling::p[1]")
    assert preceding_sibling_resources.is_displayed()
    driver.quit()

def test_following_sibling_practice(driver):
    driver.get(URL)
    practice_following_sibling = driver.find_element(By.XPATH, "//p[text()='Practice Platforms']/following-sibling::p[1]")
    assert practice_following_sibling.is_displayed()
    driver.quit()

def test_ancestor_elements(driver):
    driver.get(URL)
    ancestor_live = driver.find_element(By.XPATH, "(//p[contains(text(), 'LIVE Classes')])[1]/ancestor::div[1]")
    assert ancestor_live.is_displayed()
    driver.quit()