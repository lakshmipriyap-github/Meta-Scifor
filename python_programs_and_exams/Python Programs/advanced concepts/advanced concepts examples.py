'''
maps,filters,lamda,list comprehension,iterator
'''
#**************** map ***************************
print("************ maps **************")
def fun(num):
    return num+1

num = [2,3,5,7,3]
map1 = map(fun,num)
print(list(map1))

def fun_print(num):
    print(num,end=" ")

map2 = map(fun_print,num)
list(map2)

# #**************** filter  ***************************
print("\n************ filter **************")
def filter_fun(num):
    return num+1 > 5

fltr = filter(filter_fun,num)
print(list(fltr))

# #**************** lamda ***************************
print("************ lamda **************")
add = lambda x,y : x+y
print(add(2,3))

show = lambda add: print(add)
show(add(4,8))

# #**************** list comprehension ***************************
print("************ list comprehension **************")
res = [i+1 for i in range(1,5)]
print(res)

# #**************** iteration function ***************************
print("************ iteration **************")
n = [2,3,4]
lst = iter(n)
print("this is iter",end=",")
print(next(lst))
print("different from for loop",end=",")
print(next(lst))
print("I can get the values in between , from where I stopped last", end=",")
print(next(lst))

# #**************** generators function ***************************
print("************ generators **************")
def gen():
    for i in range(0,10):
        yield i

obj = gen()
print("Hello",end=",")
print(next(obj))
print("generators are similar to iter",end=",")
print(next(obj))
print("but with functions",end=",")
print(next(obj))
print("I can retreived from where I stopped",end=",")
print(next(obj))
print("unlike the return values from a function",end=",")
print(next(obj))

#**************** decorator function ***************************
print("************ decorators **************")
# to change the behaviour of a class or a function
'''
 1.a function can either be used as an object ie, there is a func1(),
  then i m assigning funobj = func1, now i can call like funcobj() instead of func1()
2. function can be passed as an args to another fn
3. as a wrapper function. that is returning one fun from another.
'''
def BiggerPrint(func):
    def SmallerPrint():
        print("I am in Smaller print")
        s = func()
        return s.lower()
    print("I am in Bigger Print")
    return SmallerPrint

def passstring():
    print('I am pass string')
    return "ABCDEF"

# using the function as argument.
objsmall = BiggerPrint(passstring)
print(objsmall())

# now I am using a decorator. below decorator is equivalent to the above commented code.
@BiggerPrint
def passstring():
    print('I am pass string')
    return "ABCDEF"
passstring()



# #**************** asynchronous function ***************************
import  asyncio

print("************ async **************")

async def Numbers():
    for i in range(1,5):
        print(i)
        await Numerals()

async def Numerals():
    lst = ["one","two","three","four","five"]
    for i in lst:
        print(i)



