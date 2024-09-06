'''
Nidhi has a bad habit of repeating the same word while typing.
She wants a program that can remove duplicate phrases from paragraphs written by her.
To help Nidhi write a python program that can connect with a text file and remove repeating words
'''

def chech_duplicate(content):
    words = content.split()
    after_rem_dup = ""
    dic = {}
    for i in words:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for i in words:
        if (dic[i] == 1):
            after_rem_dup += i + ' '
    return after_rem_dup

fname = "myfile.txt" #input("Enter the file name : ")
fhandler = open(fname,"r")
content = fhandler.read()
fhandler.close()

toWriteToFile = chech_duplicate(content) # calling the function to remove the duplicates.

fhandler = open(fname,"w")
fhandler.write(toWriteToFile)
fhandler.close()
