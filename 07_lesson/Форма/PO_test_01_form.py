from selenium import webdriver
from Pages.DataType import DataType


def test_01_form():
    driver = webdriver.Chrome()

    # Создание экземпляра страницы
    data_type = DataType(driver)

    # Открытие страницы
    data_type.open_page()

    # Заполнение формы
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

    # Нажатие кнопки Submit
    data_type.btn_submit()

    # Выполнение проверочных действий
    data_type.zip_code_red()
    data_type.green_fields()

    # Закрытие браузера
    driver.quit()
