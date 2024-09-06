'''
Himanshi has a text file and she wants to check whether that file contains any numerical value.
So to help Himanshi write a python program that can check whether the text file includes any numerical value or not.
As text files contain so many lines, so print the line number that has numerical values
'''


fname = open("../json and HTTP request/sample.txt", "r")
content = fname.readlines()
lineno = 0
for i in content:
    lineno += 1
    line = i.split()
    for j in line:
        if j.isdigit():
            print(f"line number  {lineno}  has digit  {j} ")

