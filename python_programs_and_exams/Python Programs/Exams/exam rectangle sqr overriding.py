'''
Yash now learned how he could use inheritance to create a square class
with the help of the existing rectangle class. Now with the help of method
overriding, he wants to change the side of the squares as well. He just
need to redefine the method setLength( ) and setBreadth( ).
'''
class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def setLength(self,l):
        self.l = l

    def setBreadth(self,b):
        self.b = b

    def findArea(self):
        return self.l*self.b

class Square(Rectangle):
    def setLength(self, s):
        self.l = s

    def setBreadth(self, s):
        self.b = s


rectObj = Rectangle(4,5)
print("Length Breadth and Area of Rectangle is :",rectObj.l,rectObj.b,rectObj.findArea())


sqrObj = Square(4,4)
print("Length Breadth and Area of Square is :",sqrObj.l,sqrObj.b,sqrObj.findArea())



