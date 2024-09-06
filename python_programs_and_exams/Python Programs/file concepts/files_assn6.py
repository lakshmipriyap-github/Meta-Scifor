'''
Ayman wants to modify one of his text files.
In his text file, he wants to start a new line whenever he encounters a number followed by a period(.).
So he decides to do the same with the help of the python program. Write a program for Ayman.
'''

import re

fname = input("Enter the file name : ")
fhandle = open(fname,"r")
content = fhandle.read()
newcontent = ""
lst = re.split("\d\.",content)
print(lst)
for i in lst:
    newcontent += i+"\n"
fhandle.close()

fhandle = open(fname,"w")
fhandle.write(newcontent)
fhandle.close()