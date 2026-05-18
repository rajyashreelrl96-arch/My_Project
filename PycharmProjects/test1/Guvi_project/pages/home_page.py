from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    # homepage Locators
    login_btn = (By.XPATH, "//button[text()='Login']")
    signup_btn = (By.XPATH, "//button[contains(text(),'Sign up')]")

    # Homepage methods
    def click_login(self):
        self.click(self.login_btn)
    def click_signup(self):
        self.click(self.signup_btn)

    def is_login_visible(self):
        return self.is_visible(self.login_btn)

    def is_signup_visible(self):
        return self.is_visible(self.signup_btn)

    def is_menu_visible(self, text):
        return text in self.driver.page_source

    chat_widget = (
        By.XPATH,
        "//*[contains(@aria-label,'Chat Widget')]"
    )

    def chatbot_visible(self):
        return self.is_visible(self.chat_widget)

