from bs4 import BeautifulSoup
import requests
import sys
from os.path import join, dirname
from os import environ
from dotenv import load_dotenv
import time

# session global variable
# session automatically handles cookie management/passes cookies along with POST requests
session = requests.Session()


def get_page(url):
	return session.get(url).content


def check_item_in_stock(html, soup):
	# should find this particular parent class since there are other divs with class "label-1"; it could potentially lead to bugs
	# text also needs to be stripped
	in_stock = soup.find("ul", {"class": "list-unstyled availability-msg"}).find("div", {"class": "label-1"}).text.strip()

	if in_stock == 'Available':
		return True

	return False


def add_to_cart(pid):
	headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}

	# this needs to be properly encoded; test later if encoding with urllib.parse works
	# form_data = { 'pid': pid, 'quantity': quantity }

	response = session.post('https://www.speer.com/on/demandware.store/Sites-VistaSpeer-Site/default/Cart-AddProduct',
							data='pid=' + pid + '&quantity=' + str(quantity), headers=headers)

	if response.status_code == 200:
		return True

	else:
		print("Error adding to cart")
		return False


def get_state_restriction(shipping_info):

	url = "https://www.speer.com/on/demandware.store/Sites-VistaSpeer-Site/default/Cart-CheckShippingRestrictions" \
		  "?stateCode="+shipping_info["state"]

	response = session.get(url)

	if response.status_code == 200:
		# shipment UUID is in the json response from the server
		shipmentUUID = response.json().get('items')[0].get('shipmentUUID')
		return shipmentUUID

	else:
		print("Entered state is restricted")
		return False


def verify_state(shipmentUUID):
	url = "https://www.speer.com/on/demandware.store/Sites-VistaSpeer-Site/default/CheckoutShippingServices-UpdateShippingMethodsList?firstName=&lastName=&address1=&address2=&city=&postalCode=&stateCode=&countryCode=&phone=&shipmentUUID=" + shipmentUUID
	response = session.post(url)
	return response.status_code == 200


def verify_address(shipmentUUID):
	# use env variables in production
	# street address has double spaces for this request for some reason
	street = environ.get("STREET")
	street2 = environ.get("STREET2")

	url = "https://www.speer.com/on/demandware.store/Sites-VistaSpeer-Site/default/CheckoutShippingServices-UpdateShippingMethodsList?firstName=&lastName=&address1=" + street + "&address2="+street2+"&city=&postalCode=&stateCode=TX&countryCode=US&phone=&shipmentUUID=" + shipmentUUID
	response = session.post(url)
	return response.json()["shippingForm"]["valid"]


def get_csrf_token():
	response = session.get("https://www.speer.com/on/demandware.store/Sites-VistaSpeer-Site/default/Checkout-Begin")
	soup = BeautifulSoup(response.content, 'html.parser')
	try:
		#csrf_token is hidden in the "value" attribute of an input tag
		csrf_token = soup.find("input", {"name": "csrf_token"}).get("value")
		return csrf_token
	except:
		print("Error getting csrf token")
		return False


def build_shipping_info():
	# use environment variables for production;
	shipping_info = {"first_name": environ.get("FIRST_NAME"), "last_name": environ.get("LAST_NAME"),
					 "address": environ.get("STREET"), "address2": environ.get("STREET2"), "state": environ.get("STATE"),
					 "city": environ.get("CITY"), "zip": environ.get("ZIP"), "phone": environ.get("PHONE"),
					 "email": environ.get("EMAIL")
					 }

	#shipping_info = {"first_name": "John", "last_name": "John", "address": "9958+Twin+Shores+Dr", "city": "Willis", "state": "TX", "zip": "77318-6657", "phone": "4176447689", "email": "koyir39221%40zefara.com"}

	return shipping_info


def build_payment_info():
	# use env variables in production
	payment_info = {"cardType": environ.get("CARDTYPE"), "cardNumber": environ.get("CARDNUMBER"),
					 "expirationMonth": environ.get("EXPIRATIONMONTH"),
					 "expirationYear": environ.get("EXPIRATIONYEAR"), "securityCode": environ.get("SECURTYCODE")
					 }

	#payment_info = {"cardType": "Visa", "cardNumber": "4767718334205707", "expirationMonth": "4", "expirationYear": "2027", "securityCode": "170"}

	return payment_info


def submit_shipping(shipmentUUID, shipping_info, csrf_token):
	url = "https://www.speer.com/on/demandware.store/Sites-VistaSpeer-Site/default/CheckoutShippingServices-SubmitShipping"

	# build query string for post request
	query = "?originalShipmentUUID=" + shipmentUUID + \
			"&shipmentUUID=" + shipmentUUID + \
			"&shipmentSelector=new" \
			"&dwfrm_shipping_shippingAddress_addressFields_firstName=" + shipping_info["first_name"] + \
			"&dwfrm_shipping_shippingAddress_addressFields_lastName=" + shipping_info["last_name"] + \
			"&dwfrm_shipping_shippingAddress_addressFields_address1=" + shipping_info["address"] + \
			"&dwfrm_shipping_shippingAddress_addressFields_address2=" + shipping_info["address2"] + \
			"&dwfrm_shipping_shippingAddress_addressFields_country=US" \
			"&dwfrm_shipping_shippingAddress_addressFields_states_stateCode=" + shipping_info["state"] + \
			"&dwfrm_shipping_shippingAddress_addressFields_city=" + shipping_info["city"] + \
			"&dwfrm_shipping_shippingAddress_addressFields_postalCode=" + shipping_info["zip"] + \
			"&dwfrm_shipping_shippingAddress_addressFields_phone=" + shipping_info["phone"] + \
			"&dwfrm_shipping_shippingAddress_shippingMethodID=001" \
			"&dwfrm_shipping_shippingAddress_giftMessage=" \
			"&csrf_token=" + csrf_token

	response = session.post(url + query)

	# check if everything was properly validated
	if response.json()["form"]["valid"]:
		return True

	else:
		print("Error validating shipping information")
		return False


def submit_payment(shipping_info, payment_info, csrf_token):
	url = "https://www.speer.com/on/demandware.store/Sites-VistaSpeer-Site/default/CheckoutServices-SubmitPayment"

	# build query string for post request
	query = "?addressSelector=manual-entry&" \
			"dwfrm_billing_addressFields_firstName=" + shipping_info["first_name"] + \
			"&dwfrm_billing_addressFields_lastName=" + shipping_info["last_name"] + \
			"&dwfrm_billing_addressFields_address1=" + shipping_info["address"] + \
			"&dwfrm_billing_addressFields_address2=" + shipping_info["address2"] + \
			"&dwfrm_billing_addressFields_country=US" \
			"&dwfrm_billing_addressFields_states_stateCode=" + shipping_info["state"] + \
			"&dwfrm_billing_addressFields_city=" + shipping_info["city"] + \
			"&dwfrm_billing_addressFields_postalCode=" + shipping_info["zip"] + \
			"&csrf_token=" + csrf_token + \
			"&localizedNewAddressTitle=New+Address" \
			"&dwfrm_billing_contactInfoFields_email=" + shipping_info["email"] + \
			"&dwfrm_billing_contactInfoFields_phone=" + shipping_info["phone"] + \
			"&dwfrm_billing_paymentMethod=CREDIT_CARD" \
			"&dwfrm_billing_creditCardFields_cardType=" + payment_info["cardType"] + \
			"&dwfrm_billing_creditCardFields_cardNumber=" + payment_info["cardNumber"] + \
			"&dwfrm_billing_creditCardFields_expirationMonth=" + payment_info["expirationMonth"] + \
			"&dwfrm_billing_creditCardFields_expirationYear=" + payment_info["expirationYear"] + \
			"&dwfrm_billing_creditCardFields_securityCode=" + payment_info["securityCode"]

	response = session.post(url + query)

	# check the returned json if everything was properly validated
	if response.json()["form"]["valid"]:
		return True

	else:
		print("Error validating payment information")
		return False


def place_order():

	url = "https://www.speer.com/on/demandware.store/Sites-VistaSpeer-Site/default/CheckoutServices-PlaceOrder"
	response = session.post(url)
	# check the returned json if there was an error in placing the order

	if response.json()["error"]:
		return True

	else:
		print("Error with processing order")
		return False


def purchase(soup):
	# get product id from html
	pid = soup.find("div", {"class": "page"})['data-querystring'][4:]

	response = add_to_cart(pid)

	dotenv_path = join(dirname(__file__), '.env')
	load_dotenv(dotenv_path)

	# add to cart succesful
	if response:

		# create a dictionary with all the shipping info
		shipping_info = build_shipping_info()

		# a shipment UUID is generated once the shipping state is checked
		# function returns False if state check fails
		shipmentUUID = get_state_restriction(shipping_info)

		if shipmentUUID:

			# shipment UUID needs to get passed to the server afterwards; not sure what this accomplishes exactly
			# but it ostensibly verifies shipping state in the UI
			response = verify_state(shipmentUUID)

			if response:

				# address has to be verified to continue
				response = verify_address(shipmentUUID)

				if response:

					# csrf token is hidden in the html; this function gets the necessary html and pulls out the token
					csrf_token = get_csrf_token()

					# shipping information has to be validated; the shipment UUID and csrf token have to be passed
					# to the server as well for the validation to go through
					response = submit_shipping(shipmentUUID, shipping_info, csrf_token)

					if response:

						# create a dictionary with payment info
						payment_info = build_payment_info()
						# payment info has to be validated; csrf token is required for this step too
						response = submit_payment(shipping_info, payment_info, csrf_token)

						if response:
							# initiates the purchase; all the shipping and payment info is stored on the server,
							# so nothing is passed in this post request
							response = place_order()
							if response:
								print("Purchase declined")
							else:
								print("Purchase successful")


if __name__ == '__main__':

	# command line arguments can be accessed with sys.argv[n] where n is the nth argument
	# command line arguments start at 1, since sys.argv[0] is reserved for the name of script currently running

	if len(sys.argv) > 1:
		url = sys.argv[1]
		seconds = int(sys.argv[2])
		quantity = int(sys.argv[3])

	# default values if no command line arguments passed
	else:
		#url = "https://www.speer.com/ammunition/handgun/gold_dot_handgun_personal_protection/19-23970GD.html"
		url = "https://www.speer.com/ammunition/handgun/lawman_handgun_cleanfire_training/19-54232.html"
		seconds = 60
		quantity = 1

	# timed loop that sleeps for a certain amount of minutes before refreshing and checking if ammo in stock again
	while True:
		page = get_page(url)
		# optimization: should be initialized only once
		soup = BeautifulSoup(page, 'html.parser')
		if check_item_in_stock(page, soup):
			print("Item in stock -- starting purchase")
			purchase(soup)
			break
		time.sleep(seconds)
