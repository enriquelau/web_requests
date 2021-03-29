import requests
from bs4 import BeautifulSoup as bs
import RandomHeaders

url = 'https://ammoseek.com/ammo/9mm-luger'


def headers():
    header = RandomHeaders.LoadHeader() 
    return header


def get_page_html(url):
    page = requests.get(url, headers=headers())
    return 

def price():
    soup = bs(get_page_html(url), 'html.parser')
    price_check = soup.find("div", {"class": "results-info-content"})
    return price_check


def check_price():
    page_html = get_page_html(url)
    print(price())
    
check_price()
