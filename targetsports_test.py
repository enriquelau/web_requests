from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from urllib3.exceptions import NewConnectionError
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from random import randint
import time
import sys
from decouple import config

# blazer_brass_124 = 'https://www.targetsportsusa.com/cci-blazer-brass-9mm-luger-ammo-124-grain-full-metal-jacket-5201-p-4172.aspx'
quantity = "4"
userEmail = config('targetUserEmail')
userPass = config('targetPassword')
driver = webdriver.Chrome(ChromeDriverManager().install())

# Test website
blazer_brass_124 = "https://www.targetsportsusa.com/federal-ae-357-sig-125-gr-ammo-fmj-ae357s2-p-1716.aspx"

def sleep(secs):
    time.sleep(secs)


def check_status(get_status):
    status: object = get_status
    while True:
        if status == "OUT OF STOCK":
            sleep(randint(5,15))
            driver.refresh()
        elif status == "AVAILABLE :":
            # Here is where some logic will need to be added
            # to pause the VPN change service
            print("Product Available, checking inventory levels:")
            continue


def inventory_check():
    driver.find_element_by_xpath(
        "/html/body/form/main/div/div[1]/div[1]/div[3]/div[2]/div[1]/select/option[3]").click()
    driver.find_element_by_xpath(
        "/html/body/form/main/div/div[1]/div[1]/div[3]/div[2]/vinv[2]/div/div[2]/div/span[1]/input[1]")
    inventory = driver.find_element_by_css_selector(
        "html body#product-page.master form#aspnetForm main div#ctl00_PageContent_pnlContent div "
        "div#product.product.common div.product-info div.product-options vinv.vinv_2629 div.product-stock "
        "div.stock-info").text
    stock = int(inventory[12] + inventory[13])
    if stock > 15:
        print("Checking out")
    elif stock < 15:
        sys.exit("Insufficient stock")
        return



def get_url():
    tries = 0
    while tries < 8:
        try:
            driver.get(blazer_brass_124)
            # sleep(0.5)
            get_status = driver.find_element_by_css_selector(
                "#product > div.product-info > div.product-options > vinv.vinv_6632 > div > div.stock-info").text
            print(get_status)
            check_status(get_status)
            break
        except Exception as e:  # (NoSuchElementException,NewConnectionError,WebDriverException,ConnectionError,StaleElementReferenceException):
            print(e)
            sleep(4)
            tries += 1
            continue
    process_purchase()


def process_purchase():
    try:
        # Selects the 1000 round case option
        select = driver.find_element_by_xpath(
            "/html/body/form/main/div/div[1]/div[1]/div[3]/div[2]/div[1]/select/option[3]").click()

        sleep(0.5)

        # Calling inventory check to asses stock level to proceed. 

        inventory_check()

        search = driver.find_element_by_xpath(
            "/html/body/form/main/div/div[1]/div[1]/div[3]/div[2]/vinv[2]/div/div[2]/div/span[1]/input[1]")
        search.send_keys(Keys.BACK_SPACE)
        sleep(0.2)
        search.send_keys(quantity)
        search.send_keys(Keys.RETURN)

        # Adding product to the cart
        sleep(0.5)
        driver.find_element_by_xpath(
            "/html/body/form/main/div/div[1]/div[1]/div[3]/div[2]/vinv[2]/div/div[2]/div/span[3]/input").click()

        # Going to shopping cart
        sleep(0.5)
        driver.get("https://www.targetsportsusa.com/shoppingcart.aspx")

        # Clicking the Checkout Now button
        sleep(0.5)
        driver.find_element_by_xpath("/html/body/form/main/div/div/div[4]/div[2]/input[2]").click()

        # Logging in for checkout
        sleep(0.5)
        driver.find_element_by_class_name("form-control.signinEmail").send_keys(userEmail)
        driver.find_element_by_xpath(
            "/html/body/form/main/div[1]/div/div/table/tbody/tr/td/div/div[1]/div[3]/input").send_keys(userPass)

        sleep(0.5)
        # Clicking the login button
        driver.find_element_by_class_name("button.call-to-action.login-button").click()

        sleep(0.5)
        # Button to place an order
        # driver.find_element_by_class_name("button.call-to-action.checkoutprocess-placeorder").click()
    except Exception as e:
        print(e)
        return

get_url()
