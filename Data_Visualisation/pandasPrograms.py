import pandas
import pandas as pd

Student = {"Name" : ['ashu','teju','neenu','mahi','jagath'],
           "English":[40,30,45,38,45],
           "Maths":[23,40,31,18,40],
           "science": [39, 44, 31, 28, 39],
           }
stud = pd.DataFrame(Student)
print(stud)

stud = pd.DataFrame(Student,index=[1,2,3,4,5])
print(stud)

print(stud.loc[2])