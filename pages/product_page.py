from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def check_success_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IS_ADDED_MESSAGE), "Success add message isn't presented"

    def check_product_name_in_success_add_to_basket_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_added_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ADDED_MESSAGE).text
        assert product_name == product_name_in_added_message,\
            "Incorrect product name in success message: got '{}', expected '{}'".format(product_name_in_added_message, product_name)

    def check_basket_total_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_PRICE_MESSAGE), "Basket total message isn't presented"

    def check_price_in_basket_total_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRISE).text
        product_price_in_basket_total_message = self.browser.find_element\
            (*ProductPageLocators.PRODUCT_PRICE_IN_BASKET_TOTAL_PRICE_MESSAGE).text
        assert product_price == product_price_in_basket_total_message, \
            "Incorrect price in basket total message: got '{}', expected '{}'".format(product_price_in_basket_total_message, product_price)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IS_ADDED_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_IS_ADDED_MESSAGE), \
            "Success message isn't disappear, but should"

