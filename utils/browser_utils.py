from selenium import webdriver

def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
