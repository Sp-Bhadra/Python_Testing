from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_Obj = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=Service_Obj)
driver.maximize_window()
Url = "https://opensource-demo.orangehrmlive.com"
driver.get(Url)
url = driver.current_url
driver.implicitly_wait(2000)

if Url in url:
    Title = driver.title
    ExTitle = "OrangeHRM"
    if Title == ExTitle:
        l = driver.find_elements(By.TAG_NAME, "a")
        print("No of element present is", len(l))

        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        driver.find_element(By.TAG_NAME, "button").click()
        Homepage = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
        Homepageurl = driver.current_url
        if Homepageurl == Homepage:
            print("Landed on Home Page")
        else:
            print("Incorrect Login")


    else:
        print("Title did not matched so test case failed ")


else:
    print("TestCase Failed")
driver.close()
