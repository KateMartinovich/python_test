import time

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.product_page import Product_page
from selenium import webdriver


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service('C:\\Users\\жми сюда\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)

    print("Start Test")

    login = Login_page(driver)
    login.authorization()
    mp = Main_page(driver)
    mp.search_product()
    pp = Product_page(driver)
    pp.choose_product()
    cp = Cart_page(driver)
    cp.product_confirmation()

