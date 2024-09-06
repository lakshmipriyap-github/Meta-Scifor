'''
build a calculator using single inheritance
'''
class Calc:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def addition(self):
        return self.x + self.y
    def subtraction(self):
        return self.x - self.y
    def multiplication(self):
        return self.x * self.y
    def division(self):
        return self.x / self.y
class Advanced(Calc):
    def Modulo(self):
        return self.x%self.y
    def exponent(self):
        return (pow(self.x,self.y))
ch = input(f"Enter what operation you have to do : \n1. addition\n 2. substraction\n3. multiplication\n 4. division\n 5. modulo\n 6. exponent\n")
x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
base = Calc(x,y)
adv = Advanced(x,y)
if(ch == "1"):
    print("Sum",base.addition())
elif(ch == "2"):
    print("difference",base.subtraction())
elif (ch == "3"):
    print("product", base.multiplication())
elif (ch == "4"):
    print("quotient", base.division())
elif (ch == "5"):
    print("modulus", adv.Modulo())
elif (ch == "6"):
    print("exponent", adv.exponent())
