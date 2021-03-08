import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from urllib3.exceptions import NewConnectionError
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager

# blazer_brass_124 = 'https://www.targetsportsusa.com/cci-blazer-brass-9mm-luger-ammo-124-grain-full-metal-jacket-5201-p-4172.aspx'
quantity = "4"
userEmail = "le1952@protonmail.com"
userPass = "cZ2HyhARVft9h}Qt;$m"
driver = webdriver.Chrome(ChromeDriverManager().install())
cardMonth = "08"
cardYear = "2025"
cardSecurityCode = "8636"

#Test website
blazer_brass_24 = driver.get("https://www.targetsportsusa.com/federal-ae-357-sig-125-gr-ammo-fmj-ae357s2-p-1716.aspx")
# blazer_brass_124 = 'https://www.targetsportsusa.com/cci-blazer-brass-9mm-luger-ammo-124-grain-full-metal-jacket-5201-p-4172.aspx'
    #Trying to get the text that reads what is out of stock.

    # Need to add a while loop to check in stock
def sleep(secs):
    time.sleep(secs)


def check_status(get_status):
    status: object = get_status
    while True:
        if status == "OUT OF STOCK":
            sleep(5)
            driver.refresh()
        else:
            process_purchase()

def get_url():
    tries = 0
    while tries < 8:
        try:
            driver.get(blazer_brass_124)
            #sleep(0.5)
            get_status = driver.find_element_by_css_selector("#product > div.product-info > div.product-options > vinv.vinv_6632 > div > div.stock-info").text
            check_status(get_status)
            break
        except[NoSuchElementException,NewConnectionError,WebDriverException,ConnectionError,StaleElementReferenceException,Exception]:
            sleep(1)
            tries += 1
            continue

def process_purchase():
    while True:

        #Selects the 1000 round case option
        select = driver.find_element_by_xpath("/html/body/form/main/div/div[1]/div[1]/div[3]/div[2]/div[1]/select/option[3]").click()

        time.sleep(0.5)

        #Enters the quantity to purchase
        search = driver.find_element_by_xpath("/html/body/form/main/div/div[1]/div[1]/div[3]/div[2]/vinv[2]/div/div[2]/div/span[1]/input[1]")
        search.send_keys(Keys.BACK_SPACE)
        time.sleep(0.2)
        search.send_keys(quantity)
        search.send_keys(Keys.RETURN)

        #Adding product to the cart
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/form/main/div/div[1]/div[1]/div[3]/div[2]/vinv[2]/div/div[2]/div/span[3]/input").click()

        #Going to shopping cart
        time.sleep(0.5)
        driver.get("https://www.targetsportsusa.com/shoppingcart.aspx")

        #Clicking the Checkout Now button
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/form/main/div/div/div[4]/div[2]/input[2]").click()

        #Logging in for checkout
        time.sleep(0.5)
        driver.find_element_by_class_name("form-control.signinEmail").send_keys(userEmail)
        driver.find_element_by_xpath("/html/body/form/main/div[1]/div/div/table/tbody/tr/td/div/div[1]/div[3]/input").send_keys(userPass)

        time.sleep(0.5)
        #Clicking the login button
        driver.find_element_by_class_name("button.call-to-action.login-button").click()

        time.sleep(0.5)
        #Button to place an order
        #driver.find_element_by_class_name("button.call-to-action.checkoutprocess-placeorder").click()

get_url()