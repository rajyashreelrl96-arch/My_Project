from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class DashboardPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    PROFILE_ICON = (By.XPATH, "//div[@class='profile-click-icon-div']")
    LOGOUT_BTN = (By.XPATH, "//div[contains(text(),'Log out')]")
    POP_UP = (By.XPATH, "//button[@class='custom-close-button']")

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE_ICON)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BTN)).click()

    def is_logged_out(self):
        try:
            return self.wait.until(EC.url_contains("login"))
        except TimeoutException:
            return False

    def close_popup(self):
        if EC.alert_is_present():
            self.wait.until(EC.element_to_be_clickable(self.POP_UP)).click()
