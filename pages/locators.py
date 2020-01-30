from selenium.webdriver.common.by import By

#class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
        LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")
        REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-email")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BASKET = (By.CSS_SELECTOR, ".basket-mini")
    PRICE = (By.CSS_SELECTOR, ".price_color")
    POSITION = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_POSITION = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")