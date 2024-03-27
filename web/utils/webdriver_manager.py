from selenium import webdriver


class WebDriverManager:
    @staticmethod
    def get_driver():
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        return driver
