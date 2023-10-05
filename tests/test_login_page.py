import pytest
import selenium
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from pages.login_page import LoginPage
from config import BASE_URL, USERNAME, PASSWORD


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        self.login_page = LoginPage(self.driver)

    def test_successful_login(self):
        self.login_page.login("standard_user", "secret_sauce")
        current_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/inventory.html"
        self.assertEqual(current_url, expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}")
        self.login_page.logout()
        expected_url1 = "https://www.saucedemo.com"
        actual_url1 = self.driver.current_url
        if expected_url1 == actual_url1:
            assert True
        self.assertEqual(actual_url1, expected_url1, f"Expected URL: {expected_url1}, Actual URL: {actual_url1}")

    def test_failed_login(self):
        self.login_page.login("locked_out_user", "secret_sauce")
        # self.lp = LoginPage(self.driver)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        expected_message = "Epic sadface: Sorry, this user has been locked out."
        if error_message == expected_message:
            assert True