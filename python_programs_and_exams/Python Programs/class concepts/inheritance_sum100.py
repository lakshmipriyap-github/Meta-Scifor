'''
create a sum of 100 numbers using single inheritance
'''
class Sum:
    def __init__(self,n):
        self.n = n
        self.sum = 0

class findSum(Sum):
    def printSum(self):
        for i in range(1,self.n+1):
            self.sum += i
        print(f"Sum of {n} numbers is : {self.sum}")
        return

n = int(input("Enter the number :"))
showObj = findSum(n)
showObj.printSum()