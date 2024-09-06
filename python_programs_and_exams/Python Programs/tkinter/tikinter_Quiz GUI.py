'''
help matthew write a code in python that will show the questions, should be able to select any one answer using radio button,
and a button to go to the next question and a button to quit from the quiz and a message pop up to show the result once the
quiz is done
#import required modules
#read front he json file and show each question and options on the GUI using labels and ask the user to choose one option
using radiobutton options check if its right and update the score variable parallely
#finally show the score of the user when all the questions are done answering
'''
from tkinter import  *
import tkinter as ttk
from tkinter import  messagebox
import json

global correct
global wrong
global no_of_ques
correct = 0
wrong = 0

class Quiz:
    def __init__(self):
        global no_of_ques
        no_of_ques = len(questions)
        self.currq = 0
        self.ansRb = IntVar()
        self.displayLabel()
        self.displayRadio()
        self.displayButton()

    def changeRadio(self):
        self.QueLabel.config(text = questions[self.currq])
        self.op1_b.config(text = options[self.currq][0])
        self.op2_b.config(text = options[self.currq][1])
        self.op3_b.config(text = options[self.currq][2])
        self.op4_b.config(text = options[self.currq][3])
    def go_to_next_ques(self):
        global wrong
        global correct
        if self.ansRb.get() == answers[self.currq]:
            # print(self.ansRb.get(),answers[self.currq]) #check point
            correct += 1
        else:
            # print(self.ansRb.get(),answers[self.currq]) #check point
            wrong +=1

        self.currq +=1
        if self.currq == no_of_ques:
            messagebox.showinfo("result",f"Score:{correct}/{wrong+correct}\nCorrect Answer:{correct}\nWrong Answer:{wrong}")
            QuizWindow.destroy()
        else:
            self.changeRadio()
    def displayLabel(self):
        self.QueLabel = Label(QuizWindow,text=questions[self.currq],font=("times new roman", 18, "bold"), fg="#006080", bg="#ccccff")
        self.QueLabel.place(x=300, y=150)
        print()
    def displayRadio(self):
        self.op1_b = Radiobutton(QuizWindow, text=options[self.currq][0],variable=self.ansRb, value=1,font=("times new roman", 18, "bold"), bg="#ccccff", fg="#006080")
        self.op1_b.place(x=300, y=200)
        self.op2_b = Radiobutton(QuizWindow,text=options[self.currq][1],variable=self.ansRb,value=2,font=("times new roman", 18, "bold"),bg="#ccccff", fg="#006080")
        self.op2_b.place(x=300, y=250)
        self.op3_b = Radiobutton(QuizWindow,text=options[self.currq][2],variable=self.ansRb,value=3,font=("times new roman", 18, "bold"),bg="#ccccff", fg="#006080")
        self.op3_b.place(x=300, y=300)
        self.op4_b = Radiobutton(QuizWindow,text=options[self.currq][3],variable=self.ansRb,value=4,font=("times new roman", 18, "bold"),bg="#ccccff",fg="#006080")
        self.op4_b.place(x=300, y=350)

    def displayButton(self):
        self.nextq = Button(QuizWindow, command=self.go_to_next_ques,font=("times new roman", 18, "bold"), fg="#006080", bg="#ccccff",text="next question")
        self.nextq.place(x=300, y=450)
        self.exit = Button(QuizWindow, font=("times new roman", 18, "bold"), fg="#006080", bg="#ccccff",text="exit",command=QuizWindow.destroy)
        self.exit.place(x=600, y=450)

QuizWindow = ttk.Tk()
QuizWindow.geometry("1200x700+0+0")
QuizWindow.title("Python Quiz")
QuizWindow.config(bg="#ccccff")
title = Label(QuizWindow,text="~~~~~~~~PYTHON QUIZ~~~~~~~~",width=80,font=("times new roman", 20, "bold"), fg="#ccccff", bg="#006080")
title.place(x=0,y=50)
QuizWindow.resizable("false","false")
with open('Quizfile.json') as qfile:
    data = json.load(qfile)

questions = (data['questions'])
options = (data['options'])
answers = (data['answers'])

obj = Quiz()
QuizWindow.mainloop()
