from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    USERNAME = (By.XPATH, "//div[@class='email-input']/div/div/input")
    PASSWORD = (By.XPATH, "//div[@class='password-input']/div/div/input")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    ERROR_MSG = (By.XPATH, "//div[contains(text(),'Invalid')]")
    INVALID_EMAIL = (By.XPATH, "//p[text()='*Incorrect email!']")
    INVALID_PASSWORD = (By.XPATH, "//p[text()='Email and password required!']")

    def open_url(self):
        self.driver.get("https://v2.zenclass.in/login")

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)).click()

    def is_login_failed(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.INVALID_EMAIL)).is_displayed()
        except TimeoutException:
            return False

    def is_invalid_email(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.INVALID_EMAIL)).is_displayed()
        except TimeoutException:
            return False

    def is_invalid_password(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.INVALID_PASSWORD)).is_displayed()
        except TimeoutException:
            return False