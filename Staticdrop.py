import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("D:// chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "name").send_keys("Sarada")
driver.find_element(By.NAME, "email").send_keys("sarada@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Sarada123")
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
message = driver.find_element(By.XPATH, "//strong[text()='Success!']").text
assert "Success" in message
driver.close()

