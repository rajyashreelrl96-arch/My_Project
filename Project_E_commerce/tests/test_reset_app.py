from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.menu_page import MenuPage


def test_reset_app_functionality(setup):

    # Login
    LoginPage(setup).login(
        "standard_user",
        "secret_sauce"
    )

    # Add products
    inventory = InventoryPage(setup)

    inventory.select_random_products()

    # Reset app state
    menu = MenuPage(setup)

    menu.reset_app_state()

    # Validate cart badge removed
    assert "shopping_cart_badge" not in setup.page_source

def test_logout_btn(setup):
    LoginPage(setup).login(
        "standard_user", "secret_sauce"
    )
    menu = MenuPage(setup)
    menu.logout()
    assert "saucedemo" in setup.current_url