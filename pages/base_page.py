from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(locator)).click()

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)


