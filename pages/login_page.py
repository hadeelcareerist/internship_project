from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.EMAIL = (By.NAME, "email-2")
        self.PASSWORD = (By.ID, "field")
        self.LOGIN_BTN = (By.XPATH, "//a[text()='Continue']")

    def log_in_to_the_page(self, email, password):
        wait = WebDriverWait(self.driver, 20)

        email_field = wait.until(EC.presence_of_element_located(self.EMAIL))
        email_field.clear()
        email_field.send_keys(email)

        password_field = wait.until(EC.presence_of_element_located(self.PASSWORD))
        password_field.clear()
        password_field.send_keys(password)

        login_button = wait.until(EC.element_to_be_clickable(self.LOGIN_BTN))
        login_button.click()

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Secondary')]")))