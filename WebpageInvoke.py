from selenium import webdriver
from selenium.webdriver.chrome.service import Service

Service_obj = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
