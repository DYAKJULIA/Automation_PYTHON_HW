from selenium import webdriver
from Pages.SlowCalculator import SlowCalculator


def test_02_calc():
    driver = webdriver.Chrome()

    # Создание экземпляра страницы
    slow_calculator = SlowCalculator(driver)

    # Открытие страницы
    slow_calculator.open_page()

    # Заполнение поля ввода по локатору #delay
    slow_calculator.delay("45")

    # Заполнение формы значениями и ожидание результата
    slow_calculator.calc()

    # Проверка результата
    slow_calculator.result()

    # Закрытие браузера
    driver.quit()