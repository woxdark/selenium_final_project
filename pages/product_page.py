from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        link.click()

    def check_add_item_to_basket(self):
        "проверка выдаваемости сообщений и сверка данных"
        self.should_be_msg_add_succes()
        self.should_be_msg_eq_name()
        self.should_be_price_eq_basket()

    def should_basket_be_empty_for_guest(self):
        self.go_to_basket_page()
        assert len(self.browser.find_elements(*ProductPageLocators.BASKET_CONTENT)) == 1, "Basket not Empty for guest"
        assert self.browser.find_element(*ProductPageLocators.BASKET_CONTENT).text,\
            "Massage Empty basket not found"

    def should_be_btn_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button basket is not presented"
        assert not self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).get_attribute("disabled"), "Button basket is disabled"

    def should_be_msg_add_succes(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Мessage succes is not presented"

    def should_be_msg_eq_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_msg = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MSG).text
        assert product_name == product_name_msg, "Message name not eq name product msg"

    def should_be_price_eq_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_basket = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == product_price_basket, "Price not eq price product msg"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappered_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The element should disappear, but it didn't"

