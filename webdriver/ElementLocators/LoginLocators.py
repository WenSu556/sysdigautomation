from selenium.webdriver.common.by import By

class LoginLocators:
    email_input = (By.NAME, 'username')
    email_pwd = (By.NAME, 'password')
    regions_menu = (By.CSS_SELECTOR, 'div[title]')
    forgot_link = (By.CSS_SELECTOR, 'a[href*="forgotPassword"]')
    back_link = (By.CSS_SELECTOR, 'a[href*="login"]')
    google_login = (By.CSS_SELECTOR, 'a[href*="google"]')