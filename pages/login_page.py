import time

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class LoginPage(BasePage):
    username_textbox = "input[placeholder = 'Username']"
    password_textbox = " // input[ @ placeholder = 'Password']"
    login_button = "input[data-test = 'login-button']"
    open_menu = "//button[@id='react-burger-menu-btn']"
    logout_link = "Logout"


    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, LoginPage.username_textbox).click()
        self.driver.find_element(By.CSS_SELECTOR, LoginPage.username_textbox).send_keys(username)
        self.driver.find_element(By.XPATH, LoginPage.password_textbox).click()
        self.driver.find_element(By.XPATH, LoginPage.password_textbox).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, LoginPage.login_button).click()

    def logout(self):
       wait = WebDriverWait(self.driver, 10)
       menu_button = wait.until(EC.presence_of_element_located((By.XPATH, LoginPage.open_menu)))
       menu_button.click()
       time.sleep(5)
       logout_option = self.driver.find_element(By.LINK_TEXT, LoginPage.logout_link)
       logout_option.click()
