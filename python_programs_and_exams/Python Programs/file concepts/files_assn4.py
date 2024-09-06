'''
Arvind has a huge text file and he wants to put a serial number at the beginning of each line.
Doing this task manually can take a lot of time. He is not aware of python file handling.
Write a python program that can put a serial number in front of each line in any specified text file.
'''

fname = input("Enter the file name : ")
fhandle = open(fname,"r")
count = 1
content = ""

# reading from the file and storing the contents in a string with line numbers.
for line in fhandle.readlines():
    content += f"{count}. {line}"
    count+=1
fhandle.close()

fhandle = open(fname,"w")
fhandle.write(content)
fhandle.close()