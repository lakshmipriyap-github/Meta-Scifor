'''
Jhony, a 10th grade kid has recently started to learn python tkinter and
is so much keen to understand how an MS Paint works and wants to create a
very small replica of it in his own system using python with the following buttons
pen
brush
color
eraser
brush/pen size changer
#import the libraries and create the GUI using the drawing features of the tkinter
'''

from tkinter import *
from tkinter import colorchooser
import tkinter as ttk

class Draw():

    def __init__(self):
        self.x = None # coordinates for drawing
        self.y = None
        # default settings.
        self.pencolor = "black"
        self.bg = "white"
        self.fg = "black"
        self.width = 5
        self.paintWindow() #to display the widgets and the canvas in the paint window.
        self.paintCanvas.bind('<ButtonRelease-1>',self.reset) #reset the coordinates when mouse released after the drawing.

    def reset(self, event):# function to reset the mouse cordinates.
        self.x = None
        self.y = None

    def erase(self):# function to erase/clear the canvas
        self.paintCanvas.delete(ALL)
        return

    def setWidth(self,width):
        self.width = width

    def drawWithPen(self,event):# function to draw with pen.
        if self.x and self.y:
            self.paintCanvas.create_line(self.x,self.y,event.x,event.y,width=self.width,fill=self.fg,capstyle="round",joinstyle="round",smooth="raw")
        self.x = event.x
        self.y = event.y
        return

    def drawWithBrush(self,event):# function to draw with pen.
        if self.x and self.y:
            self.paintCanvas.create_line(self.x,self.y,event.x,event.y,width=self.width,fill=self.fg,capstyle="round",stipple="gray75",smooth="raw")
        self.x = event.x
        self.y = event.y
        return
    def setBackground(self):# function to set the canvas color.
        self.bg = colorchooser.askcolor()[1]
        self.paintCanvas.config(bg=self.bg)
        return

    def setForeground(self):# function to set the brush,pen color.
        self.fg = colorchooser.askcolor()[1]
        return

    def paintWindow(self):
        # creating the frames for widgets.
        leftPane = Frame(PaintWindow,cursor="hand2",bd=3,bg="#D8BFD8")
        leftPane.place(x=10,y=50)
        # buttons to display the options
        pen = Button(leftPane, text="pen", font=("times new roman", 14, "bold"), fg="black",justify="center",command= lambda : self.paintCanvas.bind("<B1-Motion>",self.drawWithPen))
        pen.grid(row=0,column=0,ipadx=40,pady=10)
        brush = Button(leftPane,text="brush",font=("times new roman",14,"bold"),fg="black",justify="center",command= lambda : self.paintCanvas.bind("<B1-Motion>",self.drawWithBrush))
        brush.grid(row=2,column=0,ipadx=30,pady=10)
        color = Button(leftPane,text="color",font=("times new roman",14,"bold"),fg="black",justify="center",command=self.setForeground)
        color.grid(row=3,column=0,ipadx=30,pady=10)
        bgcolor = Button(leftPane, text="background", font=("times new roman", 14, "bold"), fg="black", justify="center",command=self.setBackground)
        bgcolor.grid(row=4, column=0, pady=10)
        eraser = Button(leftPane,text="erase",font=("times new roman",14,"bold"),fg="black",justify="center",command=self.erase)
        eraser.grid(row=5,column=0,ipadx=30,pady=10)
        # slider to adjust the pen/brush size. using "self" since functions are accessing it.
        self.slider = ttk.Scale(leftPane,orient="vertical",from_=5,to=50,command=self.setWidth)
        self.slider.set(self.width) #set the default value to display.
        self.slider.grid(row=6,column=0,ipadx=10,ipady=10)
        sliderLabel = Label(leftPane,text="size",font=("times new roman", 14, "bold"),fg="black", justify="center")
        sliderLabel.grid(row=7,column=0,ipadx=10)
        # creating a canvas.using "self" since functions are accessing it.
        self.paintCanvas = ttk.Canvas(PaintWindow,bg=self.bg,width=830,height=670,borderwidth=3,border=2)
        self.paintCanvas.place(x=150,y=10)
        return

PaintWindow = ttk.Tk()
PaintWindow.geometry("1000x700+0+0")
PaintWindow.title("Paint")
PaintWindow.resizable("false","false")
PaintWindow.config(bg="#D8BFD8")
obj = Draw()
PaintWindow.mainloop()
