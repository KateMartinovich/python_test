import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    colour_filter_button = "//button[@class='category_filter_button' and text()='Цвет']"
    black_colour = "//div[@class='dropdown__content show']//span[contains(concat(' ', @class, ' '), ' filter-label ') and contains(concat(' ', @class, ' '), ' check2__label ') ]"
    choose_product_1 = "//a[@href='https://conteshop.by/ru/conte/kolgotki-jenskie-kolgotki-c-diagonalnymi-nadpisyami-sentiment-nero']"
    product_size_4 = "//div[@id='size_86541']"
    product_count_plus = "//a[@id='btn-qty-plus']"
    product_count_minus = "//a[@id='btn-qty-minus']"
    add_to_cart_button = "//div[@class='fixed-button']//span[contains(@class, 'add-to-cart1') and contains(@class, 'button') and contains(@class, 'btn-cart')]"
    checkout_button = "//span[@class='conte-button']"

    # Getters

    def get_colour_filter_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.colour_filter_button)))

    def get_black_colour(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.black_colour)))

    def get_choose_product_1(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.choose_product_1)))

    def get_product_size_4(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_size_4)))

    def get_product_count_plus(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_count_plus)))

    def get_product_count_minus(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_count_minus)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # Actions

    def click_colour_filter_button(self):
        self.get_colour_filter_button().click()
        print("Click colour filter button")

    def click_black_colour(self):
        self.get_black_colour().click()
        print("Click black colour checkbox")

    def click_choose_product_1(self):
        self.get_choose_product_1().click()
        print("Click choose product_1")

    def click_product_size_4(self):
        self.get_product_size_4().click()
        print("Click product size 4")

    def click_product_count_plus(self):
        self.get_product_count_plus().click()
        print("Click product count plus")

    def click_product_count_minus(self):
        self.get_product_count_minus().click()
        print("Click product count minus")

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Click add to cart button")

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")

    # Methods

    def choose_product(self):
        self.get_current_url()
        self.click_colour_filter_button()
        self.click_black_colour()
        self.click_choose_product_1()
        self.click_product_size_4()
        self.click_product_count_plus()
        self.click_product_count_minus()
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.click_add_to_cart_button()
        self.click_checkout_button()
