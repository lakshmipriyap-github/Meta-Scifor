'''
create a calculator using the class object
'''
class calc:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x - self.y
    def prod(self):
        return self.x*self.y
    def div(self):
        if( self.y != 0):
            return  self.x/self.y

ch = input("1.additon \n2.substraction\n3.multiplication\n4.division\n")
x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
calcObj = calc(x,y)
if( ch == "1"):
    print(f"The sum of {x} and {y} is : {calcObj.add()}")
elif( ch == "2"):
    print(f"The difference of {x} and {y} is : {calcObj.sub()}")
elif( ch == "3"):
    print(f"The product of {x} and {y} is : {calcObj.prod()}")
elif( ch == "4"):
    print(f"The quotient of {x} and {y} is : {calcObj.div()}")
else:
    print("Wrong choice !!!")

