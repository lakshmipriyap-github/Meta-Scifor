'''
Nidhi is trying to understand how the phone gets updated with
new features with all the old features already available in the new phone.
Write a program to explain this with the help of inheritance and method
overriding. Hint: Create class Nokia1, then create class Nokia2 and
inherit all the methods from Nokia1 to Nokia2. Also, modify the required
methods in Nokia2 and add a few additional methods as well. In the
same way, you can create Nokia3 and Nokia4 as well.
'''
class Nokia1:
    def __init__(self):
        self.model = "xxxx"
        self.price = "23412"
        self.ring = "abc"

    def printmob(self):
        print(f"Model Name : {self.model} , Price : {self.price}")
        return

    def changeRingtone(self,ring):
        self.ring = ring
        print("Ring tone changed !!!")

class Nokia2(Nokia1):
    def __init__(self):
        self.model = "yyyy"
        self.price = "30000"
        self.ring = "xyz"
        self.theme = "new theme"
    def printmob(self):
        print(f"Model Name : {self.model} , Price : {self.price}, Theme : {self.theme}")
        return

    def changeTheme(self,theme):
        self.theme = theme
        print("Theme changed")
        print(f"Model Name : {self.model} , Price : {self.price}, Theme : {self.theme}")
        return

obj1 = Nokia1()
obj2 = Nokia2()

obj1.printmob()
obj1.changeRingtone("ring2")

obj2.printmob()
obj2.changeTheme("theme2")
