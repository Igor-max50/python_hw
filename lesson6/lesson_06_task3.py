# Дождаться картинки
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((
        By.ID, "text"), "Done!"))

third_image_1 = driver.find_element(By.ID, "compass")
third_image_2 = driver.find_element(By.ID, "calendar")
third_image_3 = driver.find_element(By.ID, "award")
third_image_4 = driver.find_element(By.ID, "landscape")

print(third_image_3.get_attribute("src"))

driver.quit()
