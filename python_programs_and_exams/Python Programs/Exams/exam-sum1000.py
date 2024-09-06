'''
Print the sum of 1000 numbers using class object concepts
'''
class Sum:

    def __init__(self):
        self.sum = 0
    def find_sum(self):
        for i in range(1,1000+1):
            self.sum+=i
        print("The sum of 1000 numbers is :",self.sum)
        return

obj = Sum()
obj.find_sum()