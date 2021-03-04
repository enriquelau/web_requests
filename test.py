import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from urllib3.exceptions import NewConnectionError
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
URL = 'https://www.speer.com/ammunition/handgun/lawman_handgun_training/19-53651.html'
driver = webdriver.Chrome(ChromeDriverManager().install())
quantity = "40"
userEmail = "enriquelau@protonmail.com"
password = "b%f)itq+wTZNRZN6=DT)zA:F"
creditCard = "372653830681009"
cardMonth = "08"
cardYear = "2025"
cardSecurityCode = "8636"

def check_status(get_status):
    while True:
        if get_status == "Currently Unavailable":
            time.sleep(5)
            driver.refresh()
        elif get_status == "Available":
            print('In stock')

def begin_purchase():
    try:
        driver.get(URL)
        get_status = driver.find_element_by_class_name("availability.product-availability").text
        check_status(get_status)
    except (NoSuchElementException, NewConnectionError):
        time.sleep(5)

begin_purchase()

