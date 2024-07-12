import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_confirmation_page import OrderConfirmationPage
from utils.browser_utils import initialize_driver
from utils.constants import BASE_URL
import time
@pytest.fixture
def driver():
    driver = initialize_driver()
    driver.get(BASE_URL)
    yield driver
    driver.quit()
@pytest.mark.order(2)
def test_place_order(driver):
    home_page = HomePage(driver)
    product_details_page = ProductDetailsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    order_confirmation_page = OrderConfirmationPage(driver)

    home_page.navigate_to_category()
    time.sleep(2)
    home_page.select_product()
    time.sleep(2)
    product_details_page.set_quantity(2)
    time.sleep(2)
    product_details_page.add_to_cart()
    time.sleep(2)
    cart_page.accept_terms_and_checkout()
    time.sleep(2)
    checkout_page.checkout_as_guest()
    time.sleep(2)
    checkout_page.enter_billing_details("John", "Doe", "john.do@example.com", "Cal", "United States", "American Samoa","Australia", "123 Main St", "10001", "+8801767878787")
    time.sleep(10)
    checkout_page.select_shipping_method()
    checkout_page.select_payment_method()
    checkout_page.enter_credit_card_details("Visa", "John Doe", "4111111111111111", "12", "2025", "123")
    checkout_page.confirm_order()

    assert order_confirmation_page.get_order_confirmation_message() == "Your order has been successfully processed!"
