from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:

    def __init__(self, driver):
        self.driver = driver

        self._username_loc = (By.NAME, "email")
        self._password_loc = (By.NAME, "password")
        self._login_loc = (By.XPATH, "//button[@type='submit']")
        self._logout_loc = (By.XPATH, "//*[contains(text(),'Log out')]")
        self._error_loc = (By.XPATH, "//*[contains(text(),'Invalid') or contains(text(),'incorrect')]")

    def enter_username(self, username):
        self.driver.find_element(*self._username_loc).clear()
        self.driver.find_element(*self._username_loc).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self._password_loc).clear()
        self.driver.find_element(*self._password_loc).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self._login_loc).click()

    def error_message(self):
        return self.driver.find_element(*self._error_loc).text

    def is_login_button_enabled(self):
        return self.driver.find_element(*self._login_loc).is_enabled()

    def is_logged_in(self):
        return "dashboard" in self.driver.current_url.lower() or "zenclass" in self.driver.current_url.lower()

    def click_logout(self):
        self.driver.find_element(*self._logout_loc).click()

    def is_logged_out(self):
        return "login" in self.driver.current_url.lower()

    # from selenium.webdriver.common.by import By
    # class Login:
    #     def __init__(self,driver):
    #         self._username_loc = "//input[@id=':r2:']"
    #         self._password_loc = "//input[@id=':r2:']"
    #         self._login_loc = "//button[@type='submit']"
    #         self._logout_loc = "//div[contains(text(), 'Log out')]"
    #         self.driver = driver
    #
    #     def navigate_url(self,url):
    #         try:
    #            self.driver.get(url)
    #            return True
    #         except:
    #             raise Exception("error in navigating to login page")
    #
    #     def enter_username(self,username):
    #         self.driver.find_element(*self._username_loc).send_keys(username)
    #
    #     def enter_password(self,password):
    #         self.driver.find_element(*self._password_loc).send_keys(password)
    #
    #     def click_login(self):
    #         self.driver.find_element(*self._login_loc).click()
    #
    #     def get_error_message(self):
    #         return self.driver.find_element(self.ERROR_MSG).text
    #
    #     def click_logout(self):
    #         self.driver.find_element(*self._logout_loc).click()
