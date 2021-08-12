import smtplib
from email.message import EmailMessage
import requests as req
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from urllib3.exceptions import NewConnectionError
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from decouple import config

url = 'https://hkparts.net/product/9mm-ejector-lever-3rd-gen-p58.htm/'

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
quantity = "4"
userEmail = config('federalUserEmail')
password = config('federalPassword')
creditCard = config('creditCard')
cardMonth = config('cardMonth')
cardYear = config('cardYear')
cardSecurityCode = config('cardSecurityCode')

def sleep(secs):
    time.sleep(secs)

def check_status(get_status):
    status = get_status
    while True:
        if status == "Out of stock":
            print('Out of stock')
            sleep(5)
            driver.delete_all_cookies()
            sleep(1)
            email_alert("In stock - HK Parts Lever", "https://hkparts.net/product/9mm-ejector-lever-3rd-gen-p58.htm/", "le1952@protonmail.com")
            driver.refresh()
        elif status == "In stock":
            email_alert("In stock - HK Parts Lever", "https://hkparts.net/product/9mm-ejector-lever-3rd-gen-p58.htm/", "le1952@protonmail.com")
            return

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "enrique.a.lau@gmail.com"
    msg['from'] = user
    password = 'rmqkcxjsigwcoqnn'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    return
    
def get_url():
    tries = 0
    while tries < 8:
        try:
            driver.get(url)
            get_status = driver.find_element_by_xpath("/html/body/div[3]/div[5]/div[1]/main/div[3]/div[2]/p[2]").text
            check_status(get_status)
            break
        except[NoSuchElementException, NewConnectionError, WebDriverException, ConnectionError,
               StaleElementReferenceException]:
            sleep(1)
            tries += 1
            continue

get_url()
