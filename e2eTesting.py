from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("D:\\chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")

driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']").click()

ProductList = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for lis in ProductList:
    ProductName = lis.find_element(By.XPATH, "div/h4/a").text
    if ProductName == "Blackberry":
        lis.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*= 'btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
driver.find_element(By.ID, "country").send_keys("in")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
sucessmsg = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you!" in sucessmsg
driver.close()
