import requests
from bs4 import BeautifulSoup as soup


#TargetSports USA test URL

#If item in stock, sign in with username and password, then proceed to checkout. 

#Winchester 9mm 147 Test, adding to cart. 
#  https://www.targetsportsusa.com/x-compunix.minicart.aspx?itemadded=1&_=1630036460261

#Save the cookie, in this step?

#Checkout https://www.targetsportsusa.com/signin.aspx?checkout=true

def inventoryChecker():
    url = 'https://www.targetsportsusa.com/winchester-usa-9mm-luger-ammo-147-grain-jacketed-hollow-point-usa9jhp2-p-2137.aspx'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " "Chrome/83.0.4103.116 Safari/537.36"}
    req = requests.get(url, headers=headers)
    print(req.text)
    pass
def signIn():
    payload = {user: password}
    pass
def purchase():
    pass
inventoryChecker()
