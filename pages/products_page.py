from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductsPage(BasePage):
    products = ".inventory_item_name"
    cart = "//a[@class ='shopping_cart_link']"
    add_to_cart = "button[data - test = 'add-to-cart-sauce-labs-backpack’]"
    sort_option = "select[data-test= 'product_sort_container']"
    your_cart = "//span[@class='title']"
    add_to_cart_item1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    add_to_cart_item2 = "//button[@data-test='add-to-cart-sauce-labs-onesie']"

    def verify_default_sort_order(self):
        product_names = self.driver.find_elements(By.CSS_SELECTOR, ProductsPage.products)
        product_names_text = [product.text for product in product_names]
        product_names_text == sorted(product_names_text)

    def verify_sort_order_price_high_low(self):
        self.driver.find_elements(By.CSS_SELECTOR, ProductsPage.sort_option).click()
        sorting_dropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        sorting_dropdown.select_by_value("hilo")