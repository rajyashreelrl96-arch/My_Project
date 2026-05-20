from selenium.webdriver.common.by import By


class CartPage:

    cart_items = (By.CLASS_NAME, "cart_item")
    checkout_btn = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items_count(self):
        return len(
            self.driver.find_elements(*self.cart_items)
        )

    def click_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()