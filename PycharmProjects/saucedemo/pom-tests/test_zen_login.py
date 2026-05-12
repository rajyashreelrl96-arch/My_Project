import pytest
# from utilities.base_test import BaseTest
from login_page import LoginPage
from dashboard_page import DashboardPage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BaseTest:
    def setup_method(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def teardown_method(self):
        self.driver.quit()


class TestZenLogin(BaseTest):

    def test_successful_login_and_logout(self):
        login = LoginPage(self.driver, self.wait)
        dashboard = DashboardPage(self.driver, self.wait)
        login.open_url()
        login.enter_username("rajyashreelrl96@gmail.com")
        login.enter_password("Marcheight0821")
        login.click_login()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(dashboard.PROFILE_ICON))
        assert "dashboard" in self.driver.current_url
        dashboard.close_popup()
        dashboard.logout()
        assert dashboard.is_logged_out()

    def test_unsuccessful_login(self):
        login = LoginPage(self.driver, self.wait)

        login.open_url()
        login.enter_username("rajyashreelrl96@email.com")
        login.enter_password("wrongpass")
        login.click_login()

        assert login.is_invalid_email()
        assert login.is_invalid_password()

    def test_empty_username_password(self):
        login = LoginPage(self.driver, self.wait)

        login.open_url()
        login.click_login()

        assert login.is_invalid_email()
        assert login.is_invalid_password()

    def test_submit_button_enabled(self):
        login = LoginPage(self.driver, self.wait)

        login.open_url()
        assert self.driver.find_element(*login.LOGIN_BTN).is_enabled()