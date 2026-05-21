import pytest
import allure

from pages.login_page import LoginPage


@allure.feature("Login")
@pytest.mark.parametrize(
    "user",
    [
        "standard_user",
        "problem_user",
        "performance_glitch_user"
    ]
)
def test_login_with_multiple_users(setup, user):

    login_page = LoginPage(setup)

    login_page.login(user, "secret_sauce")

    assert "inventory.html" in setup.current_url


@allure.feature("Login")
def test_invalid_login(setup):

    login_page = LoginPage(setup)

    login_page.login("wrong_user", "wrong_pass")

    assert "Epic sadface" in login_page.get_error_message()