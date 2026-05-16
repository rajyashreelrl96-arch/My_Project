from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

class SaucedemoPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


#Loginpage locators
    username = (By.ID, "user-name")
    password = (By.XPATH, "//input[@type='password']")
    login_btn = (By.ID, "login-button")
    error_message = (By.TAG_NAME, "h3")

#Inventory page
    cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")
    products = (By.CLASS_NAME, "inventory_item")
    cart_count = (By.CLASS_NAME, "shopping_cart_badge")
    menu_btn = (By.ID, "react-burger-menu-btn")
    sort_dropdown = (By.XPATH, "//select[@class = 'product_sort_container']")
    reset_appstate_btn = (By.ID, "reset_sidebar_link")
    logout_btn = (By.ID, "logout_sidebar_link")

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

#inventory methods
    def is_cart_icon_visible(self):
       return self.driver.find_element(*self.cart_icon).is_displayed()
    def click_cart_icon(self):
       self.driver.find_element(*self.cart_icon).click()
    def get_cart_count(self):
       return self.driver.find_element(*self.cart_count).text

    def select_random_products(self, count=4):
      all_products = self.driver.find_elements(*self.products)
      selected = random.sample(all_products, count)
      selected_items = []

      for item in selected:
         name = item.find_element(By.CLASS_NAME, "inventory_item_name ").text
         price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
         item.find_element(By.TAG_NAME, "button").click()
         selected_items.append((name, price))

      return selected_items

    def sort_products(self, option_text):
        Select(
            self.driver.find_element(*self.sort_dropdown)
        ).select_by_visible_text(option_text)

    def reset_app_state(self):
        self.wait.until(EC.element_to_be_clickable(self.menu_btn)).click()
        self.wait.until(EC.element_to_be_clickable(self.reset_appstate_btn)).click()

    def logout(self):
        #click menu button
         self.wait.until(EC.element_to_be_clickable(self.menu_btn)).click()
         # #wait for sidebar to appear
         # self.wait.until(EC.visibility_of_element_located(self.logout_btn)).click()
        #click logout
         self.wait.until(EC.element_to_be_clickable(self.logout_btn)).click()

