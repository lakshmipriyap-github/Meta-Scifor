'''
Shubham had created a BMI calculator to check his health condition daily.
But he is not able to record the values. He wants to see how his BMI is changing.
So he decided to connect his BMI program with a text file using the concept of file handling.
Now, when he uses his BMI program, his height, weight, BMI, and date get added to a text file "bmi.txt".
Create a program that can do the same thing for you.
'''

wt = input("Enter your weight in kilograms : ")
ht = input("Enter your height in meters : ")
bmi = float(wt)/pow(float(ht),2)


content = f"{dt}\nWEIGHT : {wt} HEIGHT : {ht} BMI : {bmi}\n"

fname = open("sample.txt", "a")
fname.writelines(content)
fname.close()
