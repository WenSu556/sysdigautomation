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

    # Set region 
    def set_region(self, region):
        logging.info("set_region: %s", region)
        # Expend region menu
        curele = WebDriverWait(self.driver, self.waittime).until(EC.presence_of_element_located(LoginLocators.regions_menu)) 
        regele = curele.find_element(By.XPATH, '..')
        regele.click()

        # Click according region
        css_value = 'span[title="' + region + '"'
        newregele = self.driver.find_element(By.CSS_SELECTOR, css_value)
        newregele.click()
    
    # Click "Forgot your password"
    def click_forgot_pw(self):
        logging.info("click_forgot_pw")
        forgotele = WebDriverWait(self.driver, self.waittime).until(EC.presence_of_element_located(LoginLocators.forgot_link))    
        forgotele.click()

    # Go back from "Forgot your password" page
    def go_back_to_main(self):
        logging.info("go_back_to_main")
        backele = WebDriverWait(self.driver, self.waittime).until(EC.presence_of_element_located(LoginLocators.back_link))
        backele.click()

    # Google log in 
    def click_google_login(self):
        logging.info("click_google_login")
        googleele = WebDriverWait(self.driver, self.waittime).until(EC.presence_of_element_located(LoginLocators.google_login))
        googleele.click()