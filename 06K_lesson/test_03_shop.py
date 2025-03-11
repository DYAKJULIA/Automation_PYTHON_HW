import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем WebDriver
@pytest.fixture()
def driver():
    # Указываем путь к драйверу
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_01_form(driver):
    # Откройте страницу
    driver.get("https://www.saucedemo.com/")

    # Ожидаем загрузку страницы
    driver.implicitly_wait(2)

    # Авторизуйтесь как пользователь standard_user
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")

    # Нажать кнопку Login
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    # Добавьте в корзину товары: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    # Перейдите в корзину
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    # Нажмите Checkout
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    # Заполните форму своими данными: имя, фамилия, почтовый индекс
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Юлия")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Дьякова")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123112")

    # Нажмите кнопку Continue
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    # Получение итоговой стоимости (Total)
    total = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
    print(total)

    # Проверьте, что итоговая сумма равна $58.29
    assert total == "Total: $58.29"

