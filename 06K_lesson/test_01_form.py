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
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Ожидаем загрузку страницы
    driver.implicitly_wait(2)

    # Заполните форму значениями
    driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

    # Нажмите кнопку Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверьте (assert), что поле Zip code подсвечено красным
    zip_code_color = driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
    assert "alert-danger" in zip_code_color

    # Проверьте (assert), что остальные поля подсвечены зеленым
    green_color = driver.find_elements(By.CSS_SELECTOR, '.alert-success')
    assert len(green_color) == 9
