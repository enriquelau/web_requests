import requests
import lxml
from bs4 import BeautifulSoup as bs
import RandomHeaders

URL = 'https://ammoseek.com/ammo/9mm-luger'

def headers():
    header = RandomHeaders.LoadHeader() 
    return header

def get_page_url(URL):
    res = requests.get(URL, headers=headers())
    return res.content

def parcing_price(page_html):
    soup = bs(page_html, 'html.parser')
    price = soup.find_all("div", {"class": "results-info-content"})
    print(price)
    return price

def check_price():
    page_html = get_page_url(URL)
    temp = parcing_price(page_html)
    print('temp')

check_price()
