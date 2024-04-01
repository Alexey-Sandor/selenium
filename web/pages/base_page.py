from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from web.utils import Config


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Config.BASE_URL

    def find_element(self, locator, time=10):
        with allure.step(f"Click on {locator}"):
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator)
            )
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator), message="Element not found"
            )

    def find_elements(self, locator, time=10):
        with allure.step(f"Click on {locator}"):
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator),
                message=f"Can't find element by {locator}",
            )

    def go_to_site(self):
        return self.driver.get(self.url)

    def invisibility_of_element_located(self, locator, time=10):
        with allure.step(f"nono"):
            return WebDriverWait(self.driver, time).until(
                EC.invisibility_of_element_located(locator), message="Element not found"
            )
