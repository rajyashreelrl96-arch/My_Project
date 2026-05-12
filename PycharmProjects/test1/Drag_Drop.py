import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://jqueryui.com/droppable/")
    yield driver
    driver.quit()
def switch_to_iframe(driver):
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
    driver.switch_to.frame(iframe)
def test_drag_and_drop_positive(setup):
    driver = setup
    switch_to_iframe(driver)
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()
    assert target.text == "Dropped!", "Drag and drop failed"


def test_drag_and_drop_negative(setup):
    driver = setup
    switch_to_iframe(driver)
    target = driver.find_element(By.ID, "droppable")
    assert target.text == "Drop here", "Negative test failed – text changed unexpectedly"