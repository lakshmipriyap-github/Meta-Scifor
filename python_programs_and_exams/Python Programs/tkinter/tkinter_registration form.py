'''
Create a registration form to register for a covid vaccine that should accept the following information
Create a registration form to register for a covid vaccine that should accept the following information
Name of the visitor (Entry)
Age of the visitor (Entry)
Gender (Radio Button)
Address (Text)
Email Id (Entry)
Contact No (Entry)
Country (Entry)
State (Entry)
SELECT If you are having any following disease (checkbox)
->cold
->cough
->fever
->headache
'''
import tkinter.font
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import tkinter as ttk

global count
global reg
reg = {}
count = 1

def submitForm():
    global count
    name = nameEntry.get()
    age = ageEntry.get()
    email = emailEntry.get()
    ph = contactEntry.get()
    add = addressText.get("1.0",END)
    country = countryEntry.get()
    state = stateEntry.get()
    gen = gender.get()
    reg[count]=(name,age,gen,add,email,ph,country,state,ch1.get(),ch2.get(),ch3.get(),ch4.get())
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
    emailEntry.delete(0, END)
    emailEntry.insert(0, '')
    contactEntry.delete(0, END)
    contactEntry.insert(0, '')
    countryEntry.delete(0, END)
    countryEntry.insert(0, '')
    stateEntry.delete(0, END)
    stateEntry.insert(0, '')
    check1.deselect()
    check2.deselect()
    check3.deselect()
    check4.deselect()
    addressText.delete(1.0,END)
    addressText.insert(1.0,'')
    return


Form1 = ttk.Tk()    # creating a main window
Form1.geometry("1500x780+0+0")  #setting the window size
Form1.title("Covid Vaccine Registration Form")
Form1.config(bg="#ccccff")

#variables
gender = StringVar()
ch1 = StringVar()
ch2 = StringVar()
ch3 = StringVar()
ch4 = StringVar()

# Label for heading
heading = Label(Form1,width=50,text="COVID VACCINE REGISTRATION FORM",font=("Arial",24,"bold"),foreground="#660033",bg="#ccccff")
heading.place(x=280,y=20)

backgroundImage=ImageTk.PhotoImage(file="img1.jpg")
bgLabel=Label(Form1,image=backgroundImage)
bgLabel.place(x=300,y=10)

# using frame as a place holder.
placeholder = Frame(Form1,bg="#ccccff",bd=3,borderwidth=10,cursor="hand2")
placeholder.place(x=300,y=100)

# creating labels and entries.
nameLabel = Label(placeholder,text="Name",font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff",anchor="w")
nameLabel.grid(row=1,column=1,padx=20,pady=10,ipadx=50)
nameEntry = Entry(placeholder,font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff")
nameEntry.grid(row=1,column=2,ipadx=50)

ageLabel = Label(placeholder,text="Age",anchor="w",font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff")
ageLabel.grid(row=2,column=1,padx=20,pady=20,ipadx=55)
ageEntry = Entry(placeholder,font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff")
ageEntry.grid(row=2,column=2,ipadx=50)

genderLabel = Label(placeholder,text="Gender",font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff",anchor="w")
genderLabel.grid(row=3,column=1,padx=20,pady=5,ipadx=45)
genderradio1 = Radiobutton(placeholder,text="male",variable=gender,value="male",font=("times new roman",14,"bold"),fg="#660033",bg="#ccccff",anchor="w")
genderradio1.grid(row=3,column=2,ipadx=10)
genderradio2 = Radiobutton(placeholder,text="female",variable=gender,value="female",font=("times new roman",14,"bold"),fg="#660033",bg="#ccccff",anchor="w")
genderradio2.grid(row=4,column=2)

addressLabel = Label(placeholder,text="Address",font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff",anchor="w")
addressLabel.grid(row=5,column=1,padx=20,pady=10,ipadx=40)
addressText = Text(placeholder,font=("times new roman",12,"normal"),height=3,width=40,borderwidth=1,bg="#ccccff")
addressText.grid(row=5,column=2)

emailLabel = Label(placeholder,text="Email",font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff",anchor="w")
emailLabel.grid(row=6,column=1,padx=20,pady=10,ipadx=50)
emailEntry = Entry(placeholder,font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff")
emailEntry.grid(row=6,column=2,ipadx=50)

contactLabel = Label(placeholder,text="Contact number",font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff",anchor="w")
contactLabel.grid(row=7,column=1,padx=20,pady=10,ipadx=5)
contactEntry = Entry(placeholder,font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff")
contactEntry.grid(row=7,column=2,ipadx=50)

countryLabel = Label(placeholder,text="Country",font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff",anchor="w")
countryLabel.grid(row=8,column=1,padx=20,pady=10,ipadx=40)
countryEntry = Entry(placeholder,font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff")
countryEntry.grid(row=8,column=2,ipadx=50)

stateLabel = Label(placeholder,text="State",font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff",anchor="w")
stateLabel.grid(row=9,column=1,padx=20,pady=10,ipadx=52)
stateEntry = Entry(placeholder,font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff")
stateEntry.grid(row=9,column=2,ipadx=50)

# using frame as a place holder.
placeholder2 = Frame(Form1,bg="#ccccff",bd=3,borderwidth=10,cursor="hand2")
placeholder2.place(x=320,y=560)

symptomslLabel = Label(placeholder2,text="Check if you have any of the following symptoms",font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff",anchor="w")
symptomslLabel.grid(row=1,column=1,ipadx=50)

check1 = Checkbutton(placeholder2,text="cold",variable=ch1,onvalue="cold",offvalue="no cold",font=("times new roman",14,"bold"),fg="#660033",bg="#ccccff",anchor="w")
check1.grid(row=1,column=2)
check2 = Checkbutton(placeholder2,text="cough",variable=ch2,onvalue="cough",offvalue="no cough",font=("times new roman",14,"bold"),fg="#660033",bg="#ccccff",anchor="w")
check2.grid(row=1,column=3)
check3 = Checkbutton(placeholder2,text="fever",variable=ch3,onvalue="fever",offvalue="no fever",font=("times new roman",14,"bold"),fg="#660033",bg="#ccccff",anchor="w")
check3.grid(row=1,column=4)
check4 = Checkbutton(placeholder2,text="headache",variable=ch4,onvalue="headache",offvalue="no headache",font=("times new roman",14,"bold"),fg="#660033",bg="#ccccff",anchor="w")
check4.grid(row=1,column=5)

submit = Button(Form1,text="Submit",font=("times new roman",14,"bold"),fg="#660033",bg="#ccccff",command=submitForm)
# submit.grid(row=10,column=1,padx=10,pady=10)
submit.place(x=650,y=650,)
resetData()
Form1.mainloop()
