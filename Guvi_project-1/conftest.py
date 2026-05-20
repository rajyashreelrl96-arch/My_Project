import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.maximize_window()
    # driver.implicitly_wait(10)
    driver.get("https://www.guvi.in")
    yield driver
    driver.quit()