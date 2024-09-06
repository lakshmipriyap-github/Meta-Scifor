'''
Random Quote Engine: Design a function that selects and displays a random quote from a predefined list.
'''
import random

def quoteGenerator():
    lst = ["quote1","quote2","quote3","quote4","quote5"]
    randomquote = random.choices(lst)
    print("The Quote for the day is : ",randomquote)
    return

quoteGenerator()

