'''
polymorphism
'''
class Example:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def sum(self):
        sum = self.x + self.y
        print("Finding sum of integers:",sum)
        return
class  New(Example):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def sum(self):
        sum = self.x + self.y
        print("Finding sum of decimal numbers:",sum)
        return

obj = Example(2,4)
obj.sum()
objnew = New(2,4)
objnew.sum()