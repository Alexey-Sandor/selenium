import time
import allure
import pytest
from web.utils.config import Config
from web.pages import LoginPage, ProductPage
from .manager_test import BaseTest


@pytest.mark.cart
@allure.feature("Работа с корзиной")
@allure.suite("Работа с корзиной")
class TestCartPage(BaseTest):
    @allure.title("Успешное добавление товара в корзину")
    def test_add_to_cart(self, chrome_driver, mocker):
        login_page = LoginPage(chrome_driver)
        product_page = ProductPage(chrome_driver)
        login_page.go_to_site()
        login_page.login(Config.USERNAME, Config.PASSWORD)
        product_page.add_product_to_cart()
        try:
            assert (
                product_page.find_element(
                    ("xpath", "//span[@class='shopping_cart_badge']")
                ).text
                == "1"
            ), "Товар не добавлен в корзину"
        except AssertionError as e:
            self.handle_assertion_error(chrome_driver, e)
        finally:
            product_page.driver.execute_script("window.localStorage.clear();")

    def test_remove_from_cart(self, chrome_driver):
        login_page = LoginPage(chrome_driver)
        product_page = ProductPage(chrome_driver)
        login_page.go_to_site()
        login_page.login(Config.USERNAME, Config.PASSWORD)
        product_page.add_product_to_cart()
        product_page.remove_product_from_cart()
        try:
            assert product_page.invisibility_of_element_located(
                ("xpath", "//span[@class='shopping_cart_badge']"), 10
            ), "Корзина не пустая"
        except AssertionError as e:
            self.handle_assertion_error(chrome_driver, e)
