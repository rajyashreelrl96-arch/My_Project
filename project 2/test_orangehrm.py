import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from orangehrm_page import orangehrmPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com")
    yield driver
    driver.quit()

#Testcase 1  login functionality using multiple sets of credentials
@pytest.mark.parametrize("user,pwd", [
    ("Admin", "admin123"),
    ("wrongadmin", "wrongpass123")
])
def test_multiple_credentials(setup, user, pwd):
    page = orangehrmPage(setup)
    page.login(user, pwd)

    if pwd == "admin123":
        assert page.menu_visible(page.Dashboard_menu)
        page.logout()
    else:
        assert "Invalid credentials" in page.get_error_msg()

#Testcase 2  Home URL is accessible
def test_url_accessible(setup):
    assert "https://opensource-demo.orangehrmlive.com/" in setup.current_url

#Testcase 3 Validate presence of login fields
def test_login_fields_visible(setup):
    page = orangehrmPage(setup)
    assert page.wait.until(EC.visibility_of_element_located(page.username)).is_displayed()
    assert page.wait.until(EC.visibility_of_element_located(page.password)).is_displayed()

#Testcase 4 visibility and clickability of main menu items  after login
def test_menu_visibility(setup):
    page = orangehrmPage(setup)
    page.login("admin", "admin123")

    assert page.menu_visible(page.admin_menu)
    assert page.menu_visible(page.PIM_menu)
    assert page.menu_visible(page.Leave_menu)
    assert page.menu_visible(page.Time_menu)
    assert page.menu_visible(page.Recruitment_menu)
    assert page.menu_visible(page.My_info)
    assert page.menu_visible(page.Performance_menu)
    assert page.menu_visible(page.Dashboard_menu)

#Testcase 5 Create a new user and validate login
def test_create_user(setup):
    page = orangehrmPage(setup)
    page.login("Admin", "admin123")
    page.create_user("Jitesh Sharma", "Rajya123",  "rajya@123")
    assert "admin" in setup.current_url.lower()



#Testcase 6  newly created user in the admin user list
def test_created_user(setup):
    page = orangehrmPage(setup)
    page.login("Admin", "admin123")
    username = "Rajya123"
    page.create_user(
        "Jitesh Sharma",
        "Rajya123", "rajya@123")
    page.search_user(username)
    assert page.user_found(username), "No Records found!"


#Testcase 7 Forgot password
def test_forgot_password(setup):
    page =  orangehrmPage(setup)
    page.forgot_password("Admin")
    assert "Reset Password link sent successfully" in page.get_success_msg()
# def forgot_password(self, username):
#     self.driver.find_element(By.XPATH, "//p[text()='Forgot your password? ']").click()
#     self.wait.until(EC.visibility_of_element_located(By.NAME, 'username')).send_keys(username)
#     self.driver.find_element(By.XPATH, "//button[@type='submit']" ).click()

#Testcase 8 open My_info
def test_open_myinfo(setup):
    page = orangehrmPage(setup)
    page.login("Admin", "admin123")
    page.open_my_info()
    assert page.sub_menu_visible("Personal Details")
    assert page.sub_menu_visible("Contact Details")
    assert page.sub_menu_visible("Emergency Contacts")
    assert page.sub_menu_visible("Dependents")
    assert page.sub_menu_visible("Immigration")
    assert page.sub_menu_visible("Job")
    assert page.sub_menu_visible("Salary")
    assert page.sub_menu_visible("Report-to")
    assert page.sub_menu_visible("Qualifications")
    assert page.sub_menu_visible("Memberships")


#Testcase 9 Assign Leave
def test_assign_leave(setup):
    page = orangehrmPage(setup)
    page.login("Admin", "admin123")
    page.assign_leave("Jitesh Sharma")
    assert "assignLeave" in setup.current_url
    print("Leave assigned successfully")

#Testcase 10
def test_claim_menu(setup):
    page = orangehrmPage(setup)
    page.login("Admin", "admin123")
    page.claim_menu("Jitesh Sharma")
    success_msg = page.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Success')]")))
    assert success_msg.is_displayed()
