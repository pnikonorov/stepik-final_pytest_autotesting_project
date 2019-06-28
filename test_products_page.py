import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize('offer_name', ['offer'+ str(n) for n in range(10)])
def test_guest_can_add_product_to_cart(browser, offer_name):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={}".format(offer_name)
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.check_success_add_to_basket_message()
    page.check_product_name_in_success_add_to_basket_message()
    page.check_basket_total_message()
    page.check_price_in_basket_total_message()
