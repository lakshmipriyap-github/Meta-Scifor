'''
create a scientific calculator
'''
import tkinter.font
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import tkinter as ttk
import  math

# use 2 global variables.
#  dataDisplay : variable to display the data selected by user via button clicks
#  dataEval : variable to store query string , which can further be used for finding result

global dataDisplay,dataEval
def submitForm():
    global dataEval
    res = str(eval(dataEval)) # evaluates the query string
    dataVar.set(res)
    return

def resetData():
    global dataEval,dataDisplay
    dataEval=""
    dataDisplay=""
    dataVar.set(dataDisplay)
    return

def onClick(var):
    global dataDisplay # for displaying the text
    global dataEval # for evaluation

    # framing the string to display in entry field
    dataDisplay += str(var)
    dataVar.set(dataDisplay)

    # forming evaluating string with "math variable in it.
    if(var == "cos"):
        dataEval += "math.cos"
    elif(var == "sin"):
        dataEval += "math.sin"
    elif(var == "tan"):
        dataEval += "math.tan"
    elif(var == "log"):
        dataEval += "math.log"
    else:
        dataEval += str(var)

    return



CalcForm = ttk.Tk()    # creating a main window
CalcForm.geometry("500x450+0+0")  #setting the window size
CalcForm.title("Scientific Calculator")
CalcForm.resizable("false","false")
CalcForm.config(bg="#006080")

dataVar = StringVar()   #this variable is used to show the results in the "Entry field"
dataDisplay=""
dataEval=""

# Entry for Display
display = Entry(CalcForm,width=28,textvariable=dataVar,font=("times new roman",24,"normal"),foreground="#660033",bg="#f2d9f2",justify="right",relief="raised")
display.place(x=20,y=30)

# using frame as a place holder.
placeholder = Frame(CalcForm,bg="#f2d9f2",bd=3,borderwidth=10,cursor="hand2")
placeholder.place(x=20,y=100)

cos = Button(placeholder,text="cos",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick("cos"))
cos.grid(row=0,column=0,padx=5,pady=10,ipadx=20)
sin = Button(placeholder,text="sin",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick("sin"))
sin.grid(row=0,column=1,padx=5,pady=10,ipadx=20)
tan = Button(placeholder,text="tan",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick("tan"))
tan.grid(row=0,column=2,padx=5,pady=10,ipadx=20)
cls = Button(placeholder,text="C",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command=resetData)
cls.grid(row=0,column=3,padx=5,pady=10,ipadx=20)
add = Button(placeholder,text="+",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick('+'))
add.grid(row=0,column=4,padx=5,pady=10,ipadx=20)

log = Button(placeholder,text="log",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick("log"))
log.grid(row=1,column=0,padx=5,pady=10,ipadx=20)
n7 = Button(placeholder,text="7",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick(7))
n7.grid(row=1,column=1,padx=5,pady=10,ipadx=20)
n8 = Button(placeholder,text="8",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick(8))
n8.grid(row=1,column=2,padx=5,pady=10,ipadx=20)
n9 = Button(placeholder,text="9",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick(9))
n9.grid(row=1,column=3,padx=5,pady=10,ipadx=20)
sub = Button(placeholder,text="-",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick('-'))
sub.grid(row=1,column=4,padx=5,pady=10,ipadx=20)

exp = Button(placeholder,text=f"x\u207F",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick('**'))
exp.grid(row=2,column=0,padx=5,pady=10,ipadx=20)
n4 = Button(placeholder,text="4",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick(4))
n4.grid(row=2,column=1,padx=5,pady=10,ipadx=20)
n5 = Button(placeholder,text="5",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick(5))
n5.grid(row=2,column=2,padx=5,pady=10,ipadx=20)
n6 = Button(placeholder,text="6",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick(6))
n6.grid(row=2,column=3,padx=5,pady=10,ipadx=20)
mul = Button(placeholder,text="*",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick('*'))
mul.grid(row=2,column=4,padx=5,pady=10,ipadx=20)

openBrkt = Button(placeholder,text="(",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick("("))
openBrkt.grid(row=3,column=0,padx=5,pady=10,ipadx=20)
n1 = Button(placeholder,text="1",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick(1))
n1.grid(row=3,column=1,padx=5,pady=10,ipadx=20)
n2 = Button(placeholder,text="2",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick(2))
n2.grid(row=3,column=2,padx=5,pady=10,ipadx=20)
n3 = Button(placeholder,text="3",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick(3))
n3.grid(row=3,column=3,padx=5,pady=10,ipadx=20)
div = Button(placeholder,text="/",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick('/'))
div.grid(row=3,column=4,padx=5,pady=10,ipadx=20)

closeBrkt = Button(placeholder,text=")",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick(")"))
closeBrkt.grid(row=4,column=0,padx=5,pady=10,ipadx=20)
mod = Button(placeholder,text="%",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick("%"))
mod.grid(row=4,column=1,padx=5,pady=10,ipadx=20)
n0 = Button(placeholder,text="0",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick(0))
n0.grid(row=4,column=2,padx=5,pady=10,ipadx=20)
dec = Button(placeholder,text=".",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command= lambda : onClick("."))
dec.grid(row=4,column=3,padx=5,pady=10,ipadx=20)
eq = Button(placeholder,text="=",font=("times new roman",14,"bold"),fg="#006080",bg="#ccccff",command=submitForm)
eq.grid(row=4,column=4,padx=5,pady=10,ipadx=20)

CalcForm.mainloop()
