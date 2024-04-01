import time

import allure

from web.pages import CartPage, ProductPage, OrderPage, LoginPage
from web.utils import Config
from .manager_test import BaseTest


@allure.feature("Оформление заказа")
@allure.suite("Оформление заказа")
class TestOrderSuite(BaseTest):
    @allure.title("Оформление заказа")
    def test_create_order(self, chrome_driver):
        excepted_url = "https://www.saucedemo.com/checkout-complete.html"
        login_page = LoginPage(chrome_driver)
        product_page = ProductPage(chrome_driver)
        cart_page = CartPage(chrome_driver)
        order_page = OrderPage(chrome_driver)
        login_page.go_to_site()
        login_page.login(Config.USERNAME, Config.PASSWORD)
        product_page.add_product_to_cart()
        product_page.go_to_cart()
        cart_page.click_checkout()
        order_page.fill_in_the_form("alexey", "sandor", "234432")
        order_page.click_finish_button()
        assert order_page.driver.current_url == excepted_url
