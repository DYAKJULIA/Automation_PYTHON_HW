from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликните на кнопку
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for i in range(5):
    add_button.click()

# Соберите со страницы список кнопок Delete. Выведите на экран размер списка.
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

print("Количество кнопок Delete:", len(delete_buttons))
sleep(3)


driver.quit()