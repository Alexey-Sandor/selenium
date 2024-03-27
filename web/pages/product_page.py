import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage


class ProductLocator:
    ADD_PRODUCT_TO_CART_BUTTON = ("xpath", "(//button[text()='Add to cart'])[1]")
    REMOVE_PRODUCT_FROM_CART_BUTTON = ("xpath", "//button[text()='Remove']")
    GO_TO_CART_BUTTON = ("xpath", "//a[@class='shopping_cart_link']")

class ProductPage(BasePage):
    def add_product_to_cart(self):
        with allure.step("Добавляем товар в корзину"):
            self.find_element(ProductLocator.ADD_PRODUCT_TO_CART_BUTTON).click()

    def remove_product_from_cart(self):
        self.find_element(ProductLocator.REMOVE_PRODUCT_FROM_CART_BUTTON).click()

    def go_to_cart(self):
        with allure.step("Переходим в корзину"):
            self.find_element(ProductLocator.GO_TO_CART_BUTTON).click()