from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

# Перейдите на сайт
driver.get("http://uitestingplayground.com/textinput")

# Найти поле ввода и ввести текст "SkyPro"
input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")

# Нажмите на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()

# Получите текст кнопки и выведите в консоль ("SkyPro")
print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)

driver.quit()