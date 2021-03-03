from bs4 import BeautifulSoup
import requests
import time


# The next assignment is to get the item into the cart.
def purchase():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/83.0.4103.116 Safari/537.36"}
    with requests.Session() as s:
        url = "https://www.speer.com/ammunition/handgun/lawman_handgun_training/19-53919.html"
        r = s.get()
        print
    return


def get_page_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    print(page.status_code)
    return page.content


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_div = soup.find("div", {"class": "label-1"})
    return out_of_stock_div.text


def check_inventory():
    while True:
        # These are test websites, some with product and others with none.
        # url = "https://www.federalpremium.com/handgun/american-eagle/american-eagle-handgun/11-AE9AP.html"
        # url = "https://www.federalpremium.com/handgun/premium-handgun-hunting/swift-a-frame/11-P500SA.html"
        # url = "https://www.speer.com/ammunition/handgun/lawman_handgun_training/19-53919.html"
        url = "https://www.speer.com/ammunition/handgun/lawman_handgun_training/19-53651.html"
        page_html = get_page_html(url)
        # The conditional below is checking to see if the string
        # "Currently Unavailable" exists in the html that was parsed with the check_item_in_stock method"
        if "Available" in check_item_in_stock(page_html):
            print("In Stock")
            time.sleep(5)
        else:
            print("OOS")
            time.sleep(5)


check_inventory()
purchase()
# next steps
# create a session, send a post request, login to the website.
