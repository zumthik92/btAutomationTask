from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class CartPage(BasePage):
    cart = "//a[@class='shopping_cart_link']"
    add_to_cart_item1 = "button[data-test='add-to-cart-sauce-labs-backpack’]"
    add_to_cart_item2 = "//button[@data-test='add-to-cart-sauce-labs-onesie']"
    checkout_button = "button[data-test='checkout']"
    form_first_name ="//input[@data-test='firstName']"
    form_last_name = "//input[@data-test='lastName']"
    zip_postal_code = "//input[@data-test='postalCode']"
    continue_button = "//input[@data-test='continue']"



    def verify_input_field_for_form_fields():
        pass




