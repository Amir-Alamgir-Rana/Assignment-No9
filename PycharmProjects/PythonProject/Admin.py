import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.support import expected_conditions as EC

class Admin:
    def __init__(self,driver):
        self.driver=driver

    def add_Admin(self):
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()

        wait = WebDriverWait(self.driver, 20)

        # Step 1: Click the dropdown to expand
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='oxd-select-text-input']")))
        dropdown.click()

        # Step 2: Click "ESS" option from the list
        admin_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='oxd-form-row']//div[3]")))
        admin_option.click()
        self.driver.implicitly_wait(20)

        self.driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("Amir_Alamgir")
        self.driver.implicitly_wait(20)

        wait = WebDriverWait(self.driver, 20)

        # Step 1: Click the dropdown to expand
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[3]//div[1]//div[2]//div[1]//div[1]//div[2]//i[1]")))
        dropdown.click()

        # Step 2: Click "ESS" option from the list
        self.driver.implicitly_wait(20)
        admin_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option']//span[text()='Disabled']")))
        admin_option.click()
        self.driver.implicitly_wait(20)

        #Enter username
        wait = WebDriverWait(self.driver, 15)

        # Locate input field
        input_field = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@class='oxd-input oxd-input--focus oxd-input--error']")))

        input_field.click()
        #self.driver.implicitly_wait(20)

        #Enter password
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH,"//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']").send_keys("admin123")

        #Enter Conform_password
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--focus']").send_keys("admin123")

        # Save Record
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()















