import tkinter
import tkinter as tkex
import random
def Calc():
    x = 2 #int(input("Enter first number : "))
    y = 3 #int(input("Enter second number : "))
    sum = x+y
    dif = x-y
    prod = x*y
    div = x/y

    labelsum.config(text=f"sum: {sum}")
    labeldiff.config(text=f"sum: {dif}")
    labelprod.config(text=f"sum: {prod}")
    labeldiv.config(text=f"sum: {div}")
    labelsum.pack()
    labeldiff.pack()
    labelprod.pack()
    labeldiv.pack()
    return

window1 = tkex.Tk() # creating an window instance
window1.title("Calculator")
window1.configure(bg="pink",padx=300,pady=300)
button1 = tkinter.Button(window1,text="submit",bg="cyan",command=Calc)#creating button
button1.pack()#placing in the window


labelsum = tkex.Label(window1,text="",bg="light green")
labeldiff = tkex.Label(window1,text="",bg="light green")
labelprod = tkex.Label(window1,text="",bg="light green")
labeldiv = tkex.Label(window1,text="",bg="light green")


button2 = tkinter.Button(window1,text="close",bg="cyan",command=window1.destroy)#creating button
button2.pack()#placing in the window

window1.mainloop() # to display the window