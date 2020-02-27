import requests
import time

url = "https://api.thingspeak.com/update.json"
data = {"api_key":"73J9QW95XSLQTY0G","created_at": "2018-04-23 21:36:22 +0200", "field1": "3","field2":"50" }

while True: 
   
    resp =requests.get(url,json=data)
    time.sleep(5) 
