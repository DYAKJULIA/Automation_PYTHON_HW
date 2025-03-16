from selenium.webdriver.common.by import By

class Product:

    def __init__(self, driver):
        self._driver = driver

# Добавление товаров в корзину: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie
    def product_selection(self):
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()


