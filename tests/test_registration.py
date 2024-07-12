import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import pytest
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utils.browser_utils import initialize_driver
from utils.constants import BASE_URL
pytestmark = pytest.mark.skip(reason="Skipping registration tests")
@pytest.fixture
def driver():
    driver = initialize_driver()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.mark.order(1)
@pytest.mark.parametrize("gender, first_name, last_name,DOB_day,DOB_Month,DOB_year, email, company, newsletter, password, expected_message", [
    ("Male", "John", "Doe","12","October","1996", "cal4@example.com", "California", True, "pass@1234", "Your registration completed"),
    
])

def test_registration(driver, gender, first_name, last_name,DOB_day,DOB_Month,DOB_year,email, company, newsletter, password, expected_message):
    home_page = HomePage(driver)
    time.sleep(2)
    registration_page = RegistrationPage(driver)
    time.sleep(2)
    home_page.go_to_registration_page()
    time.sleep(2)
    registration_page.select_gender(gender)
    time.sleep(2)
    registration_page.set_first_name(first_name)
    time.sleep(2)
    registration_page.set_last_name(last_name)
    time.sleep(2)
    registration_page.set_DOB(DOB_day,DOB_Month,DOB_year)
    time.sleep(2)
    registration_page.set_email(email)
    time.sleep(2)
    registration_page.set_company(company)
    time.sleep(2)
    registration_page.set_newsletter(newsletter)
    time.sleep(2)
    registration_page.set_password(password)
    time.sleep(2)
    registration_page.click_register()
    time.sleep(2)

    assert registration_page.get_result_message() == expected_message
    time.sleep(2)
