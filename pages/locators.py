from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#register_form #id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#register_form #id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#register_form #id_registration-password2')
    REGISTER_SUBMIT = (By.NAME, 'registration_submit')

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    BASKET = (By.CLASS_NAME, 'basket-mini')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_MSG = (By.CSS_SELECTOR, '.alertinner strong:nth-child(1)')
    BASKET_TOTAL = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    MSG_SUCCES = (By.CLASS_NAME, 'alert-success')
