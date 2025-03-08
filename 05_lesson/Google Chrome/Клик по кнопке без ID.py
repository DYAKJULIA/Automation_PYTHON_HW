from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Откройте страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Кликните на синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
blue_button.click()
print("Кнопка работает!")

driver.quit()
