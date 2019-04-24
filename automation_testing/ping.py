from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import json
from time import sleep

class AutomationTesting:
    def __init__(self):
        self.browser = webdriver.Chrome('./chromedriver')
        with open('data.json',"r") as json_file:
            self.data = json.load(json_file)

    def system_login(self):
        # import pdb; pdb.set_trace()
        self.browser.get(self.data["url"])
        delay = 3
        try:
            WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.ID, 'mat-input-0')))
            print ("Ping is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        username =self.browser.find_element_by_id("mat-input-0")
        password = self.browser.find_element_by_id("mat-input-1")
        username.send_keys(self.data["username"])
        password.send_keys(self.data["password"])
        login_attempt = self.browser.find_element_by_xpath("//*[@type='submit']")
        login_attempt.submit()
        delay = 3
        try:
            WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.ID, 'mat-raised-button')))
            print ("Ping is ready!")
        except TimeoutException:
            print ("Loading took too much time!")
        self.browser.find_element_by_class_name('mat-raised-button').click()
        delay = 3
        try:
            WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'mat-input-2')))
            print ("Alert is ready!")
        except TimeoutException:
            print ("Loading took too much time!")
        login_attempt1 = self.browser.find_element_by_id("mat-input-2")
        login_attempt1.send_keys(self.data["alert"])

        self.browser.find_element_by_class_name('mat-select-trigger').click()
        self.browser.find_element_by_id('mat-option-22').click()
       

if __name__=="__main__":
    pg=AutomationTesting()
    pg.system_login()
