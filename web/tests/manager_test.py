import pytest
import allure



class BaseTest:
    @staticmethod
    def handle_assertion_error(chrome_driver, error_message):
        with allure.step("Поймали ошибку"):
            allure.attach(
                chrome_driver.get_screenshot_as_png(),
                name="screenshot.png",
                attachment_type=allure.attachment_type.PNG,
            )
            raise AssertionError(error_message)

