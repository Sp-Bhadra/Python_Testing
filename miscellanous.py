from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless") #invoke browser without head
chrome_options.add_argument("--ignore-certificate-errors") #if url is unsfe in this case use ths (SSL Certificate)
ServiceObj = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=ServiceObj, options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,1500);") #scroll to 1500 pixel
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);") #Scroll down to bottom of page
driver.get_screenshot_as_file("screen.png") #Take screen shot
driver.close()
