from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import Select
import time


class CheckoutPage(BasePage):
    CHECKOUT_AS_GUEST_BUTTON = (By.XPATH, "//button[contains(text(),'Checkout as Guest')]")
    BILLING_FIRST_NAME = (By.ID, "BillingNewAddress_FirstName")
    BILLING_LAST_NAME = (By.ID, "BillingNewAddress_LastName")
    BILLING_EMAIL = (By.ID, "BillingNewAddress_Email")
    BILLING_COMPANY = (By.ID, "BillingNewAddress_Company")
    BILLING_COUNTRY = (By.ID, "BillingNewAddress_CountryId")
    BILLING_STATE=(By.ID,"BillingNewAddress_StateProvinceId")
    BILLING_CITY = (By.ID, "BillingNewAddress_City")
    BILLING_ADDRESS1 = (By.ID, "BillingNewAddress_Address1")
    BILLING_ZIP_POSTAL_CODE = (By.ID, "BillingNewAddress_ZipPostalCode")
    BILLING_PHONE_NUMBER = (By.ID, "BillingNewAddress_PhoneNumber")
    BILLING_CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[name='save']")
    SHIPPING_METHOD_CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[name='save-shipping-method']")
    PAYMENT_METHOD_CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[name='save-payment-method']")
    PAYMENT_INFO_CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[name='save-payment-info']")
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, "button[name='confirm-order']")

    def checkout_as_guest(self):
        self.wait_for_element(self.CHECKOUT_AS_GUEST_BUTTON).click()

    def enter_billing_details(self, fName, lName, email, company, country,state, city, address1, zip, phone):
        self.wait_for_element(self.BILLING_FIRST_NAME).send_keys(fName)
        self.wait_for_element(self.BILLING_LAST_NAME).send_keys(lName)
        self.wait_for_element(self.BILLING_EMAIL).send_keys(email)
        self.wait_for_element(self.BILLING_COMPANY).send_keys(company)
        #self.wait_for_element(self.BILLING_COUNTRY).send_keys(country)
        # Select country from dropdown (implement dropdown selection logic)
        #self.wait_for_element(self.BILLING_COUNTRY).select.select_by_visible_text(country)
        dropdown_element = self.wait_for_element(self.BILLING_COUNTRY)
        time.sleep(3)
        # Create a Select object
        select = Select(dropdown_element)
        time.sleep(4)
        # Select the country by visible text
        select.select_by_visible_text(country)
        dropdown_state = self.wait_for_element(self.BILLING_STATE)
        time.sleep(3)
        # Create a Select object
        select = Select(dropdown_state)
        time.sleep(3)
        # Select the country by visible text
        select.select_by_visible_text(state)
        self.wait_for_element(self.BILLING_CITY).send_keys(city)
        self.wait_for_element(self.BILLING_ADDRESS1).send_keys(address1)
        self.wait_for_element(self.BILLING_ZIP_POSTAL_CODE).send_keys(zip)
        time.sleep(3)
        self.wait_for_element(self.BILLING_PHONE_NUMBER).send_keys(phone)
        self.wait_for_element(self.BILLING_CONTINUE_BUTTON).click()
        time.sleep(10)

    def select_shipping_method(self):
        # Assuming Next Day Air is already selected
        self.wait_for_element(self.SHIPPING_METHOD_CONTINUE_BUTTON).click()

    def select_payment_method(self):
        # Assuming Credit Card is already selected
        self.wait_for_element(self.PAYMENT_METHOD_CONTINUE_BUTTON).click()

    def enter_credit_card_details(self, cardType, holderName, number, expMonth, expYear, code):
        # Implement dropdown selection logic for card type, month, and year
        self.wait_for_element(self.BILLING_FIRST_NAME).send_keys(holderName)
        self.wait_for_element(self.BILLING_LAST_NAME).send_keys(number)
        # self.select_dropdown_value(self.CREDIT_CARD_TYPE, cardType)
        # self.select_dropdown_value(self.EXPIRE_MONTH, expMonth)
        # self.select_dropdown_value(self.EXPIRE_YEAR, expYear)
        self.wait_for_element(self.BILLING_ZIP_POSTAL_CODE).send_keys(code)
        self.wait_for_element(self.PAYMENT_INFO_CONTINUE_BUTTON).click()

    def confirm_order(self):
        self.wait_for_element(self.CONFIRM_ORDER_BUTTON).click()
