'''
Create a student management system project using the classes and objects
concept in python which should perform the following operations
1.Accept Student details
2.Display Student Details
3.Search Details of a Student
4.Delete Details of Student
5.Update Student Details
6.Exit
#create a student class and add functions for the above shown options in
the description and ask the user to choose one among them
'''

class StudentsMgmtSystem:
    def __init__(self):
        self.student = {}
    def addStudent(self,name,rno,cls,div):
        self.student[name] = [rno,cls,div]
        return
    def Display(self):
        for name in self.student:
            print(f"Name :{name},rno :{self.student[name][0]},class&div :{self.student[name][1]}{self.student[name][2]}")
        return
    def Search(self,name):
        for i in self.student:
            if (i.lower() == name.lower()):
                print(f"Name : {i}\nRno : {self.student[name][0]}\nclass & div: {self.student[name][1]}{self.student[name][2]}")
            else:
                print("Data not found !!!!")
        return
    def Delete(self,name):
        self.student.pop(name)
        return
    def Update(self,name, rno, cls, div):
        self.student[name][0] = rno
        self.student[name][1] = cls
        self.student[name][2] = div
        return

obj1 = StudentsMgmtSystem()
while (1):
    ch = input(f"Enter your option \n1.Add student\
                  \n2.Display Student\
                  \n3.Search student\
                  \n4.Delete Student\
                  \n5.Update Student\
                  \n6.Exit\n")
    if (ch == "1"):
        name = input("Enter the name : ")
        rno = int(input("Enter the rno : "))
        cls = int(input("Enter the class : "))
        div = input("Enter the division : ")
        obj1.addStudent(name, rno, cls, div)
    elif (ch == "2"):
         obj1.Display()
    elif (ch == "3"):
        name = input("Enter the name of the student :  ")
        obj1.Search(name)
    elif (ch == "4"):
        name = input("Enter the name of the student : ")
        obj1.Delete(name)
    elif (ch == "5"):
        name = input("Enter the name : ")
        rno = int(input("Enter the rno : "))
        cls = int(input("Enter the class : "))
        div = input("Enter the division : ")
        obj1.Update(name, rno, cls, div)
    elif (ch == "6"):
        break

