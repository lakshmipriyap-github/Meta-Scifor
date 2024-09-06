import requests
import json
# url = "http://localhost:8000/request%20module"

url = "https://reqres.in/api/users/2"
response = requests.get(url)
with open("filetodelete.json","w") as file:
    json.dump(response.json(),file,indent=1)

# deleting from server
delRes = requests.delete(url)
print(delRes.status_code)


