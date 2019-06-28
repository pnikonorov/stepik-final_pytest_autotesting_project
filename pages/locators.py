from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FROM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTER_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTER_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "[name='registration_submit']")
    #EMAIL_LOGIN_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    #PASSWORD_LOGIN_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    #LOG_IN_BTN = (By.CSS_SELECTOR, "[name='login_submit']")

class ProductPageLocators(object):
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRISE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_IS_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1)")
    PRODUCT_NAME_IN_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1) > .alertinner > strong")
    BASKET_TOTAL_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-info")
    PRODUCT_PRICE_IN_BASKET_TOTAL_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-info strong")

class CartPageLocators(object):
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS_TITLE = (By.CSS_SELECTOR, "#content_inner > .basket-title")