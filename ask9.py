import json
import urllib.request
max=-100
name=""
url = "https://api.brewerydb.com/v2/styles?key=12bc1ebe6c39c02e2b2ba0196e5e0101&format=json"
req = urllib.request.urlopen(url)
html = json.load(req)
kleidia=input("Plhktrologhste lekseis-kleidia xwrismenes me komma :")
kleidia=kleidia.split(",")
for i in range(len(kleidia)):
    for k in html['data']:
        sum=0
        if 'description' in k:
         if kleidia[i] in k['description']:
            sum+=k['description'].count(kleidia[i])
         if 'description' in k['name']:
            if kleidia[i] in k['name']['description']:
             sum+=k['name']['description'].count(kleidia[i])
        if sum>max:
          max=sum
          name=k['name']
print("Oriste h mpura gia esas! :",name)
