import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

ServiceObj = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=ServiceObj)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
WindowsOpened = driver.window_handles
driver.switch_to.window(WindowsOpened[1])
'''
Text = driver.find_element(By.XPATH, "//p[contains(text(),'Please email us at')]").text
driver.close()
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", Text)
print(emails)
'''
Text = driver.find_element(By.XPATH,"//div/p[2]").text
emails = Text.split("at")[1].strip().split(" ")[0]
driver.close()
driver.switch_to.window(WindowsOpened[0])
assert "Username:" == driver.find_element(By.CSS_SELECTOR, ".text-white[for='username']").text
driver.find_element(By.NAME, "username").send_keys(emails)
driver.find_element(By.ID, "password").send_keys("Sara@123")
Radios = driver.find_elements(By.CSS_SELECTOR, ".checkmark")
Radios[1].click()
time.sleep(2)
driver.find_element(By.ID, "cancelBtn").click()
dropdown = Select(driver.find_element(By.XPATH, "//select[@class='form-control']"))
dropdown.select_by_visible_text("Teacher")
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver.find_element(By.NAME, "signin").click()
driver.implicitly_wait(4)
wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[starts-with(text(),' username/password.')]")))
Invalid = driver.find_element(By.XPATH, "//div[starts-with(text(),' username/password.')]").text
assert "Incorrect username/password." == Invalid
print("Passed")
driver.close()
