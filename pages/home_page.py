from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    REGISTER_LINK = (By.LINK_TEXT, "Register")
    CATEGORY_LINK = (By.LINK_TEXT, "Electronics")
    PRODUCT_LINK = (By.LINK_TEXT, "Cell phones")
    MODEL_LINK=(By.LINK_TEXT, "Nokia Lumia 1020")

    def go_to_registration_page(self):
        self.wait_for_element(self.REGISTER_LINK).click()

    def navigate_to_category(self):
        self.wait_for_element(self.CATEGORY_LINK).click()
        self.wait_for_element(self.PRODUCT_LINK).click()

    def select_product(self):
        self.wait_for_element(self.MODEL_LINK).click()
