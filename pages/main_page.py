import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    search = "//input[@class='search-form1__input']"
    submit_button = "//input[@class='search-form1__submit']"

    # Getters

    def get_search(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.search)))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.submit_button)))

    # Actions

    def input_search(self, search):
        self.get_search().send_keys(search)
        print("Input search")

    def click_submit_button(self):
        self.get_submit_button().click()
        print("Click submit button")

    # Methods

    def search_product(self):
        self.get_current_url()
        self.input_search("колготки")
        self.click_submit_button()
