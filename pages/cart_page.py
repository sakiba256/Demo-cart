from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    SHOPPING_CART=(By.LINK_TEXT,"Shopping cart")
    TERMS_OF_SERVICE_CHECKBOX = (By.ID, "termsofservice")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def accept_terms_and_checkout(self):
        self.wait_for_element(self.SHOPPING_CART).click()
        self.wait_for_element(self.TERMS_OF_SERVICE_CHECKBOX).click()
        self.wait_for_element(self.CHECKOUT_BUTTON).click()
