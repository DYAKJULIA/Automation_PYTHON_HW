import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")
time.sleep(5)

# Найти и нажать кнопку "Close" в модальном окне
close_button = driver.find_element(By.XPATH, "//div[@class='modal-footer']/p")
close_button.click()
print("Модальное окно закрыто!")

driver.quit()