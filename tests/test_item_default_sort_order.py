
import unittest
from selenium import webdriver
from config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class TestItemSortOrderValidation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        self.login_page = LoginPage(self.driver)
    def test_default_item_sort(self):
        """
        Verify the default sort order
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        self.login_page.login(USERNAME, PASSWORD)
        ProductsPage.verify_default_sort_order(self)

    def test_change_sort_order(self):
        """
        Verify user to able to change sort order
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        LoginPage.login(self, USERNAME, PASSWORD)
        ProductsPage.verify_sort_order_price_high_low(self)