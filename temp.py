from bs4 import BeautifulSoup as bs
import requests

'''
Today's lesson: 

1. Need to store the cookie sessions to make the session persist for checkout. 
2. Need to implement a way to hold the csrf token, which will require a function 
   that will obtain it and keep it alive for the checkout process. 

'''
url = 'https://www.speer.com/bullets/handgun_bullets/gold_dot_handgun_component_bullet/19-3985.html'
session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/83.0.4103.116 Safari/537.36"}


# This will be the function that will save initial cookie, possibly?
# May need another one for the csrf cookie session. 
def initiate():
    global session
    response = session.get(url)
    print(response.text)


def add_to_cart():
    return
    #global session 
    #adding to cart with the below post request
    #payload = {"pid":"19-53919","quantity":"3"}
    #requests.post(url,headers=headers,data=payload)
    #print(initiate(response))

'''
soup = bs(response.text,"html.parser")
r = requests.get("https://www.speer.com/on/demandware.store/Sites-VistaSpeer-Site/default/Cart-CheckShippingRestrictions?stateCode=TX")
'''

# account_creds = {}


# Login for checkout

'''
It seems to work, although I would like another way to verify. 
Possibly print out or screenshot the contents, to verify. 
This is only for testing. 

'''
# checkState = ''


#def add_to_cart():
initiate() 
