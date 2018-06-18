#FUNCTION: Block of organized , re-usable code that is used to perform single action.
a=int(input("insert first name"))
b=int(input("insert second name"))
def sum(a,b):
    sum=a+b
    return sum
print("sum is",sum(a,b))

def nfunc(mlist):
    mlist.append([1,2,3,4,5,6,7])
    print("value inside func",mlist)
    return

mlist=[10,20,30];
nfunc(mlist);
print("funct outside func",mlist)

#FUNCTION ARGUMENTS
#1]Required arguments: arguments passed to a function in correct positional order.
def me(a,b):
    c=a+b
    print(c)
me(8,5)
#2)Default arguments: Argument which provides the default values to the parameters passed in the function definition.
def myf(id,name,age=20):
    print(id)
    print(name)
    print(age)
    return

myf(10,"ravi",23)
myf(2,"raju")

#3]Keyword arguments: Related to the function calls.
def my(id,name):
    print(id)
    print(name)
    return
my(id=12,name="ravi")
my(name="raju",id=23)

#RETURN STATEMENT:
#return [expression] terminates the function and transfer the output back to caller which has been generated by functions.


#SCOPE OF VARIABLES
#1) Global variables
add=0
def sum(a,b):
    add=a+b
    return add
sum(5,15)

#2) Local Variables
add=0 #global variable
def sum(a,b):
    total=a+b #local variable
    return total
add=sum(5,5)
print(add,"is sum")