from selenium.webdriver.common.by import By
import time

class LoginPage:
    username = (By.ID, "user-name")
    password = (By.XPATH, "//input[@type='password']")
    login_btn = (By.ID, "login-button")
    error_message = (By.TAG_NAME, "h3")

    def __init__(self, driver):
        self.driver = driver
#login methods
    def login(self, user, pwd):
       self.driver.find_element(*self.username).clear()
       self.driver.find_element(*self.username).send_keys(user)

       self.driver.find_element(*self.password).clear()
       self.driver.find_element(*self.password).send_keys(pwd)

       self.driver.find_element(*self.login_btn).click()
       time.sleep(5)

    def get_error_message(self):
       return self.driver.find_element(*self.error_message).text


