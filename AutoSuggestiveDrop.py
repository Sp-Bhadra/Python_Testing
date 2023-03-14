import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ServiceObj = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=ServiceObj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
Countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(Countries))
for country in Countries:
    if country.text == "India":
        country.click()
        break
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
driver.close()
