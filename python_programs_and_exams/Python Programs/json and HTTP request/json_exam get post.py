'''
How do I make a GET  and post request using the requests module? and also checking status
'''

import requests
import json

payload = {"user":"lakshmi","code":"1234"}
url = "https://api.chucknorris.io/jokes/random"

# get request
resp = requests.get(url,params=payload)
if( resp.status_code == 200):
    contentJson = resp.json()
    print(contentJson)
else:
    print("Error ",resp.status_code)

#post request
resp = requests.post(url,data=payload)
if( resp.status_code == 200):
    print("sucess")
else:
    print("Error ",resp.status_code)
