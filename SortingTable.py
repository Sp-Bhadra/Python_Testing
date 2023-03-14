from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
BrowserSortedWebElemt = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#1st Sort that table
driver.find_element(By.XPATH, "//span[text() = 'Veg/fruit name']").click()
#collect text visible in to a list
VeggieWebElementList = driver.find_elements(By.XPATH, "//tr//td[1]")
for ele in VeggieWebElementList:
    BrowserSortedWebElemt.append(ele.text) #collecting text into List
ActualBrowserWebElement = BrowserSortedWebElemt.copy()#copying of sorted Iteams
BrowserSortedWebElemt.sort() # sorting Table
assert BrowserSortedWebElemt == ActualBrowserWebElement
driver.close()
