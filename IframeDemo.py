from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ServiceObj = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=ServiceObj)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Ready to Automate")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)

driver.close()