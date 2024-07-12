from selenium.webdriver.common.by import By
from .base_page import BasePage

class OrderConfirmationPage(BasePage):
    ORDER_CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, "div.title strong")

    def get_order_confirmation_message(self):
        return self.wait_for_element(self.ORDER_CONFIRMATION_MESSAGE).text
