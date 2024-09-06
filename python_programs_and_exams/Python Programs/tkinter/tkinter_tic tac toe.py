import tkinter as ttk
from tkinter import messagebox

class Tictactoe:
    def __init__(self,window):
        self.window = window
        self.buttons = []
        self.showgame()

    def showgame(self):
        self.playarea = [""]*9
        self.curr_player = "X"
        self.buttons = []
        for i in range(0, 3):
            rows = []
            for j in range(0, 3):
                button = ttk.Button(self.window, text="", font=("times new roman", 14, "bold"), width=5, height=3, command= lambda i=i ,j=j : self.playGame(i,j))
                button.grid(row=i, column=j, padx=10, pady=10)
                rows.append(button)
            self.buttons.append(rows)

    def playGame(self,i,j):
        if self.playarea[i*3 +j] == "":
            self.playarea[i*3 +j] = self.curr_player
            self.buttons[i][j].config(text = self.curr_player)
            if self.winner():
                messagebox.showinfo("Game over!!!",f"Player {self.curr_player} won!")
                self.showgame()
        else:
             if self.curr_player == "X":
                self.curr_player = "O"
             else:
                self.curr_player = "X"

    def winner(self):
        states = [ (0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for x in states :
            if self.playarea[x[0]] == self.playarea[x[1]] == self.playarea[x[2]] != "":
                return True
        return False



window = ttk.Tk()
window.geometry("500x450+0+0")
window.title("TIC-TAC-TOE")
window.resizable("False","False")
obj = Tictactoe(window)
window.mainloop()