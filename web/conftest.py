import pytest
from web.utils import WebDriverManager


@pytest.fixture(scope="session")
def chrome_driver():
    driver = WebDriverManager.get_driver()
    yield driver
    driver.quit()

