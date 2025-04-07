import allure
from selenium import webdriver
from Pages.SlowCalculator import SlowCalculator

@allure.feature("Тестирование медленного калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка вычисления с задержкой")
@allure.description("Тест проверяет, что калькулятор корректно работает с задержкой.")
def test_02_calc():
    driver = webdriver.Chrome()

    with allure.step("Создание экземпляра страницы"):
        slow_calculator = SlowCalculator(driver)

    with allure.step("Открытие страницы"):
        slow_calculator.open_page()

    with allure.step("Заполнение поля ввода по локатору #delay"):
        slow_calculator.delay("45")

    with allure.step("Заполнение формы значениями и ожидание результата"):
        slow_calculator.calc()

    with allure.step("Проверка результата"):
        slow_calculator.result()

    with allure.step("Закрытие браузера"):
        driver.quit()