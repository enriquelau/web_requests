import requests
from bs4 import BeautifulSoup as bs

session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/83.0.4103.116 Safari/537.36"}

def add_to_cart():
    global session
    endpoint = "https://www.speer.com/ammunition/handgun/lawman_handgun_training/19-53919.html"
    payload = {
        "pid":"19-53919",
        "quantity":"3",
        "options":'%%5B%%5D'
    }
    response = session.post(endpoint, data=payload)

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
