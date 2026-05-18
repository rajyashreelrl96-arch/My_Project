from Guvi_project.pages.home_page import HomePage
from Guvi_project.pages.login_page import LoginPage
from utils.config import VALID_EMAIL, VALID_PASSWORD

def test_valid_login(setup):
    print("EMAIL:", VALID_EMAIL)
    print("PASSWORD:", VALID_PASSWORD)

    HomePage(setup).click_login()
    login = LoginPage(setup)
    login.login(VALID_EMAIL, VALID_PASSWORD)
    login.wait_for_succesfull_login()
    assert "guvi.in" in setup.current_url

def test_invalid_login(setup):
    HomePage(setup).click_login()
    login = LoginPage(setup)
    login.login(
        "invalid@gmail.com",
        "wrong123"
    )

    assert "Incorrect Email or Password" \
           in login.get_invalid_message()

def test_logout(setup):
    HomePage(setup).click_login()
    login = LoginPage(setup)
    login.login(VALID_EMAIL, VALID_PASSWORD)
    login.wait_for_succesfull_login()
    login.logout()
    assert "login" \
           in setup.page_source.lower()

