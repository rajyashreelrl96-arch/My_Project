from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random

class InventoryPage:

#Inventory page
    cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")
    products = (By.CLASS_NAME, "inventory_item")
    cart_count = (By.CLASS_NAME, "shopping_cart_badge")
    menu_btn = (By.ID, "react-burger-menu-btn")
    sort_dropdown = (By.XPATH, "//select[@class = 'product_sort_container']")
    reset_appstate_btn = (By.ID, "reset_sidebar_link")
    logout_btn = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver

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
