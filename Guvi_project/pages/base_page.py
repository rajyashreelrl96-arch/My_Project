from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator):
        return self.wait.until(visibility_of_element_located(locator)).is_displayed()