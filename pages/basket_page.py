from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import ProductPageLocators
import time


class BasketPage(BasePage):
    def check_basket_empty(self):
        basket_staff_empty = self.browser.find_element(*BasketPageLocators.BASKET_STAFF_EMPTY)
        assert "Your basket is empty." in basket_staff_empty.text, "There is bug in basket"

    def should_add_goods(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappeared"