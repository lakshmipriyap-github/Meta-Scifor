import json
import requests

# **********************************  http get request *******************************************
# payload = {"usname":"laks","code":"1234"}
# url1 = "https://httpbin.org/get"
# response = requests.get(url1,params=payload)
# # print(response.content)
# print(response.text)
# if response.status_code == 200:
#      print("success")
#      respJson = response.json()
#      arg = respJson.get("args")
#      header = respJson.get("headers")
#      print(f"args : {arg} ---- header : {header}")
#      dict = json.dumps(respJson)
#      print(dict,"\n",type(dict))
# else:
#   print("permission denied",response.status_code)


# **********************************  http post request *******************************************
# payload = {"username": "laks","password":"1234"}
# url1 = "https://httpbin.org/post"
# response = requests.post(url1,data=payload)
# r_dic = response.json()
# print(r_dic['form'])
# # print(response.text)

# #******************
url1 = "https://httpbin.org/"
response = requests.get(url1)
content = response.text
with open("file.json","w") as file:
     json.dump(content,file,indent=1)