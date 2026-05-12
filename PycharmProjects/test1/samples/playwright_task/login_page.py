from playwright.sync_api import Page, TimeoutError
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


from locators import LoginPageLocators


class LoginPage:

    def __init__(self, page:Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.zenclass.in/login")

    def enter_username(self, username):
        try:
            self.page.wait_for_selector(LoginPageLocators.username, timeout=5000)
            self.page.fill(LoginPageLocators.username, username)
        except TimeoutError:
            print("Username not found")

    def enter_password(self, password):
        try:
            self.page.wait_for_selector(LoginPageLocators.password, timeout=5000)
            self.page.fill(LoginPageLocators.password, password)
        except TimeoutError:
            print("Password not found")

    def click_login(self):
        try:
            self.page.wait_for_selector(LoginPageLocators.login_btn)
            self.page.click(LoginPageLocators.login_btn)
            self.page.wait_for_timeout(5000)
        except TimeoutError:
            print("Login Button not found")

    def validate_invalid_password(self):
        try:
            self.page.wait_for_selector(LoginPageLocators.invalid_password)
            self.page.wait_for_timeout(5000)
        except TimeoutError:
            print("Error message not found")

    # def click_logout(self):
    #     try:
    #         self.page.wait_for_selector(LoginPageLocators.logout_btn)
    #         self.page.click(LoginPageLocators.logout_btn)
    #     except TimeoutError:
    #         print("Logout Button not found")

    def logout(self):

        try:
            # Wait briefly to see if popup appears
            self.page.wait_for_selector(LoginPageLocators.close_popup, timeout=5000)
            self.page.click(LoginPageLocators.close_popup)
            print("Popup closed successfully.")
        except:
            print("Popup not found, continuing without closing.")


        try:
            # Click profile icon first
            self.page.wait_for_selector(LoginPageLocators.profile_btn, timeout=10000)
            self.page.click(LoginPageLocators.profile_btn)

            # Then click logout
            self.page.wait_for_selector(LoginPageLocators.logout_btn)
            self.page.click(LoginPageLocators.logout_btn)
            self.page.wait_for_timeout(3000)

        except TimeoutError:
            raise Exception("Logout button not found")