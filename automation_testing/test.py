from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import json
from time import sleep

class AutomationTesting:
    def __init__(self):
        self.browser = webdriver.Chrome('./chromedriver')
        # with open('data.json',"r") as json_file:
        #     self.data = json.load(json_file)

    def system_login(self):
        # import pdb; pdb.set_trace()
        self.browser.get("http://3.8.158.97:4551/pingAlert/createAlert")
        delay = 3
        try:
            WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.ID, 'mat-input-77')))
            print ("Ping is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        username =self.browser.find_element_by_id("mat-input-77")
        # password = self.browser.find_element_by_id("mat-input-1")
        # username.send_keys(self.data["username"])
        password.send_keys("test1")
        # login_attempt = self.browser.find_element_by_xpath("//*[@type='submit']")
        # login_attempt.submit()
        # delay = 3
        # try:
        #     WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.ID, 'mat-raised-button')))
        #     print ("Ping is ready!")
        # except TimeoutException:
        #     print ("Loading took too much time!")
        # self.browser.find_element_by_class_name('mat-raised-button').click()
        # delay = 3
        # try:
        #     WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.ID, '#mat-input-77')))
        #     print ("Alert is ready!")
        # except TimeoutException:
        #     print ("Loading took too much time!")
        # head = self.browser.find_element_by_css_selector("#mat-input-77")
        # # frame_elem = head.find_element_by_class_name("mat-form-field-flex")
        # # alert =frame_elem.find_element_by_id("mat-input-77")
        # head.send_keys("test1")
        # sleep(10)mat-input-77
        # self.browser.quit()

if __name__=="__main__":
    pg=AutomationTesting()
    pg.system_login()
