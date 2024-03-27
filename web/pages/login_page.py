from .base_page import BasePage
import allure


class LoginLocator:
    USERNAME_INPUT = ("xpath", "//input[@id='user-name']")
    PASSWORD_INPUT = ("xpath", "//input[@id='password']")
    LOGIN_BUTTON = ("xpath", "//input[@id='login-button']")


class LoginPage(BasePage):

    def login(self, username, password):
        with allure.step(f"Ввод имени пользователя: {username}"):
            self.find_element(LoginLocator.USERNAME_INPUT).send_keys(username)
        with allure.step(f"Ввод пароля: {password}"):
            self.find_element(LoginLocator.PASSWORD_INPUT).send_keys(password)
        with allure.step("Нажатие кнопки входа"):
            self.find_element(LoginLocator.LOGIN_BUTTON).click()
