'''
Arunima created a text file on programming where she wrote the word language incorrectly many times.
Now she wants to replace the incorrect word with the correct word.
Doing it manually can take a lot of time plus she can miss out few words at the end.
To help Arunima to replace the words write a python program.
Use the concept of file handling and make changes in the text file.
'''

fname = input("Enter the file name : ")
word = input("Enter the wrong word to replace : ")
replace = input("Enter the correct word to  : ")

fhandle = open(fname,"r")
content = fhandle.read()
content = content.replace(word,replace)
fhandle.close()

fhandle = open(fname,"w")
fhandle.write(content)
fhandle.close()
