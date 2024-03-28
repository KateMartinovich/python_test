import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    promo_button_no = "//p[@class='cart-promo-button-n']"

    # Getters

    def get_promo_button_no(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.promo_button_no)))

    # Actions

    def click_promo_button_no(self):
        self.get_promo_button_no().click()
        print("Click promo button no")

    # INFO Cart Product

    def product_info(self):
        # Product price
        value_price_product = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[7]/div/noindex/div[1]/div[2]/div[1]/div[1]/ul[2]/li/div/div[2]/div[1]/div/div/p")
        value_price_text = value_price_product.text
        print(f"Price of the product: {value_price_text}")

        # Cart product price
        price_cart_product = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[7]/div/noindex/div[1]/div[2]/div[1]/div[1]/ul[2]/li/div/div[2]/div[4]/div/div/p")
        value_cart_price_product = price_cart_product.text
        print(f"Price of the product in the cart: {value_cart_price_product}")

        if value_price_text == value_cart_price_product:
            print("WARNING: The product's price matches the price in the cart.")
        else:
            print("INFO: The product's price does not match the price in the cart.")

    # Methods

    def product_confirmation(self):
        self.click_promo_button_no()
        self.get_current_url()
        self.assert_url('https://conteshop.by/ru/checkout/cart')
        self.get_screenshot()
        self.product_info()
