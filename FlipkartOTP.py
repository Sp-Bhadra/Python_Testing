import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_Obj = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=Service_Obj)
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(3)

Login = driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/input[1]")
Login.send_keys("8594938288")
driver.find_element(By.XPATH, "//button[normalize-space()='Request OTP']").click()
time.sleep(3)
otp = driver.find_elements(By.XPATH, "//input[@class='_2IX_2- _1WRfas']")

for ot in otp:
    ot.send_keys([227244])
    break
