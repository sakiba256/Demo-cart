from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class RegistrationPage(BasePage):
    GENDER_MALE = (By.ID, "gender-male")
    GENDER_FEMALE = (By.ID, "gender-female")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    DOB_DAY=(By.NAME,"DateOfBirthDay")
    DOB_MONTH=(By.NAME,"DateOfBirthMonth")
    DOB_YEAR=(By.NAME,"DateOfBirthYear")
    EMAIL = (By.ID, "Email")
    COMPANY = (By.ID, "Company")
    NEWSLETTER = (By.ID, "Newsletter")
    PASSWORD = (By.ID, "Password")
    CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")
    RESULT_MESSAGE = (By.CLASS_NAME, "result")

    def select_gender(self, gender):
        if gender == "Male":
            self.wait_for_element(self.GENDER_MALE).click()
        else:
            self.wait_for_element(self.GENDER_FEMALE).click()

    def set_first_name(self, first_name):
        self.wait_for_element(self.FIRST_NAME).send_keys(first_name)

    def set_last_name(self, last_name):
        self.wait_for_element(self.LAST_NAME).send_keys(last_name)

    def set_DOB(self, day,month,year):
        self.wait_for_element(self.DOB_DAY).send_keys(day)
        time.sleep(2)
        self.wait_for_element(self.DOB_MONTH).send_keys(month)
        time.sleep(2)
        self.wait_for_element(self.DOB_YEAR).send_keys(year)

    def set_email(self, email):
        self.wait_for_element(self.EMAIL).send_keys(email)

    def set_company(self, company):
        self.wait_for_element(self.COMPANY).send_keys(company)

    def set_newsletter(self, status):
        checkbox = self.wait_for_element(self.NEWSLETTER)
        if checkbox.is_selected() != status:
            checkbox.click()

    def set_password(self, password):
        self.wait_for_element(self.PASSWORD).send_keys(password)
        self.wait_for_element(self.CONFIRM_PASSWORD).send_keys(password)

    def click_register(self):
        self.wait_for_element(self.REGISTER_BUTTON).click()

    def get_result_message(self):
        return self.wait_for_element(self.RESULT_MESSAGE).text
