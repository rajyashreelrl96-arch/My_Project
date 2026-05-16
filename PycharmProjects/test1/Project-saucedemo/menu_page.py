from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage:

    menu_btn = (By.ID, "react-burger-menu-btn")
    reset_appstate_btn = (By.ID, "reset_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def reset_app_state(self):

        # Click menu button
        self.wait.until(
            EC.element_to_be_clickable(self.menu_btn)
        ).click()

        # Click reset app state
        self.wait.until(
            EC.element_to_be_clickable(self.reset_appstate_btn)
        ).click()

    logout_btn = (By.ID, "logout_sidebar_link")

    def logout(self):

        self.wait.until(
        EC.element_to_be_clickable(self.menu_btn)).click()

        self.wait.until(
        EC.element_to_be_clickable(self.logout_btn)).click()