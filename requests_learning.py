import requests
from bs4 import BeautifulSoup as bs

session = requests.Session()
print(session.cookies.get_dict())
response = session.get('https://speer.com')
print(session.cookies.get_dict())
print(response.status_code)


