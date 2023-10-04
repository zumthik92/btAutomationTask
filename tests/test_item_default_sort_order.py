import pytest
import selenium
import unittest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from pages.login_page import Login
from pages.products_page import ItemSortOrder

class TestItemSortOrderValidation:
    """
    verifying the item sort order
    """
    baseURL = "https://www.saucedemo.com"
    def test_default_item_sort(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        Login.login_successful_and_land_on_homepage(self, username="standard_user", password='secret_sauce')
        ItemSortOrder.default_item_sort(self)
        print("it is sorted")
        self.assertTrue()

    def test_change_sort_order(self):
        """
        Verify user to able to change sort order
        """



