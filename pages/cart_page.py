from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty_cart_text(self):
        empty_cart_text = self.browser.find_element(*CartPageLocators.EMPTY_CART_TEXT).text
        assert "Your basket is empty" in empty_cart_text, "Empty cart text isn't presented"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_ITEMS_TITLE), \
            "Items are presented in basket, but should not be"