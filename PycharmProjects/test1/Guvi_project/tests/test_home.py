from Guvi_project.pages.home_page import HomePage

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
    assert  "guvi.in" in setup.current_url

def test_menu(setup):

    home = HomePage(setup)

    assert home.is_menu_visible(
        "LIVE Classes"
    )

    assert home.is_menu_visible(
        "Courses"
    )

def test_dobby_assistant(setup):

    home = HomePage(setup)

    assert home.chatbot_visible()

