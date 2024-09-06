'''
Create a factorial program using class object
'''
class factorial:
    def __init__(self):
        self.fact = 1

    def find_fact(self,num):
        for i in range(1,num+1):
            self.fact =self.fact * i
        return self.fact


obj = factorial()
print(obj.find_fact(4))