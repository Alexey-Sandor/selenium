import pytest
from web.utils import WebDriverManager
from pytest_mock import MockerFixture

@pytest.fixture(scope="session")
def chrome_driver():
    driver = WebDriverManager.get_driver()
    yield driver
    driver.quit()

