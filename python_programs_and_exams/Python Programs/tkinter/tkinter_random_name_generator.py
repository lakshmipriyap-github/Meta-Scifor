'''
In a coding class the teacher has taught the kids about the python GUI and has now assigned the following task to the students
1) Create a random name picker from a given list of students
2) should have a button clicking on which a random name should be picked
3) Once the random name is picked the name should be removed from the list so that the name is not repeated and
also the removed name should show in completed section
#create a GUI with two sections one to see the randomly generated name and the other one to see the names
that are generated randomly and which are not suppose to be considered for generating randomly again.
'''

import tkinter as ttk
from tkinter import messagebox
import random

class Picker:
    def __init__(self):
        self.name = ["niya","seetha","ram","jay","manno","sudeep","chinu","veer","tommy"]
        self.namestr = ""
        self.name_random=[]
        self.randomstr = ""

    def getName(self):
        if (self.name):
            self.curr_name = random.choice(self.name)
            self.name_random.append(self.curr_name)
            self.randomstr = ",".join(self.name_random)
            self.nameLabel.config(text=self.randomstr)

            self.name.remove(self.curr_name)
            self.namestr = ",".join(self.name)
            self.listLabel.config(text=self.namestr)
        else:
            self.listLabel.config(text="list is empty")

    def Display(self):
        leftFrame = ttk.Frame(NamePicker,bg="#006080")
        leftFrame.place(x=0,y=0)
        self.leftTitle = ttk.Label(leftFrame, text="pick a name from the list", font=("times new roman", 14, "bold"),bg="#ccccff", fg="#006080")
        self.leftTitle.grid(row=0, column=50, padx=20, pady=20)
        self.listLabel = ttk.Label(leftFrame, text=self.name, font=("times new roman", 14, "bold"), bg="#ccccff",fg="#006080")
        self.listLabel.grid(row=250, column=50, padx=20, pady=20)
        self.pickButton = ttk.Button(leftFrame, text="Pick", font=("times new roman", 14, "bold"), bg="#ccccff",fg="#006080", command=self.getName)
        self.pickButton.grid(row=500, column=50, padx=20, pady=20)

        rightFrame = ttk.Frame(NamePicker,bg="#006080")
        rightFrame.place(x=500,y=0)
        self.rightTitle = ttk.Label(rightFrame, text="Selected names list", font=("times new roman", 14, "bold"),bg="#ccccff", fg="#006080")
        self.rightTitle.grid(row=0, column=50, padx=20, pady=20)
        self.nameLabel = ttk.Label(rightFrame, text=self.name_random, font=("times new roman", 14, "bold"), bg="#ccccff",fg="#006080")
        self.nameLabel.grid(row=250, column=50, padx=20, pady=20)

NamePicker = ttk.Tk()
NamePicker.title("Name Picker")
NamePicker.geometry("1000x700+0+0")
obj = Picker()
obj.Display()
NamePicker.mainloop()