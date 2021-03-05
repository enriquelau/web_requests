import time
# import speer_purchase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys
from urllib3.exceptions import NewConnectionError
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager

#url = 'https://www.speer.com/ammunition/handgun/lawman_handgun_training/19-53651.html'
url = 'https://www.speer.com/ammunition/handgun/lawman_handgun_training/19-53919.html'

driver = webdriver.Chrome(ChromeDriverManager().install())
quantity = "40"
userEmail = "enriquelau@protonmail.com"
password = "b%f)itq+wTZNRZN6=DT)zA:F"
creditCard = "372653830681009"
cardMonth = "08"
cardYear = "2025"
cardSecurityCode = "8636"


def sleep(secs):
    time.sleep(secs)


def check_status(get_status):
    status: object = get_status
    while True:
        if status == "Currently Unavailable":
            sleep(5)
            driver.refresh()
        elif status == "Available":
            # Code or function comes in here to proceed to checkout
            return status


def process_purchase():
    driver.find_element_by_class_name("decline.btn.btn-primary").click()


def get_url():
    try:
        driver.get(url)
        get_status = driver.find_element_by_class_name("availability.product-availability").text
        check_status(get_status)
    except(NoSuchElementException, NewConnectionError, WebDriverException):
        sleep(3)
    process_purchase()


get_url()
