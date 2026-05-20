from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    print("Starting Browser...")
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

def after_all(context):
    print("Closing Browser...")
    context.driver.quit()