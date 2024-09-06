from tkinter import *
from tkinter import messagebox
import tkinter as tkex

wind = tkex.Tk()
wind.title("hello")
wind.geometry("1500x750+0+0")

loginFrame = Frame(wind,bg='blue')
loginFrame.place(x=400,y=300)

usernameLabel=Label(wind,text="USER NAME",font=("times new roman",18,'bold'),fg='maroon',bg='#EECFA1')
usernameLabel.grid(row=100,column=100,pady=10,padx=20)



wind.mainloop()