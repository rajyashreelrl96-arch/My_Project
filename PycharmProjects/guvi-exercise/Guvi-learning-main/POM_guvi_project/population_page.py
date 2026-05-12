from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PopulationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        # self.population_count = "//*[@data-target='current_population']"
        self.population_count = "//h1[contains(text(),'World population')]/preceding-sibling::*[1]/text()"


    def open_page(self, url):
        self.driver.get(url)

    def get_population(self):
        self.population_count = "//h1[contains(text(),'World population')]/preceding-sibling::*[1]"
        population_element = self.driver.find_element(By.XPATH, self.population_count)
        population = population_element.text
        return population