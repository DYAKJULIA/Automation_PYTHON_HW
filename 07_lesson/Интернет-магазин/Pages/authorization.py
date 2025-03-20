from selenium.webdriver.common.by import By

class Authorization:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        # Ожидание загрузки страницы
        self._driver.implicitly_wait(2)

# Авторизация
    def user_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(term)

    def password(self, term):
            self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(term)

# Нажать кнопку Login
    def login(self):
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()