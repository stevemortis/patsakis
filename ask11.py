import urllib.request
import requests
import json
url = "https://api.punkapi.com/v2/beers/random"
req = urllib.request.urlopen(url)
html = json.load(req)
for item in html:
	name1=(item['name'])
print("*H MPYRA APOSTELETAI STO e-MAIL SAS!*")	
def send_simple_message():
    return requests.post(
    	#Χρησιμοποιω το δικο μου mailgun account με τον οποιο στελνω το mail στο unipi@mailinator.com
        "https://api.mailgun.net/v3/sandbox098d9c9c6a964f0b95e5b7f2cba6e08d.mailgun.org/messages",
        auth=("api", "key-d44f2c7eb56496f3ba7f97acbd8ea222"),
        data={"from": "Steve <postmaster@sandbox098d9c9c6a964f0b95e5b7f2cba6e08d.mailgun.org>",
              "to": "askhsh 11 <unipi@mailinator.com>",
              "subject": "Η μπύρα σας!",
              "text": name1})

send_simple_message()
print("*H MPYRA SAS PERIMENEI! PARAKALW ELEGKSTE TA e-MAIL SAS*")

