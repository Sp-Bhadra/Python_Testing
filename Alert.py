from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name ="Sarada"
ServiceObj = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=ServiceObj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Sarada")
driver.find_element(By.ID, "confirmbtn").click()  #"alertbtn"
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.dismiss()

