import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage


class OrderLocator:
    FIRST_NAME_INPUT = ('xpath', "//input[@name='firstName']")
    LAST_NAME_INPUT = ('xpath', "//input[@name='lastName']")
    POSTAL_CODE_INPUT = ('xpath', "//input[@name='postalCode']")
    CONTINUE_UNPUT = ('xpath', "//input[@name='continue']")
    FINISH_BUTTON = ('xpath', "//button[@name='finish']")

class OrderPage(BasePage):
    def fill_in_the_form(self, first_name, last_name, postal_code):
        with allure.step(f"Вводим имя"):
            self.find_element(OrderLocator.FIRST_NAME_INPUT).send_keys(first_name)
        with allure.step(f"Вводим фамилию"):
            self.find_element(OrderLocator.LAST_NAME_INPUT).send_keys(last_name)
        with allure.step("Вводим почтовый индекс"):
            self.find_element(OrderLocator.POSTAL_CODE_INPUT).send_keys(postal_code)
        with allure.step("Переходит к следующему шагу оформления заказа"):
            self.find_element(OrderLocator.CONTINUE_UNPUT).click()

    def click_finish_button(self):
        with allure.step("Завершаем оформление заказа"):
            self.find_element(OrderLocator.FINISH_BUTTON).click()