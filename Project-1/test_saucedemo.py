import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from saucedemo import SaucedemoPage

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()

    # 🔥 Disable password manager + save prompts
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)

    # 🔥 Disable browser UI interruptions
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-save-password-bubble")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()

#Testcase 1    Login with multiple users
@allure.feature("Login")
@allure.story("Valid Login")
@pytest.mark.parametrize(
    "user",
    ["standard_user", "problem_user",  "performance_glitch_user"] #insted of we use seperate methods like def test_login_standarad, def test_login_problem, def test_login_performance.
)
def test_login_with_multiple_users(setup, user):
    page = SaucedemoPage(setup)
    page.login(user, "secret_sauce")
    allure.attach(
        setup.get_screenshot_as_png(),
        name = "Login success",
        attachment_type = allure.attachment_type.PNG
    )
    assert "inventory.html" in setup.current_url

#Testcase 2 Login with invalid Credentials
@allure.feature("Login")
@allure.story("Invalid Login")
def test_login_with_invalid_credentials(setup):
     page = SaucedemoPage(setup)
     page.login("wrong_user", "wrong_pass")
     allure.attach(
         setup.get_screenshot_as_png(),
         name = "Invalid Login",
         attachment_type = allure.attachment_type.PNG
     )
     assert "Epic sadface" in page.get_error_message()

#Testcase 3 Validate Logout
@allure.feature("Logout")
def test_validate_logout(setup):
    page = SaucedemoPage(setup)
    page.login("standard_user", "secret_sauce")
    allure.attach(
        setup.get_screenshot_as_png(),
        name = "Logout success",
        attachment_type =  allure.attachment_type.PNG
    )

    page.logout()
    assert "saucedemo" in setup.current_url

#Testcase 4
def test_cart_icon_visibility(setup):
    page = SaucedemoPage(setup)
    page.login("standard_user", "secret_sauce")
    assert page.is_cart_icon_visible()

#Testcase 5
def test_random_selection(setup):
    page = SaucedemoPage(setup)
    page.login("standard_user", "secret_sauce")
    products = page.select_random_products()
    print(products)
    assert len(products) == 4

#Testcase 6
def test_product_selection_in_cart(setup):
    page = SaucedemoPage(setup)
    page.login("standard_user", "secret_sauce")
    page.select_random_products()
    assert page.get_cart_count() == "4"

#Testcase 7
def test_product_details(setup):
    page = SaucedemoPage(setup)
    page.login("standard_user", "secret_sauce")
    page.select_random_products()
    page.click_cart_icon()
    items = setup.find_elements(By.XPATH,"//div[@class='cart_item']")
    assert len(items) == 4

#Testcase 8
def test_checkout_order(setup):
    page = SaucedemoPage(setup)
    page.login("standard_user", "secret_sauce")
    page.select_random_products()
    page.click_cart_icon()
    #checkout
    setup.find_element(By.ID, "checkout").click()
    #fill details
    setup.find_element(By.ID, "first-name").send_keys("rajya")
    setup.find_element(By.ID, "last-name").send_keys("L")
    setup.find_element(By.ID, "postal-code").send_keys("600044")
    setup.find_element(By.ID, "continue").click()
    #finish order
    setup.find_element(By.ID, "finish").click()
    setup.save_screenshot("order summary.png")
    assert "Thank you for your order!" in setup.page_source

#Testcase 9
def test_sort_product_page(setup):
    page = SaucedemoPage(setup)
    page.login("standard_user", "secret_sauce")
    page.sort_products("Name (Z to A)")
    assert True

#Testcase 10
def test_reset_app_functionality(setup):
    page = SaucedemoPage(setup)
    page.login("standard_user", "secret_sauce")
    page.select_random_products()
    page.click_cart_icon()
    page.reset_app_state()
    assert "shopping_cart_badge" not in setup.page_source



