'''  Create a quiz program using class concept
'''
class Quiz:
    correct = 0
    wrong = 0
    questions = [
        ("Which is the largest animal on earth?","Blue whale"),
        ("Which is the largest animal on land?","elephant"),
        ("Which is our National flower ?","lotus"),
        ("What is the capital of India ?","new delhi"),
        ("tallest animal ? ","giraffe")
    ]
    def askQuiz(self):
        for i in self.questions:
           ans = input(i[0])
           if (ans.lower() == i[1].lower()):
               print("Correct")
               self.correct += 1
           else:
               self.wrong += 1
               print("Wrong !!!")
        return
    def score(self):
        print("Your total Score is :",self.correct)
        return

quizObj = Quiz()
quizObj.askQuiz()
quizObj.score()