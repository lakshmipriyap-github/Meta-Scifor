import json

#python object
person = {"name":"laks","age":"34","city":"kollam","bool":False}

# ******************** converting the python object json.
personJson = json.dumps(person,indent=1, sort_keys= True) #dumping as json object in a string
print(person)
print(personJson,type(personJson))

# dumping as json object in a file with files
with open("file.json", "w") as file:
    json.dump(person,file,indent=1)

# deserialisation or decoding - converting an json back to python object
person1 = json.loads(personJson)
print(type(personJson))
print(person1["city"])

# with files
with open("file.json", "r") as file:
    person1 =  json.load(file)
    print(person1)
