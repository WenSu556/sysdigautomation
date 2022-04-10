import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver.ElementLocators.LoginLocators import LoginLocators

class LogInPage:
    def __init__(self, driver):
        self.driver = driver
        self.waittime = 20

    # Set user email in log in box
    def set_email(self, email):      
        logging.info("set_email: %s", email)  
        emailele = WebDriverWait(self.driver, self.waittime).until(EC.presence_of_element_located(LoginLocators.email_input))
        emailele.send_keys(email)
    
    # Input email password in log in box
    def set_empw(self, pw):
        logging.info("set_empw: %s", pw)
        pwele = WebDriverWait(self.driver, self.waittime).until(EC.presence_of_element_located(LoginLocators.email_pwd)) 
        pwele.send_keys(pw)