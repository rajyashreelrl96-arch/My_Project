# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions as EC
#
# # class Guvi_Page:
# #     def __init__(self, driver):
# #         self.driver = driver
# #         self.wait = WebDriverWait(driver, 15)
#
#     # #homepage Locators
#     # login_btn = (By.XPATH, "//button[text()='Login']")
#     # signup_btn = (By.XPATH, "//button[contains(text(),'Sign up')]")
#
#     #loginpage Locators
#     # email_text = (By.ID, 'email')
#     # password_text = (By.ID, 'password')
#     # submit_login_btn = (By.XPATH, "//a[contains(text(),'Login')]")
#     # icon_click = (By.XPATH, "//img[@alt='Profile']")
#     # logout_btn = (By.XPATH, "//*[contains(text(),'Sign Out')]")
#
#     # #Homepage methods
#     # def click_login(self):
#     #     self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()
#     # def click_signup(self):
#     #     self.wait.until(EC.element_to_be_clickable(self.signup_btn)).click()
#     # def is_login_visible(self):
#     #     return self.wait.until(EC.presence_of_element_located(self.login_btn)).is_displayed()
#     # def is_signup_visible(self):
#     #     return self.wait.until(EC.visibility_of_element_located(self.signup_btn)).is_displayed()
#
#     #Loginpage methods
#     def enter_email(self, email):
#         self.wait.until(EC.visibility_of_element_located(self.email_text)).send_keys(email)
#     def enter_password(self, password):
#         self.wait.until(EC.visibility_of_element_located(self.password_text)).send_keys(password)
#     def click_login_btn(self):
#         self.wait.until(EC.element_to_be_clickable(self.submit_login_btn)).click()
#     def click_icon(self):
#         icon = self.wait.until(EC.presence_of_element_located(self.icon_click))
#         ActionChains(self.driver).move_to_element(icon).perform()
#         self.driver.execute_script("arguments[0].click();", icon)
#
#     def click_logout_btn(self):
#         logout = self.wait.until(EC.presence_of_element_located(self.logout_btn))
#         self.driver.execute_script("arguments[0].click();", logout)
#
#     def login(self,email,password):
#         self.enter_email(email)
#         self.enter_password(password)
#         self.click_login_btn()
