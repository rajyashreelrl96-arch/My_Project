# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from Guvi_login import Guvi_Page
#
# # @pytest.fixture
# # def setup():
# #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# #     driver.maximize_window()
# #     driver.implicitly_wait(10)
# #     driver.get("https://www.guvi.in")
# #     yield driver
# #     driver.quit()
#
# #Test Case 1
# def test_verify_navigate_url(setup):
#     assert "guvi.in" in setup.current_url
#
# #Test Case 2
# def test_verify_webpage_title(setup):
#     assert setup.title == "HCL GUVI | Learn to code in your native language"
#
# #Test Case 3
# def test_verify_login_button_is_displayed(setup):
#     page = Guvi_Page(setup)
#     assert page.is_login_visible()
#
# #Test Case 4
# def test_verify_signup_button_is_displayed(setup):
#     page = Guvi_Page(setup)
#     assert page.is_signup_visible()
#
# #Test Case 5
# def test_verify_sign_button_is_clickable(setup):
#     page = Guvi_Page(setup)
#     page.click_signup()
#     assert  "guvi.in" in setup.current_url
#
# #Test Case 6
# def test_verify_login_functionality(setup):
#     page = Guvi_Page(setup)
#     page.click_login()
#     page.login("rajyashreelrl96@gmail.com", "Marcheight0821")
#     assert "guvi.in" in setup.current_url
#
# #Test Case 7
# def test_verify_invalid_login_credentials(setup):
#     page = Guvi_Page(setup)
#     page.click_login()
#     page.login("invalidusername@xyz.com", "wrongpassword")
#     error_msg = WebDriverWait(setup, 10).until(
#         EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Incorrect Email or Password')]"))
#     )
#     assert "Incorrect Email or Password" in error_msg.text
#
# #Test Case 8
# def test_verify_menu(setup):
#     assert "LIVE Classes" in setup.page_source
#     assert "Courses" in setup.page_source
#     assert "Practice" in setup.page_source
#
# #Test Case 9
# def test_validate_dobby_guvi_assistant(setup):
#     wait = WebDriverWait(setup, 20)
#     chatbot = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@aria-label,'Chat Widget')]")))
#
#     assert chatbot.is_displayed()
#
#
# #Test Case 10
# def test_validate_logout_functionality(setup):
#     page = Guvi_Page(setup)
#     page.click_login()
#     page.login("rajyashreelrl96@gmail.com", "Marcheight0821")
#     page.click_icon()
#     page.click_logout_btn()
#     assert "login" in setup.page_source.lower()

