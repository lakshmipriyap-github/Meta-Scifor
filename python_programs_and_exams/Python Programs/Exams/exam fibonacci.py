'''
Fibonacci series
'''

class Fib:
    def __init__(self):
        self.first = 0
        self.sec = 1
    def Fibonacci(self,num):
        print(f"The fibonacci series till number {num} is : \n{self.first},{self.sec},",end="")
        for i in range(2,num+1):
            print(i,end=",")

obj = Fib()
obj.Fibonacci(10)