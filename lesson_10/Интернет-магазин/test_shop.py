import allure
from selenium import webdriver
from Pages.authorization import Authorization
from Pages.product import Product
from Pages.your_cart import YourCart
from Pages.overview import Overview

@allure.title("Сквозной тест покупки товара")
@allure.description("Тест проверяет полный сценарий покупки товара: авторизация, добавление в корзину, заполнение информации и проверка итоговой суммы.")
@allure.feature("Покупка товара")
@allure.severity(allure.severity_level.CRITICAL)
def test_03_shop():
    driver = webdriver.Chrome()

    with allure.step("Создание экземпляра страницы"):
        authorization = Authorization(driver)

    with allure.step("Авторизация"):
        authorization.user_name("standard_user")
        authorization.password("secret_sauce")

    with allure.step("Нажать кнопку Login"):
        authorization.login()

    with allure.step("Добавление товаров в корзину"):
        product = Product(driver)
        product.product_selection()

    with allure.step("Переход в корзину"):
        your_cart = YourCart(driver)
        your_cart.go_to_cart()
        your_cart.checkout()

    with allure.step("Оформление заказа"):
        overview = Overview(driver)
        overview.first_name("Юлия")
        overview.last_name("Дьякова")
        overview.postal_code("123112")
        overview.further()
        overview.total()

    with allure.step("Закрытие браузера"):
        driver.quit()