from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Logout:
    open_menu = "//button[@id='react-burger-menu-btn']"
    logout_link = "logout_sidebar_link"

    def logout_successfully(self):
        wait = WebDriverWait(self.driver, 10)
        menu_button = wait.until(EC.presence_of_element_located((By.XPATH, self.open_menu)))
        menu_button.click()
        # Locate the logout option and click it
        logout_option = self.driver.find_element(By.ID, self.logout_link)
        logout_option.click()


