import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import time


# Не уверен, что нужна параметризация в данном тесте, но в заданиях не было её убрать.
# Если необходимо её убрать - закомментируйте строки @pytest.mark.parametrize и исправьте link в данном тесте
# Сорри за русский в комментариях, но ИМХО слишком большой текст для восприятия на английском:)
@pytest.mark.need_review
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

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_not_be_items_in_basket()
    cart_page.should_be_empty_cart_text()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.user
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, "HgF123DsA")
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_cart()
        page.check_success_add_to_basket_message()
        page.check_product_name_in_success_add_to_basket_message()
        page.check_basket_total_message()
        page.check_price_in_basket_total_message()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()