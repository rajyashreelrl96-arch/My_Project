from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class orangehrmPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait= WebDriverWait(driver, 10)

#Login Locators
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[@type='submit']")
    error_msg = (By.XPATH, "//p[contains(@class,'alert-content-text')]")

#Dashboard Locators
    logout_icon = (By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
    logout_btn = (By.XPATH, "//a[contains(text(), 'Logout')]")
    admin_menu = (By.XPATH, "//span[text() = 'Admin']")
    PIM_menu = (By.XPATH, "//span[text() = 'PIM']")
    Leave_menu = (By.XPATH, "//span[text() = 'Leave']")
    Time_menu = (By.XPATH, "//span[text() = 'Time']")
    Recruitment_menu = (By.XPATH, "//span[text() = 'Recruitment']")
    My_info = (By.XPATH, "//span[text()='My Info']")
    Performance_menu = (By.XPATH, "//span[text() ='Performance']")
    Dashboard_menu = (By.XPATH, "//span[text() = 'Dashboard']")
#Login methods
    def login(self, user, pwd):
        self.wait.until(EC.visibility_of_element_located(self.username)).clear()
        self.driver.find_element(*self.username).send_keys(user)
        self.wait.until(EC.visibility_of_element_located(self.password)).clear()
        self.driver.find_element(*self.password).send_keys(pwd)
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()
        self.wait.until(lambda d:
                        "dashboard" in d.current_url.lower() or
                        self.is_error_visible()
                        )

    def is_error_visible(self):
        try:
            return self.driver.find_element(*self.error_msg).is_displayed()
        except:
            return False

    def get_error_msg(self):
       return self.wait.until(EC.visibility_of_element_located(self.error_msg)).text

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.logout_icon)).click()
        self.wait.until(EC.element_to_be_clickable(self.logout_btn)).click()

    def create_user(self, employee_name, username, password):

        # Admin menu
        self.wait.until(EC.element_to_be_clickable(self.admin_menu)).click()

        # Add button
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Add']")
        )).click()

        # User Role
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//label[text()='User Role']/following::div[contains(@class,'oxd-select-text')][1]")
        )).click()

        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@role='listbox']")
        ))

        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='option']//span[text()='ESS']")
        )).click()

        # Employee name (Autocomplete)
        emp = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Type for hints...']")
        ))
        emp.clear()
        emp.send_keys(employee_name)

        options = self.wait.until(EC.visibility_of_all_elements_located(
            (By.XPATH, "//div[@role='listbox']//span")
        ))

        for option in options:
            if employee_name in option.text:
                option.click()
                break

        # Status
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//label[text()='Status']/following::div[contains(@class,'oxd-select-text')][1]")
        )).click()

        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@role='listbox']")
        ))

        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='option']//span[text()='Enabled']")
        )).click()

        # Username
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//label[text()='Username']/following::input[1]")
        )).send_keys(username)

        # Password
        self.driver.find_element(
            By.XPATH, "//label[text()='Password']/following::input[1]"
        ).send_keys(password)

        # Confirm Password
        self.driver.find_element(
            By.XPATH, "//label[text()='Confirm Password']/following::input[1]"
        ).send_keys(password)

        # Save
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']")
        )).click()

    def search_user(self, username):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']"))).click()
        username_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Username']/following::input[1]")))
        username_field.clear()
        username_field.send_keys(username)
        #search user
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        #result table
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='table']")))

    def user_found(self, username):
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, f"//div[@role='row']//div[contains(text(),'{username}')]")
            ))
            return True
        except:
            return False

    def forgot_password(self, username):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Forgot your password? ']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))).send_keys(username)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
    def get_success_msg(self):
        success_msg = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Reset Password link sent successfully')]")))
        return success_msg.text

    def open_my_info(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='My Info']"))).click()

    def sub_menu_visible(self, name):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[contains(text(),'{name}')]")
            )
        ).is_displayed()

    def menu_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()


    def assign_leave(self, emp_name):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Leave']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "a[text()='Assign Leave']"))).click()
        # Employee name
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']"))).send_keys(emp_name)
        # Select employee from dropdown
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@role='listbox']//span")
            )
        ).click()
        # leave type
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(text(),'CAN - Matternity')])"))).click()
        # from date
        from_date = self.driver.find_element(
            By.XPATH,
            "(//input[@placeholder='yyyy-dd-mm'])[1]")
        from_date.send_keys(Keys.CONTROL + "a")
        from_date.send_keys("2026-30-04")
        # To date
        to_date = self.driver.find_element(
            By.XPATH,
            "(//input[@placeholder='yyyy-dd-mm'])[2]")
        to_date.send_keys(Keys.CONTROL + "a")
        to_date.send_keys("2026-30-04")
        # Assign Leave
        self.wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//button[normalize-space()='Assign']"))).click()
        # Confirmation pop
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Ok']"))).click()

    def claim_menu(self, employee_name):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Claim']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Assign Claim']"))).click()
        # Employee name
        emp = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
        emp.send_keys(employee_name)
        # Select employee suggestion
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@role='option']")
            )
        ).click()
        # Event
        self.driver.find_element(By.XPATH, "(//div[contains(@class,'oxd-select-text')])[1]").click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Accommodation']"))).click()
        # Currency
        self.driver.find_element(By.XPATH, "(//div[contains(@class,'oxd-select-text')])[2]").click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Indian')]"))).click()
        # create
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create']"))).click()
        # validation
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Success')]")))