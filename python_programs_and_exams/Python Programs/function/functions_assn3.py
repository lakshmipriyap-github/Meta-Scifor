'''
Nidhi is writing a long program. She needs a function that can check whether a given number is a perfect square or not.
To help Nidhi, write a program in python and create a function that checks whether the given number is a perfect square or not.
'''

def checksqr(num):
    root = pow(num,.5)
    print(root%10,root)
    if( root%10 == 0):
        print(f"Then number {num} is a perfect square")
    else:
        print(f"Then number {num} is not a perfect square")
    return

num = int(input("Enter the number to check for perfect square : "))
checksqr(num)