import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):
    url = 'https://conteshop.by/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    user_name = "//input[@id='youama-email-login']"
    password = "//input[@id='youama-password-login']"
    enter_button = "//a[@href='https://conteshop.by/ru/customer/account/login/']"
    email_button = "//*[@id='y-to-email']/span"
    login_button = "//button[@class='conte-button conte-button--login']"
    main_word = "//ul[@class='menu_level_1 break-word list-reset']/li[contains(@class, 'item_1') or span/span[contains(text(), 'Моя учётная запись')]]"
    wishlist_button = "//a[@href='https://conteshop.by/ru/wishlist/']"

    # Getters

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_email_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_wishlist_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.wishlist_button)))

    # Actions

    def click_enter_button(self):
        self.get_enter_button().click()
        print("Click enter button")

    def click_email_button(self):
        self.get_email_button().click()
        print("Click email button")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('Input user name')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    def click_wishlist_button(self):
        self.get_wishlist_button().click()
        print("Click wishlist button")

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_enter_button()
        self.click_email_button()
        self.input_user_name("autot@internet.ru")
        self.input_password("13579abcdefg")
        self.click_login_button()
        self.click_wishlist_button()
        self.assert_word(self.get_main_word(), 'МОЯ УЧЁТНАЯ ЗАПИСЬ')
