from .base_page import BasePage
from .locators import ProductPageLocators
import time
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def should_be_btn_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button basket is not presented"
        assert not self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).get_attribute("disabled"), "Button basket is disabled"

    def should_add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def check_add_item_to_basket(self):
        "проверка выдаваемости сообщений и сверка данных"
        self.should_be_msg_add_succes()
        self.should_be_msg_eq_name()
        self.should_be_price_eq_basket()

    def should_be_msg_add_succes(self):
        assert self.is_element_present(*ProductPageLocators.MSG_SUCCES), "Мessage succes is not presented"

    def should_be_msg_eq_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_msg = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MSG).text
        assert product_name == product_name_msg, "Message name not eq name product msg"

    def should_be_price_eq_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_basket = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == product_price_basket, "Price not eq price product msg"
