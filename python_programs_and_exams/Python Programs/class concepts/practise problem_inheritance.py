'''
create a class object and insert polymorphism ,abstraction concepts with using advance concepts
'''
class Numbers:
    def displayNum(self,n):
        if(n <= 0):
            return
        else:
            print(n, end=",")
            self.displayNum(n-1)

class UsingYield(Numbers):
    def displayNum(self,n):
        for i in range(0,n):
            yield i

obj1 = Numbers()
obj1.displayNum(10)

obj2 = UsingYield()
n = obj2.displayNum(3)
print("\nFirst Value",next(n))
print("second Value",next(n))
print("third Value",next(n))