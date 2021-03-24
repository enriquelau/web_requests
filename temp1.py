#from bs4 import BeautifulSoup
import requests


session = requests.Session()
url = 'https://www.speer.com/on/demandware.store/Sites-VistaSpeer-Site/default/Cart-AddProduct'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/83.0.4103.116 Safari/537.36"}
payload = {"pid":"19-53919","quantity":"1"}
add_to_cart = requests.post(url,headers=headers,data=payload)

'''
It seems to work, although I would like another way to verify. 
Possibly print out or screenshot the contents, to verify. 
This is only for testing. 

'''
print(add_to_cart.content)




#def add_to_cart():
    
