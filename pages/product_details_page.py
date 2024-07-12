from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductDetailsPage(BasePage):
    QUANTITY_FIELD = (By.ID, "product_enteredQuantity_20")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button-20")

    def set_quantity(self, quantity):
        quantity_field = self.wait_for_element(self.QUANTITY_FIELD)
        quantity_field.clear()
        quantity_field.send_keys(str(quantity))

    def add_to_cart(self):
        self.wait_for_element(self.ADD_TO_CART_BUTTON).click()
