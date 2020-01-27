from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators ():
        LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")
        REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-email")