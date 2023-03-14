from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

ServiceObj = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=ServiceObj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
'''driver.get("https://www.flipkart.com/")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")))
driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']").click() '''
action = ActionChains(driver)
#action.move_to_element(driver.find_element(By.CSS_SELECTOR, "._1_3w1N")).perform()
# action.click_and_hold()  To click and hold
# action.double_click() To double-click any button
# action.drag_and_drop() To clcik and drag
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()


