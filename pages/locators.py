from selenium.webdriver.common.by import By
import time


#class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
        LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")
        REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
        REGISTRATION_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
        REGISTRATION_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
        REGISTRATION_FORM_PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, "#id_registration-password2")
        REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


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
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_LINK = (By.XPATH, '//a[text()="View basket"]')
    BASKET_STAFF_EMPTY = (By.CSS_SELECTOR, "#content_inner p")

