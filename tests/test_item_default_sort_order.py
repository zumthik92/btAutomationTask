
import unittest
from selenium import webdriver
from config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

class TestItemSortOrderValidation:
    """
    verifying the item sort order
    """
    def test_default_item_sort(self):
        """
        Verify the default sort order
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        self.login_page.login(USERNAME, PASSWORD)
        # LoginPage.login(self, username="standard_user", password='secret_sauce')
        ProductsPage.default_item_sort(self)
        print("it is sorted")
        self.assertTrue()

    def test_change_sort_order(self):
        """
        Verify user to able to change sort order
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        LoginPage.login(self, username="standard_user", password='secret_sauce')




