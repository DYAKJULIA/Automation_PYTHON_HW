from selenium import webdriver
from Pages.authorization import Authorization
from Pages.product import Product
from Pages.your_cart import YourCart
from Pages.overview import Overview

def test_03_shop():
    driver = webdriver.Chrome()

    # Создание экземпляра страницы
    authorization = Authorization(driver)

    # Авторизация
    authorization.user_name("standard_user")
    authorization.password("secret_sauce")
    # Нажать кнопку Login
    authorization.login()

    # Добавление товаров в корзину
    product = Product(driver)
    product.product_selection()

    # Переход в корзину
    your_cart = YourCart(driver)
    your_cart.go_to_cart()
    your_cart.checkout()

    # Оформление заказа
    overview = Overview(driver)
    overview.first_name("Юлия")
    overview.last_name("Дьякова")
    overview.postal_code("123112")
    overview.further()
    overview.total()

    driver.quit()