'''
Chirag, Yugank, and Chris decide to create a python program together.
But they are not able to understand how they are going to divide the whole program among them.
Also, they are confused with the combination process of the program as well.
We can divide a big program into smaller parts known as functions. To explain the same thing to three students,
write a python program and create different functions to add, subtract, and multiply two numbers.
'''
def getnum():
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    return num1,num2

def add(num1,num2):
    print(f"The sum of {num1} and {num2} is : {num1+num2}")
    return

def sub(num1,num2):
    print(f"The difference of {num1} and {num2} is : {num1-num2}")
    return

def prod(num1,num2):
    print(f"The product of {num1} and {num2} is : {num1*num2}")
    return

num1,num2 = getnum()
add(num1,num2)
sub(num1,num2)
prod(num1,num2)