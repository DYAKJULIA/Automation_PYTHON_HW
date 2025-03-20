from selenium.webdriver.common.by import By


class DataType:

    def __init__(self, driver):
        self._driver = driver

# Открытие страницы
    def open_page(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        # Ожидание загрузки страницы
        self._driver.implicitly_wait(2)

# Заполнение формы
    def first_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(term)

    def last_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(term)

    def address(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(term)

    def e_mail(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(term)

    def phone(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(term)

    def zip_code(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys(term)

    def city(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(term)

    def country(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(term)

    def job_position(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys(term)

    def company(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(term)

# Нажатие кнопки Submit
    def btn_submit(self):
        self._driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Проверьте (assert), что поле Zip code подсвечено красным
    def zip_code_red(self):
        zip_code_color = self._driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
        assert "alert-danger" in zip_code_color

# Проверьте (assert), что остальные поля подсвечены зеленым
    def green_fields(self):
        green_color = self._driver.find_elements(By.CSS_SELECTOR, ".alert-success")
        assert len(green_color) == 9
