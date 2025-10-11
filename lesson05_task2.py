# Упражнение 2. Клик по кнопке без ID
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Открыть Google Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Перейти на сайт
driver.get("http://uitestingplayground.com/dynamicid")

# Нажать на синюю кнопку 3 раза

button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
button.click()

sleep(2)
driver.quit()