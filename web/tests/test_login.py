import pytest
import allure

from web.pages import LoginPage
from web.utils import Config
from .manager_test import BaseTest


@pytest.mark.login
@allure.feature("Авторизация пользователя")
@allure.suite("Авторизация пользователя")
class TestAuthenticationSuite(BaseTest):
    @allure.title("Авторизация с валидными данными")
    def test_success_login(self, chrome_driver):
        expected_url = "https://www.saucedemo.com/inventory.html"
        login_page = LoginPage(chrome_driver)
        login_page.go_to_site()
        login_page.login(Config.USERNAME, Config.PASSWORD)
        try:
            assert expected_url == chrome_driver.current_url, "Авторизация не сработала"

        except AssertionError as e:
            self.handle_assertion_error(chrome_driver, e)

    @allure.title("Авторизация с невалидным логином")
    def test_invalid_login(self, chrome_driver):
        login_page = LoginPage(chrome_driver)
        login_page.go_to_site()
        login_page.login("invalid_login", Config.PASSWORD)
        try:
            assert (
                login_page.find_element(("css selector", "[data-test='error']")).text
                == "Epic sadface: Username and password do not match any user in this service"
            ), "Авторизация не должна быть успешной с пустыми полями"
        except AssertionError as e:
            self.handle_assertion_error(chrome_driver, e)

    @allure.title("Авторизация с пустым логином и паролем")
    def test_invalid_username(self, chrome_driver):
        login_page = LoginPage(chrome_driver)
        login_page.go_to_site()
        login_page.login("", "")
        try:
            assert (
                login_page.find_element(("css selector", "[data-test='error']")).text
                == "Epic sadface: Username is required"
            ), "Авторизация не должна быть успешной с пустыми полями"
        except AssertionError as e:
            self.handle_assertion_error(chrome_driver, e)
