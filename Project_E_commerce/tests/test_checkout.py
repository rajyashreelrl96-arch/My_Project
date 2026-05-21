from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_order(setup):
    print(setup.current_url)

    LoginPage(setup).login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(setup)

    inventory.select_random_products()

    inventory.click_cart_icon()

    cart = CartPage(setup)

    cart.click_checkout()

    checkout = CheckoutPage(setup)

    checkout.enter_checkout_details(
        "rajya",
        "L",
        "600044"
    )

    checkout.continue_checkout()

    checkout.finish_order()

    assert "Thank you for your order!" in \
           checkout.get_success_message()


