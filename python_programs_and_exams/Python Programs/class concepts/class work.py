class Student:
    name = "Lakshmi"
    def __init__(self,x,y): #constructor in python
        self.x = x
        self.y = y
    def sum(self):
        return self.x + self.y

    def printname(self):
        print(self.name)

# ********************* single inheritance *******************
class Inherit(Student): # child
    def __init__(self):
        self.name = "LPP"
        return
    def show(self):
        print(self.name)
        return

#  ******************* multilevel inheritance ******************
class first:
    pass
class second(first):
    pass
class thirs(second):
    pass

#  ******************* multiple inheritance ******************
class multi1:
    pass
class multi2:
    pass
class multichild(multi1,multi2):
    pass

#  ******************* hierarchical inheritance ******************
class baseclass:
    pass
class heir1(baseclass):
    pass
class heir2(baseclass):
    pass

obj1 = Student(6,7)
obj2 = Student(3,5)
print(Student.name)
print("Name is :",obj1.name,obj2.name)
r = obj1.sum()
print(r)

inclass = Inherit()
inclass.show()