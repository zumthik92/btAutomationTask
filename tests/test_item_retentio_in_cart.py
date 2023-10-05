import time
import unittest
from selenium.webdriver.common.by import By
from config import BASE_URL, USERNAME, PASSWORD
from selenium import webdriver
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class TestCartRetention(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        # self.cart_page = CartPage(self.driver)

    def test_cart_retention(self):
        self.login_page.login(USERNAME, PASSWORD)
        CartPage.verify_item_retention_in_cart(self)
        self.login_page.logout()
        time.sleep(5)
        self.login_page.login(USERNAME, PASSWORD)
        CartPage.check_the_products_retained(self)
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "button[data-test='remove-sauce-labs-backpack']"))