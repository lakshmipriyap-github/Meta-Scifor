'''
Nidhi is creating a program in python for her school project.
In between the program, she is converting numerical numbers into word format again and again.
Then she realizes that she needs a function that can convert a number into word format with hyphens between each word.
( for example 57 = five-seven ). To help Nidhi create a function toWord() that can do the same thing.
Hint: Use for loop and use if-elif-else condition Sample run: >> toWord(89) >> eight-nine >> toWord(398) >> three-nine-eight
'''
def convert(num):
    word = []
    while(num !=0):
        mod = num%10
        num = num//10
        word.append(toword(mod))
    print(word[::-1])
    return
def toword(mod):
    if(mod == 1):
        return "one"
    elif(mod == 2):
        return "two"
    elif (mod == 3):
        return "three"
    elif (mod == 4):
        return "four"
    elif (mod == 5):
        return "five"
    elif (mod == 6):
        return "six"
    elif (mod == 7):
        return "seven"
    elif (mod == 8):
        return "eight"
    elif (mod == 9):
        return "nine"
    elif (mod == 0):
        return "zero"
    return
num = int(input("Enter the number :"))
convert(num)