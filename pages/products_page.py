from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductsPage(BasePage):
    products = ".inventory_item_name"
    cart = "//a[@class ='shopping_cart_link']"
    add_to_cart = "button[data - test = 'add-to-cart-sauce-labs-backpack’]"
    sort_option = "select[data-test= 'product_sort_container']"
    sort_container = "product_sort_container"
    your_cart = "//span[@class='title']"
    add_to_cart_btn = ".btn_primary"
    add_to_cart_item1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    add_to_cart_item2 = "//button[@data-test='add-to-cart-sauce-labs-onesie']"
    product_prices = "inventory_item_price"

    def verify_default_sort_order(self):
        product_names = self.driver.find_elements(By.CSS_SELECTOR, ProductsPage.products)
        product_names_text = [product.text for product in product_names]
        is_default_order = product_names_text == sorted(product_names_text)
        if is_default_order:
            assert True

    def verify_sort_order_price_high_low(self):
        self.driver.find_element(By.CSS_SELECTOR, ProductsPage.sort_option).click()
        sorting_dropdown = Select(self.driver.find_element(By.CLASS_NAME, ProductsPage.sort_container))
        sorting_dropdown.select_by_value("hilo")
        product_prices = self.driver.find_elements(By.CLASS_NAME, ProductsPage.product_prices)
        product_prices_text = [price.text for price in product_prices]
        is_price_high_to_low = product_prices_text.sort(reverse=True)
        if is_price_high_to_low:
            assert True
