from random import *
game = ["rock","paper","scissors"]
userpoint = 0
computerpoint = 0
print("Welcome to Rock Paper Scissors ...")
print("select one from Rock , paper ,scissors. press exit to stop")
while(1):
    user = input("you : ")
    user = user.lower()
    move = choice(game)
    print(f"computer's move : {move}")
    if user == move :
        print("Tie")
    elif user == "rock" :
        if move == "paper" :
            computerpoint +=1
            print("you lost")
        elif move == "scissors" :
            userpoint +=1
            print("you got a point")
    elif user == "paper" :
        if move == "scissors" :
            computerpoint +=1
            print("you lost")
        elif move == "rock" :
            userpoint +=1
            print("you got a point")
    elif user.lower() == "scissors":
        if move == "rock" :
            computerpoint +=1
            print("you lost")
        elif move == "paper" :
            userpoint +=1
            print("you got a point")
    elif user.lower() == "exit" :
        break
print(f"Scores\n you : {userpoint}\n computer:{computerpoint}")
if userpoint == computerpoint :
    print("The game is a Tie!!!!")
elif userpoint > computerpoint :
    print("Congrats .... you won the game!!!!")
else:
    print("Computer won the game !!!!")