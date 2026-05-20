from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_checkout_order(setup):

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


