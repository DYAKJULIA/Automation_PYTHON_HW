from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

# Открыть страницу
driver.get("http://uitestingplayground.com/classattr")

#Кликнуть на синюю кнопку
button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
button.click()
print("Кнопка работает!")

driver.quit()
