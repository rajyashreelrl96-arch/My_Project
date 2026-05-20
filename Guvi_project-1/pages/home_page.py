from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class HomePage(BasePage):
    # homepage Locators
    login_btn = (By.XPATH, "//button[text()='Login']")
    signup_btn = (By.XPATH, "//button[contains(text(),'Sign up')]")

    # Homepage methods
    def click_login(self):
        self.click(self.login_btn)
    def click_signup(self):
        self.wait.until(
            EC.element_to_be_clickable(self.signup_btn)
        ).click()

    def is_login_visible(self):
        return self.is_visible(self.login_btn)

    def is_signup_visible(self):
        return self.is_visible(self.signup_btn)

    def is_menu_visible(self, text):
        return self.driver.find_element(
            By.XPATH,
            f"//*[contains(text(),'{text}')]"
        ).is_displayed()
        # return text in self.driver.page_source

    chat_widget = (
        By.XPATH,
        "//*[contains(@aria-label,'Chat Widget')]"
    )

    def chatbot_visible(self):
        return self.is_visible(self.chat_widget)

