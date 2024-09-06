'''
create a school registeration form
'''
from tkinter import *
import tkinter as ttk
from tkinter import messagebox

global count
global reg
reg = {}
count = 1

def submitForm():
    global count
    name = nameEntry.get()
    age = ageEntry.get()
    gen = gender.get()
    add = addressText.get("1.0",END)
    cls = classEntry.get()
    if(gen == 1):
        g = "male"
    else:
        g="female"
    reg[count]=(name,age,cls,g,add)
    count += 1
    print(reg,count)
    resetData()
    messagebox.showinfo('Info', "You have registerd sucessfully.")
    return
def resetData():
    # clearing all the data in the form.
    nameEntry.delete(0,END)
    nameEntry.insert(0,"")
    ageEntry.delete(0,END)
    ageEntry.insert(0,'')
    classEntry.delete(0, END)
    classEntry.insert(0, '')
    addressText.delete(1.0,END)
    addressText.insert(1.0,'')
    return

regForm = ttk.Tk()
regForm.title("students registration form")
regForm.geometry("1000x700+0+0")
regForm.config(bg="#008090")
gender = ttk.IntVar()

title = ttk.Label(regForm,text="STUDENT REGISTRATION FORM",font=("times new roman",16,"bold"),fg="#101010",bg="#008090")
title.place(x=300,y=0)

Frame1 = ttk.Frame(regForm,bg="#008090")
Frame1.place(x=100,y=100)

namel = ttk.Label(Frame1,text="Name",font=("times new roman",16,"bold"),fg="#101010",bg="#008090",anchor='w')
namel.grid(row=1,column=1,ipadx=30,padx=10,pady=10)
nameEntry = ttk.Entry(Frame1,font=("times new roman",16,"bold"),fg="#101010",bg="#ccccff")
nameEntry.grid(row=1,column=2,ipadx=30,padx=10,pady=10)

age = ttk.Label(Frame1,text="age",font=("times new roman",16,"bold"),fg="#101010",bg="#008090",anchor='w')
age.grid(row=2,column=1,ipadx=40,padx=10,pady=10)
ageEntry = ttk.Entry(Frame1,font=("times new roman",16,"bold"),fg="#101010",bg="#ccccff")
ageEntry.grid(row=2,column=2,ipadx=30,padx=10,pady=10)

classdiv = ttk.Label(Frame1,text="class ",font=("times new roman",16,"bold"),fg="#101010",bg="#008090",anchor='w')
classdiv.grid(row=3,column=1,ipadx=35,padx=10,pady=10)
classEntry = ttk.Entry(Frame1,font=("times new roman",16,"bold"),fg="#101010",bg="#ccccff")
classEntry.grid(row=3,column=2,ipadx=30,padx=10,pady=10)

genderLabel = ttk.Label(Frame1,text="gender",font=("times new roman",16,"bold"),fg="#101010",bg="#008090",anchor='w')
genderLabel.grid(row=4,column=1,ipadx=30,padx=10,pady=10)
genderradio1 = ttk.Radiobutton(Frame1,text="male",variable=gender,value=1,font=("times new roman",14,"bold"),fg="#101010",bg="#008090",anchor="w")
genderradio1.grid(row=4,column=2,padx=10,pady=10)
genderradio2 = ttk.Radiobutton(Frame1,text="female",variable=gender,value=2,font=("times new roman",14,"bold"),fg="#101010",bg="#008090",anchor="w")
genderradio2.grid(row=4,column=3,padx=10,pady=10)

addressLabel = ttk.Label(Frame1,text="Address",font=("times new roman",16,"bold"),fg="#101010",bg="#008090",anchor='w')
addressLabel.grid(row=5,column=1,padx=10,pady=10,ipadx=30)

addressText = ttk.Text(Frame1,font=("times new roman",12,"normal"),height=3,width=40,borderwidth=1,bg="#ccccff")
addressText.grid(row=5,column=2)

submit =ttk.Button(Frame1,text="Submit",font=("times new roman",16,"bold"),fg="#101010",bg="#008090",command=submitForm)
submit.grid(row=6,column=2,padx=10,pady=10)

regForm.mainloop()