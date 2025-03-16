from selenium.webdriver.common.by import By

class Overview:

    def __init__(self, driver):
        self._driver = driver

    # ОФОРМЛЕНИЕ ЗАКАЗА
    # Заполнение формы данными: имя, фамилия, почтовый индекс
    def first_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(term)

    def last_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(term)

    def postal_code(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(term)

    # Нажмите кнопку Continue
    def further(self):
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()

    # Получение итоговой стоимости (Total)
    def total(self):
        total = self._driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
        print(total)
        # Проверьте, что итоговая сумма равна $58.29
        assert total == "Total: $58.29"
