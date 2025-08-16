import app
import wait
from select import select
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.get("https://codepen.io/RobotsPlay/pres/pyNLdL")
#def test_openbrowser():
#    driver.get("https://candymapper.com/")
 #   driver.maximize_window()
#driver.get("https://candymapper.com/")
#driver.maximize_window()
#element=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "dropdown")))
#driver.find_element(By.XPATH, value="//input[@name='username']").click()
#driver.find_element(By.XPATH,value="//span[normalize-space()='Add Account']").click()
#driver.implicitly_wait(10)
#driver.save_screenshot("test.png")
#driver.execute_script("window.scrollTo(0, 1100);")
#input("Press enter to continue...")

def add(d,b):
    return d+b



def sub(d,b):
    return d-b


def test_add():
    print(add(2,4))

def test_sub():
    print(sub(2,4))