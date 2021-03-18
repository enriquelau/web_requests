import requests
from bs4 import BeautifulSoup as bs

'''
session = requests.Session()
print(session.cookies.get_dict())

response = session.get('https://speer.com')
print(session.cookies.get_dict())
print(response.status_code)
'''

session = requests.Session()
response = session.get('https://www.reddit.com/r/InStockAmmo/new/')
print(response.text)

# http_site="https://www.reddit.com/r/InStockAmmo/new/"
#soup = bs(http_site, 'html.parser')

# print(soup.prettify)
