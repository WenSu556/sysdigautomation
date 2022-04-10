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

    # test case for changing regions
    def test_change_regions(self):
        logging.info("Begin testing: test_change_regions")
        test_cases = self.jparser.read_json('LoginPageCases.json', "regiondropdown")['testcase']
        for test in test_cases:
            self.log_in_page.set_region(test['input'])
            # Check new url is correct
            self.assertTrue(self.driver.current_url.startswith(test['expect']))
        logging.info("Finish testing: test_change_regions")

    # test case for forgot password link
    def test_forgot_password(self):
        logging.info("Begin testing: test_forgot_password")
        expect = self.jparser.read_json('LoginPageCases.json', "forgotpwlink")['expect']
        new_url = parse.urldefrag(self.driver.current_url)[0] # base url
        self.log_in_page.click_forgot_pw()
        
        new_url = new_url + expect
        self.assertEqual(self.driver.current_url, new_url)

        # Go back to log in page for other test cases
        self.driver.back()
        logging.info("Finish testing: test_forgot_password")


    # test case for google sign in
    def test_google_signin(self, domain):
        logging.info("Begin testing: test_google_signin")
        self.log_in_page.click_google_login()

        # AP domain or other domains
        test_domain = self.jparser.read_json('LoginPageCases.json', "googlesignin")['domain']
        if domain in test_domain:
            test_expect = self.jparser.read_json('LoginPageCases.json', "googlesignin")['expect']
            self.assertTrue(self.driver.current_url.startswith(test_expect))
        else: #AP domain
            test_expect = self.jparser.read_json('LoginPageCases.json', "googlesigninexception")['expect']
            self.assertTrue(test_expect in self.driver.current_url)

        # Go back to log in page for other test cases
        self.driver.back()
        logging.info("Finish testing: test_google_signin")

        # test case for testing all previous tests with different regions
    def test_mixed(self):
        logging.info("Begin testing: test_mixed")
        domains = self.jparser.read_json('LoginPageCases.json', 'domain')      
        for domain in domains:
            self.driver.get(domain)
            self.test_email_login()
            self.test_forgot_password()
            self.test_google_signin(domain)
            self.test_change_regions()
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