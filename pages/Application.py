from pages.login_page import LoginPage
from pages.secondary_page import SecondaryPage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.secondary_page = SecondaryPage(self.driver)

