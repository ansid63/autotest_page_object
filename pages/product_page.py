from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def test_guest_can_add_product(self):
        self.should_add_goods()
        self.solve_quiz_and_get_code()
        time.sleep(5)
        self.check_basket_price()
        self.check_basket_position()

    def should_add_goods(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def check_basket_price(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET)
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        assert price.text in basket.text, "Price wrong"

    def check_basket_position(self):
        position = self.browser.find_element(*ProductPageLocators.POSITION)
        basket_position = self.browser.find_element(*ProductPageLocators.BASKET_POSITION)
        assert position.text in basket_position.text, "Position/Name wrong"