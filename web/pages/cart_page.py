import allure

from .base_page import BasePage

class CartLocator:
    CHECKOUT_BUTTON = ('xpath', "//button[@name='checkout']")

class CartPage(BasePage):
    def click_checkout(self):
        with allure.step("Переходим к оформлению заказа"):
            self.find_element(CartLocator.CHECKOUT_BUTTON).click()