import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from urllib3.exceptions import NewConnectionError
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
# url = 'https://www.federalpremium.com/rifle/premium-centerfire-rifle/swift-scirocco-ii/11-P270WSMSS1.html'
# url = 'https://www.federalpremium.com/rifle/american-eagle/american-eagle-rifle/11-AE300BLK1.html'
# url = 'https://www.federalpremium.com/handgun/american-eagle/american-eagle-handgun/11-AE45A100.html'
url = 'https://www.federalpremium.com/handgun/american-eagle/american-eagle-handgun/11-AE5728A.html'
driver = webdriver.Chrome(ChromeDriverManager().install())
quantity = "40"
userEmail = "enriquelau@protonmail.com"
password = "KqtLp2FW3xyFZme_gN_"
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
            return


def add_to_cart():
    attempts = 0
    for attempts in range(0, 6):
        try:
            adding_to_cart = driver.find_element_by_class_name("add-to-cart.btn.btn-primary")
            adding_to_cart.send_keys(Keys.RETURN)
            break
        except NoSuchElementException:
            print('No add to cart button found. Must be because the webpage has not completely loaded. Re-attempting '
                  'the process for five tries:' + attempts)
            sleep(0.5)
            attempts += 1
    get_url()


def process_purchase():
    try:
        driver.find_element_by_class_name("decline.btn.btn-primary").click()
        # Erasing the text field, replacing it with the desired quatity, and adding it to the shopping cart
        search = driver.find_element_by_class_name("form-control.quantity-select.quantity.quantity-input")
        search.send_keys(Keys.BACK_SPACE)
        sleep(0.2)
        search.send_keys(quantity)
        search.send_keys(Keys.RETURN)

        sleep(0.2)

        # Pressing the Add to Cart Button
        add_to_cart()

        # Takes you to the shopping cart for checkout
        driver.get("https://www.federalpremium.com/cart")
        sleep(0.8)
        # Selects the State
        driver.find_element_by_id("TX").click()
        sleep(0.2)
        # Will need to add a condition in case this path doesn't work try another
        applyState = driver.find_element_by_class_name("btn.btn-primary.btn-block.shipping-restrictions")
        applyState.send_keys(Keys.RETURN)
        sleep(0.4)
        driver.get(
            "https://www.federalpremium.com/on/demandware.store/Sites-VistaFederal-Site/default/Checkout-Login")
        # checkoutButton.send_keys(Keys.RETURN)

        sleep(0.4)

        # Login as a returning customer
        emailLogin = driver.find_element_by_id("login-form-email")
        emailLogin.send_keys(userEmail)
        passwordLogin = driver.find_element_by_id("login-form-password")
        passwordLogin.send_keys(password)

        sleep(0.4)

        # Pressing the login button
        pressLogin = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/button")
        pressLogin.send_keys(Keys.RETURN)

        sleep(0.8)
        # #The next step is to get this to press the "NEXT: VALIDATE ADDRESS BUTTON" The below isn't working so far.
        validateAddress = driver.find_element_by_class_name("btn.btn-primary.btn-block.submit-shipping")
        validateAddress.send_keys(Keys.RETURN)
        sleep(1)

        enterEmail = driver.find_element_by_class_name("form-control.email")
        enterEmail.send_keys(userEmail)

        sleep(1)

        creditCardNumber = driver.find_element_by_class_name("form-control.cardNumber")
        creditCardNumber.send_keys(creditCard)

        driver.find_element_by_id(cardMonth).click()
        driver.find_element_by_id(cardYear).click()

        securityCode = driver.find_element_by_class_name("form-control.securityCode")
        securityCode.send_keys(cardSecurityCode)

        reviewOrder = driver.find_element_by_class_name("btn.btn-primary.btn-block.submit-payment")
        reviewOrder.send_keys(Keys.RETURN)

        sleep(1)

        # Clicking the age verification box
        driver.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div[4]/div[1]/div[6]/div[3]/div/label").click()

        placeOrder = driver.find_element_by_class_name("btn.btn-primary.btn-block.place-order")
        placeOrder.send_keys(Keys.RETURN)

    except NoSuchElementException:
        pass


def get_url():
    tries = 0
    while tries < 8:
        try:
            driver.get(url)
            get_status = driver.find_element_by_class_name("availability.product-availability").text
            check_status(get_status)
            break
        except[NoSuchElementException, NewConnectionError, WebDriverException, ConnectionError,
               StaleElementReferenceException]:
            sleep(1)
            tries += 1
            continue
    process_purchase()


get_url()
