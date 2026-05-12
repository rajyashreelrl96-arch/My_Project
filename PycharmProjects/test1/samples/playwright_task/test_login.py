import pytest
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from login_page import LoginPage

class TestZenPortal:
    def test_successful_login(self, browser_page):
        login = LoginPage(browser_page)
        login.navigate()
        login.enter_username("rajyashreelrl96@gmail.com")
        login.enter_password("Marcheight0821")
        login.click_login()
        assert browser_page.url == "https://www.zenclass.in/dashboard"

    def test_unsuccessful_login(self, browser_page):
        login = LoginPage(browser_page)
        login.navigate()
        login.enter_username("invalidemail@gmail.com")
        login.enter_password("wrongpass123")
        login.click_login()
        assert browser_page.url == "https://www.zenclass.in/login"
        login.validate_invalid_password()


    def test_username_password(self, browser_page):
        login = LoginPage(browser_page)
        login.navigate()
        assert browser_page.is_visible("//input[@placeholder='Enter your mail']")
        assert browser_page.is_visible("//input[@type='password']")

    def test_submit_button(self, browser_page):
        login = LoginPage(browser_page)
        login.navigate()
        assert browser_page.is_visible("button[type='submit']")

    def test_logout(self, browser_page):
        login = LoginPage(browser_page)

        login.navigate()
        login.enter_username("rajyashreelrl96@gmail.com")
        login.enter_password("Marcheight0821")
        login.click_login()
        login.logout()

        assert login.page.url == "https://www.zenclass.in/login"

