from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

# Перейдите на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Дождитесь загрузки всех картинок
driver.implicitly_wait(10)

src = driver.find_element(By.CSS_SELECTOR, 'img[src="img/award.png"]').get_attribute('src')

print(src)

driver.quit()
