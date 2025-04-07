import allure
from selenium import webdriver
from Pages.DataType import DataType

@allure.feature("Тестирование формы")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка заполнения формы и подсветки полей")
@allure.description("Тест проверяет корректность заполнения формы и подсветку полей.")
def test_01_form():
    driver = webdriver.Chrome()

    with allure.step("Создание экземпляра страницы"):
        data_type = DataType(driver)

    with allure.step("Открытие страницы"):
        data_type.open_page()

    with allure.step("Заполнение формы"):
        data_type.first_name("Иван")
        data_type.last_name("Петров")
        data_type.address("Ленина, 55-3")
        data_type.e_mail("test@skypro.com")
        data_type.phone("+7985899998787")
        data_type.zip_code("")
        data_type.city("Москва")
        data_type.country("Россия")
        data_type.job_position("QA")
        data_type.company("SkyPro")

    with allure.step("Нажатие кнопки 'Submit'"):
        data_type.btn_submit()

    with allure.step("Выполнение проверочных действий"):
        data_type.zip_code_red()
        data_type.green_fields()

    with allure.step("Закрытие браузера"):
        driver.quit()