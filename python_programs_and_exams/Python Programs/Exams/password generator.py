'''
Random Password Generator:
'''
import random
import string

alpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
sym = ["!",'@','$','%','&']
dig = ['0','1','2','3','4','5','6','7','8','9']
password = []
str=""

for i in range(0,5):
    password.append(random.choices(alpa)[0])
password.append(random.choices(sym)[0])
for i in range(0,5):
    password.append(random.choices(dig)[0])
password.append(random.choices(sym)[0])

for i in password:
    str += i
print("Random password is : ",str)