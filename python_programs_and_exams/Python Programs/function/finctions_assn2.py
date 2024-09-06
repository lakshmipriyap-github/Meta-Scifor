'''
Sahil is wondering whether we can use the same concept of functions in creating simple and compound interest calculators.
He is trying to create it but is unable to return the answers from the functions. Help him in doing the same
'''
def getparam():
    p = float(input("Enter the Principal amount : "))
    r = float(input("Enter the rate of interest : "))
    t = float(input("Enter the time period : "))
    return p,r,t
def calcSI(p,r,t):
    si = p*r*t
    return si
def calcCI(p,r,t):
    ci = (p*pow((1+r),t))-p
    return ci

p,r,t = getparam()
si = calcSI(p,r,t)
ci = calcCI(p,r,t)
print(f"The simple interest is : {si} and compound interest is :{ci}")
