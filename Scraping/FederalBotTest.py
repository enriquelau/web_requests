import requests
from bs4 import BeautifulSoup as bs

headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/83.0.4103.116 Safari/537.36"}

url = 'https://www.federalpremium.com/handgun/american-eagle/american-eagle-handgun/11-AE5728A.html'

result = requests.get(url, headers=headers)

#with open("bestbuy.html", "r") as f:
#document = bs(f, 'html.parser')
#print(document.prettify())    

document = bs(result.text, "html.parser")
#tags = document.find_all(["div"])
tags = document.find_all("div")
print(result.text)

'''
url = 'bestbuy.html'
result = requests.get(url, headers=headers)
document = bs(result.text, "html.parser")
print(document.prettify)
'''
