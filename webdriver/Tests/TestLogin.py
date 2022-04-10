import unittest
import logging
from urllib import parse
from selenium import webdriver

from webdriver.Pages.LogInPage import LogInPage
from webdriver.utils.JsonParser import JsonParser

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path = r"webdriver/drivers/geckodriver.exe")
        #cls.driver = webdriver.Edge(r"webdriver/drivers/msedgedriver.exe")
        cls.jparser = JsonParser()
        cls.log_in_page = LogInPage(cls.driver)

    # test case for email log in
    def test_email_login(self):
        logging.info("Begin testing: test_email_login")
        test_cases = self.jparser.read_json('LoginPageCases.json', 'emaillogin')['testcase']      
        for test in test_cases:
            test_email = test['input']['username']
            test_pw = test['input']['password']
            test_result = test['expect']
            self.log_in_page.set_email(test_email)
            self.log_in_page.set_empw(test_pw)
            # Omit clicking "Log in" button as required. Will not check result.    
            # 
        logging.info("Finish testing: test_email_login")

        # test case for testing all previous tests with different regions
    def test_mixed(self):
        logging.info("Begin testing: test_mixed")
        domains = self.jparser.read_json('LoginPageCases.json', 'domain')      
        for domain in domains:
            self.driver.get(domain)
            self.test_email_login()
        logging.info("Finish testing: test_mixed")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestLogin('test_mixed'))
    return suite

if __name__ == "__main__":
    logging.basicConfig(filename='./webdriver/logs/testlogin.log', encoding='utf-8', level=logging.INFO)
    logging.debug('This message should go to the log file')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())