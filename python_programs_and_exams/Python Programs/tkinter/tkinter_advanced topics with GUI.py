'''
Using tkinter add filter ,lambda and other advance concept to display once click on the button
'''
import tkinter as ttk

class Display:
    def __init__(self):
        self.numbers = [i + 1 for i in range(0, 20)]  # list comphrehension.
        self.Label1 = ttk.Label(font=("times new roman", 18, "bold"), fg="#660033", bg="#ccccff")
        self.Label1.place(x=300, y=100)

        self.Labelgen = ttk.Label(font=("times new roman", 18, "bold"), fg="#660033", bg="#ccccff")
        self.Labelgen.place(x=300, y=500)

        self.even = filter(self.FilterTheEven,self.numbers)
        self.odd = filter(self.FilterTheOdd,self.numbers)
        self.n = self.displayNumber() #calling generator function

    def displayNumber(self):
        for i in self.numbers:
            yield i
    def displayYield(self):
        num = next(self.n)
        if(num):
            self.Labelgen.config(text=num)
        else:
            self.Labelgen.config(text="list over")

    def findSum(self,numbers):
        s = 0
        for i in numbers:
            s +=i
        self.Labelsum = ttk.Label(font=("times new roman", 18, "bold"), fg="#660033", bg="#ccccff")
        self.Labelsum.place(x=400, y=400)
        self.Labelsum.config(text=s)

    def FilterTheEven(self,numbers):
        return numbers%2 == 0

    def FilterTheOdd(self, numbers):
            return numbers % 2 == 1

    def displayLabel(self):
        self.Label1.config(text=self.numbers)

    def displayEven(self):
        self.Label2 = ttk.Label(font=("times new roman", 18, "bold"), fg="#660033", bg="#ccccff")
        self.Label2.place(x=300, y=200)
        self.Label2.config(text=list(self.even))

    def displayOdd(self):
        self.Label3 = ttk.Label(font=("times new roman", 18, "bold"), fg="#660033", bg="#ccccff")
        self.Label3.place(x=300, y=300)
        self.Label3.config(text=list(self.odd))

Win = ttk.Tk()
Win.title("Numbers")
Win.geometry("1000x700+0+0")
obj = Display()
Button1 = ttk.Button(text="Show the list",font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff",command=obj.displayLabel)
Button1.place(x=100,y=100)

ButtonEven = ttk.Button(text="Even list",font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff",command=obj.displayEven)
ButtonEven.place(x=100,y=200)

ButtonOdd = ttk.Button(text="Odd list",font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff",command=obj.displayOdd)
ButtonOdd.place(x=100,y=300)

ButtonSum = ttk.Button(text="Sum",font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff",command= lambda : obj.findSum(obj.numbers))
ButtonSum.place(x=100,y=400)

Buttongen = ttk.Button(text="Generate a function",font=("times new roman",16,"bold"),fg="#660033",bg="#ccccff",command=obj.displayYield)
Buttongen.place(x=100,y=500)

Win.mainloop()