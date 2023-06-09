from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ServiceObj = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=ServiceObj)
driver.get("https://accounts.google.com/signup")

driver.find_element(By.XPATH, "//a[normalize-space()='Help']").click()

#prints parent window title
print("Parent window title: " + driver.title)

#get current window handle
p = driver.current_window_handle

#get first child window
chwd = driver.window_handles

for w in chwd:
#switch focus to child window
    if(w!=p):
        driver.switch_to.window(w)
    break
time.sleep(0.9)
print("Child window title: " + driver.title)
driver.quit()
