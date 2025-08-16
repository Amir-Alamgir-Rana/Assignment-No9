# Import Liabraries
import time

from selenium.webdriver.support.wait import WebDriverWait
#from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Navigation:
    def open_website(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        #driver.implicitly_wait(10)
        #driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
        driver.implicitly_wait(15)
        return driver

