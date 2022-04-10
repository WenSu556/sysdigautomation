from selenium.webdriver.common.by import By

class LoginLocators:
    email_input = (By.NAME, 'username')
    email_pwd = (By.NAME, 'password')
    regions_menu = (By.CSS_SELECTOR, 'div[title]')