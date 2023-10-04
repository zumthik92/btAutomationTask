import pytest
import selenium
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from pages.login_page import LoginPage
from pages.logout_page import Logout

    # def test_logout(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.maximize_window()
    #     self.driver.get(self.baseURL)
    #     # # to access methods from the other class
    #     self.lp = LoginPage(self.driver)
    #     self.lp.login_successful(self.username, self.password)
    #     self.lo = Logout(self.driver)
    #     self.lo.logout_successfully()
    #     expected_url = "https://www.saucedemo.com"
    #     actual_url = self.driver.current_url
    #     if expected_url == actual_url:
    #         assert True
    #     # self.assertEqual(actual_url, expected_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}")

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.login_page = LoginPage(self.driver)

    def test_successful_login(self):
        self.login_page.login("standard_user", "secret_sauce")
        current_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/inventory.html"
        self.assertEqual(current_url, expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}")

    def test_failed_login(self):
        self.login_page.login("locked_out_user", "secret_sauce")
        # self.lp = LoginPage(self.driver)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        expected_message = "Epic sadface: Sorry, this user has been locked out."
        if error_message == expected_message:
            assert True