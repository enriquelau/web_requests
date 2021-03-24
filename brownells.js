from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Users\dev\Downloads\geckodriver-v0.29.0-win64\geckodriver.exe')

driver.get('https://www.brownells.com/%27)

# driver.get('https://www.google.com/%27)

with open('fetch.js', 'r') as file: 
    data = file.read().replace('\n', '')
    driver.execute_script(data)
[12:24 AM]
fetch("https://www.brownells.com/asmx/BrownellsWebService_Google360.asmx/ProductDetail?1613706595327", {
  "headers": {
    "accept": "application/json, text/javascript, /; q=0.01",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json; charset=UTF-8",
    "km": "7oo7dl5j5",
    "sec-ch-ua": ""Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "securityticket": "ae260b93-3976-4938-9d3a-30cc7bd4fa77",
    "ts": "1613706595327"
  },
  "referrer": "https://www.brownells.com/ammunition/rifle-ammo/x-tac-5-56mm-nato-rifle-ammo-prod96174.aspx?avs%7cCartridge_1=AKK_5xzzx56+mm+NATO",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "{"pid":96174}",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
}).then(res => res.json()).then(data => {


  console.log(data)
  let x = JSON.parse(data.d)
  let status = x.Data.productDetails.stockStatus

console.log(status)


});
