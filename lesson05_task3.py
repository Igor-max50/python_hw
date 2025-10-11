# Упражнение 3. Поле ввода
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Открыть Firefox
driver = webdriver.Firefox()
driver.maximize_window()

# Перейти на сайт
driver.get("https://the-internet.herokuapp.com/inputs")

search_field = driver.find_element(By.CSS_SELECTOR, "input")
search_field.send_keys("123")

search_field.clear()
search_field.send_keys("456")

sleep(2)
driver.quit()


