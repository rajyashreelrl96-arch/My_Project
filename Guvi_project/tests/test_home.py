from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Test Case 1
def test_verify_navigate_url(setup):
    assert "guvi.in" in setup.current_url

#Test Case 2
def test_verify_webpage_title(setup):
    assert setup.title == "HCL GUVI | Learn to code in your native language"

#Test Case 3
def test_verify_login_button_is_displayed(setup):
    home = HomePage(setup)
    assert home.is_login_visible()


#Test Case 4
def test_verify_signup_button_is_displayed(setup):
    home = HomePage(setup)
    assert home.is_signup_visible()

#Test Case 5
def test_verify_sign_button_is_clickable(setup):
        home = HomePage(setup)

        home.click_signup()

        WebDriverWait(setup, 10).until(
            EC.url_contains("register")
        )
    # home = HomePage(setup)
    # home.click_signup()
    # WebDriverWait(setup, 10).until(
    #     lambda d: "signup" in d.current_url.lower()
    # )
    #
    # assert "signup" in setup.current_url.lower()
    # assert  "guvi.in" in setup.current_url

#Test Case 6
def test_menu(setup):

    home = HomePage(setup)

    assert home.is_menu_visible(
        "LIVE Classes"
    )

    assert home.is_menu_visible(
        "Courses"
    )

#Test Case 7
def test_dobby_assistant(setup):

    home = HomePage(setup)

    assert home.chatbot_visible()

