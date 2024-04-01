import allure
from datetime import datetime
import pytest
from web.utils import WebDriverManager


@pytest.fixture(scope="session")
def chrome_driver():
    driver = WebDriverManager.get_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def set_up_time():
    with allure.step('Время старта теста'):
        allure.attach(body=f"время начала теста: {datetime.now()}", name="Время начала теста", attachment_type=allure.attachment_type.TEXT)
    yield
    with allure.step("Время завершения теста"):
        allure.attach(body=f"время завершения теста: {datetime.now()}", name="Время завершения теста", attachment_type=allure.attachment_type.TEXT)