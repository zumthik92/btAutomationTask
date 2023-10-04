from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class LoginPage(BasePage):
    username_textbox = "input[placeholder = 'Username']"
    password_textbox = " // input[ @ placeholder = 'Password']"
    login_button = "input[data-test = 'login-button']"
    logout_button = "//nav[@class='bm-item-list']//a[@id='logout_sidebar_link']"


    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, LoginPage.username_textbox).click()
        self.driver.find_element(By.CSS_SELECTOR, LoginPage.username_textbox).send_keys(username)
        self.driver.find_element(By.XPATH, LoginPage.password_textbox).click()
        self.driver.find_element(By.XPATH, LoginPage.password_textbox).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, LoginPage.login_button).click()

    # def login_unsuccessful(self, username, password):








