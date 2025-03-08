from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Найти поле ввода и ввести текст 1000
input_field = driver.find_element(By.CSS_SELECTOR, "input")
input_field.send_keys("1000")
sleep(2)

#Очистите это поле (метод clear)
input_field.clear()
sleep(1)

#Введите в это же поле текст 999
input_field.send_keys("999")
sleep(2)

print("Замена текста закончена!")
driver.quit()