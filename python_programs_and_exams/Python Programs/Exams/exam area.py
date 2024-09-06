'''
Create a program of finding perimeter of a triangle and area of any three shapes using class object
'''
import math
class shapes:

    def __init__(self):
        return
    def triangle_perimeter(self,a,b,c):
        return a+b+c
    def area_sqr(self,side):
        return side*side
    def area_circle(self,radius):
        return(math.pi*radius*radius)
    def area_rectangle(self,l,b):
        return l*b
ch = input("Enter your choice : \n1.perimeter of a triangle\n2.area of a square\n3.area of a circle\n4.area of a rectangle\n")
obj = shapes()
if(ch == "1"):
    print("Enter the three sides of a triangle a,b,c :")
    a = int(input())
    b = int(input())
    c = int(input())
    print(f"PERIMETER OF THE TRIANGLE IS : {obj.triangle_perimeter(a,b,c)}")
elif(ch == "2"):
    print("Enter the sides of square :")
    side = int(input())
    print(f"Area of the square is  : {obj.area_sqr(side)}")
elif(ch == "3"):
    print("Enter the radius of the circle :")
    radius = int(input())
    print(f"Area of the circle is  : {obj.area_circle(radius)}")
elif(ch == "4"):
    print("Enter the length and breadth:")
    l = int(input())
    b = int(input())
    print(f"Area of the rectangle is  : {obj.area_rectangle(l,b)}")


