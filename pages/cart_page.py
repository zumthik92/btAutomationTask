from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.products_page import ProductsPage

class CartPage(BasePage):
    cart = "//a[@class='shopping_cart_link']"
    checkout_button = "button[data-test='checkout']"
    form_first_name = "//input[@data-test='firstName']"
    form_last_name = "//input[@data-test='lastName']"
    zip_postal_code = "//input[@data-test='postalCode']"
    continue_button = "//input[@data-test='continue']"

    def verify_item_retention_in_cart(self):
        # add item to cart
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, ProductsPage.add_to_cart_item1).click()
        self.driver.find_element(By.XPATH, ProductsPage.add_to_cart_item2).click()
        self.driver.find_element(By.XPATH, CartPage.cart).click()




    def verify_input_field_for_form_fields():
        pass




