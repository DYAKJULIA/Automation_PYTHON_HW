from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculator:

    def __init__(self, driver):
        self._driver = driver

# Открытие страницы
    def open_page(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        # Ожидание загрузки страницы
        self._driver.implicitly_wait(2)

# Заполнение поля ввода по локатору #delay
    def delay(self, term):
        self._driver.find_element(By.ID, "delay").clear()
        self._driver.find_element(By.ID, "delay").send_keys(term)

# Заполнение формы значениями и ожидание результата
    def calc(self):
        self._driver.find_element(By.XPATH, "//span[normalize-space()='7']").click()
        self._driver.find_element(By.XPATH, "//span[normalize-space()='+']").click()
        self._driver.find_element(By.XPATH, "//span[normalize-space()='8']").click()
        self._driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning']").click()
        # Ожидание результата
        WebDriverWait(self._driver, 45).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    # Проверка результата
    def result(self):
        result = self._driver.find_element(By.CSS_SELECTOR, "div.screen").text
        assert int(result) == 15