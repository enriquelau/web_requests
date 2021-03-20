import requests
from bs4 import BeautifulSoup as bs

session = requests.Session()


def add_to_cart():
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/83.0.4103.116 Safari/537.36"}
    global session
    endpoint = "https://www.speer.com/on/demandware.store/Sites-VistaSpeer-Site/default/Product-Inventory?pid=19-53919&qty=1"
    response = session.get(endpoint)
    print (response.text)
add_to_cart()


'''
def get_stock():
    global session
    endpoint = 'https://www.speer.com/ammunition/handgun/lawman_handgun_training/19-53919.html'
    response = session.get(endpoint)

    soup = bs(response.text,"html.parser")
    
    div = soup.find("div",)
 print(response.status_code)
'''
