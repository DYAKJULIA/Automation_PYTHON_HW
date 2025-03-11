import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем WebDriver
@pytest.fixture()
def driver():
    # Указываем путь к драйверу
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_01_form(driver):
    # Откройте страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Ожидаем загрузку страницы
    driver.implicitly_wait(2)

    # В поле ввода по локатору #delay введите значение 45.
    driver.find_element(By.ID, "delay").clear()
    driver.find_element(By.ID, "delay").send_keys("45")

    # Заполните форму значениями
    driver.find_element(By.XPATH, "//span[normalize-space()='7']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='+']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='8']").click()
    driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning']").click()

    # Проверьте (assert), что в окне отобразится результат 15 через 45 секунд
    WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    result = driver.find_element(By.CSS_SELECTOR, "div.screen").text
    assert int(result) == 15
