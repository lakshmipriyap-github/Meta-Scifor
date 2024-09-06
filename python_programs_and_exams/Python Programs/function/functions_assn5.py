'''
There is a famous clothing store in a city, which has four different sub-branches under the main branch.
End of each day four sub-branches should report back to the main branch about available stock in percentage.
write a python program and create four different branches and print just the available stock of each branch.
hint:#create four functions with name of your choice which should consists of one variable as total_stock,
sold_stocks, available_stock and a print statement that prints the available stock value with a proper print statement
'''
totalstock = []
stocksold = []
def branch1():
    avail = totalstock[0]-stocksold[0]
    print(f"Branch 1 \nTotalStock : {totalstock[0]}\nSold Stock : {stocksold[0]} \nAvailable stock : {avail}")
    return
def branch2():
    avail = totalstock[1]-stocksold[1]
    print(f"Branch 2 \nTotalStock : {totalstock[1]}\nSold Stock : {stocksold[1]} \nAvailable stock : {avail}")
    return
def branch3():
    avail = totalstock[2]-stocksold[2]
    print(f"Branch 3 \nTotalStock : {totalstock[2]}\nSold Stock : {stocksold[2]} \nAvailable stock : {avail}")
    return
def branch4():
    avail = totalstock[3]-stocksold[3]
    print(f"Branch 4 \nTotalStock : {totalstock[3]}\nSold Stock : {stocksold[3]} \nAvailable stock : {avail}")
    return
print("Enter the total stock of branch ")
for i in range(0,4):
 totalstock.append(int(input(f"{i+1} : ")))
print("Enter the  stock sold of branch ")
for i in range(0,4):
     stocksold.append(int(input(f"{i+1} :  ")))
branch1()
branch2()
branch3()
branch4()