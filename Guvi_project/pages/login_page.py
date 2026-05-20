from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage

class LoginPage(BasePage):
    email_text = (By.ID, 'email')
    password_text = (By.ID, 'password')

    submit_login_btn = (By.XPATH, "//a[contains(text(),'Login')]")
    icon_click = (By.XPATH, "//img[contains(@alt,'Profile')]")
    logout_btn = (By.XPATH, "//*[contains(text(),'Sign Out')]")

    invalid_msg = (By.XPATH,"//div[contains(text(),'Incorrect Email or Password')]")

    def login(self, email, password):
        self.enter_text(self.email_text, email)
        self.enter_text(self.password_text, password)
        self.click(self.submit_login_btn)

    def wait_for_succesfull_login(self):
            self.wait.until(
                EC.visibility_of_element_located(
                    self.icon_click
                )
            )

    def get_invalid_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.invalid_msg
            )
        ).text

    def logout(self):
        icon = self.wait.until(
            EC.element_to_be_clickable(
                self.icon_click
            )
        )

        ActionChains(
            self.driver
        ).move_to_element(icon).perform()

        icon.click()

        self.wait.until(
            EC.element_to_be_clickable(
                self.logout_btn
            )
        ).click()

