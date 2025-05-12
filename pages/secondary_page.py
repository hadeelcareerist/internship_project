from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SecondaryPage(BasePage):
    SECONDARY_MENU = (By.XPATH, "//div[contains(text(), 'Secondary')]")
    FILTER_BTN = (By.XPATH, "//div[@wized='openFiltersWindow']")
    WANT_TO_BUY = (By.XPATH, "//div[@class='tag-text-filters' and text()='Want to buy']")
    APPLY_BTN = (By.CSS_SELECTOR, "[wized='applyFilterButtonMLS']")
    DEAL_CARDS = (By.CLASS_NAME, "listing-card")
    PAGE_TITLE = (By.CSS_SELECTOR, "div.page-title.listing")

    def click_secondary_option(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.SECONDARY_MENU)
        ).click()

    def verify_secondary_page_opens(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.PAGE_TITLE)
        )

    def click_filter(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.FILTER_BTN)
        ).click()

    def filter_products_by_want_to_buy(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.WANT_TO_BUY)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_on_apply_filter(self):
        self.driver.find_element(By.CSS_SELECTOR, "[wized='applyFilterButtonMLS']").click()

    def verify_all_cards_have_want_to_buy_tag(self):
        cards = self.driver.find_elements(*self.DEAL_CARDS)
        for card in cards:
            tag = card.find_element(By.CSS_SELECTOR, "[wized='saleTagMLS']")
            assert "want to buy" in tag.text.lower()
