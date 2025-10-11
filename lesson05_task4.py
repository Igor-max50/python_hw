# Упражнение 4. Форма авторизации
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Открыть Firefox
driver = webdriver.Firefox()
driver.maximize_window()

# Перейти на сайт
driver.get("https://the-internet.herokuapp.com/login")

# Логин
username_input = driver.find_element(By.XPATH,'//input[@id="username"]')
username_input.send_keys("tomsmith")
# Пароль
password_input = driver.find_element(By.XPATH,'//input[@id="password"]')
password_input.send_keys("SuperSecretPassword!",)

button = driver.find_element(By.CSS_SELECTOR, "button.radius")
button.click()

flash = driver.find_element(By.ID, "flash").text
print(flash)

sleep(2)
driver.quit()