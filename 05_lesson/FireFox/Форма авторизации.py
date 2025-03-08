from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/login")

# В поле username введите значение "tomsmith"
username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys("tomsmith")

# В поле password введите значение "SuperSecretPassword!"
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("SuperSecretPassword!")

# Нажмите кнопку Login
button_login = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
button_login.click()
sleep(3)

print("Авторизация прошла успешно!")

driver.quit()