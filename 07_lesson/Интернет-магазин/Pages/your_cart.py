from selenium.webdriver.common.by import By

class YourCart:

    def __init__(self, driver):
        self._driver = driver

    # Переход в корзину
    def go_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    # Нажмите Checkout
    def checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()