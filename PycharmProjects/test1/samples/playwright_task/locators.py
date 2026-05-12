class LoginPageLocators:
    # username = "//input[@placeholder='Enter your mail']"
    username = "//label[.='Email']/following-sibling::div/input"
    password = "//input[@type='password']"
    login_btn = "//button[@type='submit']"
    logout_btn = "//div[.='Log out']"
    close_popup = "//button[@class='custom-close-button']"
    profile_btn = "//img[@id='profile-click-icon']"
    invalid_password = "//*[.'Invalid password!']"