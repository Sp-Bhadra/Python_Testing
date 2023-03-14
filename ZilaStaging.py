import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("D://chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://zila-staging.ccdms.in/")
driver.implicitly_wait(5)
driver.find_element(By.NAME,"email").send_keys("5111909077")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".mat-focus-indicator.btn.orange-btn.login-form-field.mat-button.mat-button-base").click()

time.sleep(2)
AllOtp = driver.find_elements(By.XPATH, "//input[@pattern='\d*']")

for i in AllOtp:
    i.send_keys("227244")
    break
driver.find_element(By.XPATH, "//mat-icon[text()='visibility_off']").click()
driver.find_element(By.XPATH, "//span[text()='Log In']").click()

