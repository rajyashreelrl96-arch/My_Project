from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_cart_icon_visibility(setup):

    LoginPage(setup).login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(setup)

    assert inventory.is_cart_icon_visible()


def test_random_selection(setup):

    LoginPage(setup).login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(setup)

    products = inventory.select_random_products()

    assert len(products) == 4

def test_sort_product_page(setup):
    LoginPage(setup).login( "standard_user", "secret_sauce" )
    inventory = InventoryPage(setup)
    inventory.sort_products("Name (Z to A)")
    assert True

def test_product_details(setup):
    LoginPage(setup).login( "standard_user", "secret_sauce" )
    inventory = InventoryPage(setup)
    products = inventory.select_random_products()
    inventory.click_cart_icon()
    items = setup.find_elements(By.XPATH, "//div[@class='cart_item']")
    assert len(items) == 4