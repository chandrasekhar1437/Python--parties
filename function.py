                 #function in python
"""
what  is function?
function in python are self-contained block of code designed to perform a specific task. def name()
#argument:-
 1). positional argument -  ",/"
 2). default argument   - 
 3). keyword argument   -   "*," 
 4). arbitary argument   - 
 5). arbitary keyword argument -

"""
def add():
    a=20
    b=20
    c=a+b
    print(c)
add()
#program to demonstrate function in python
print("hello")
print("welcome to python")
#function definition
def got_office(h,j):
    print(f"today is {h},must reach office {j}")
    print("wakeup")
    print("get ready")
    print("take breakfast")
    print("took our vehicle")
    print("to reach office")
#function calling
got_office("monday","10am")
got_office("tuesday","10am")
got_office("wednesday","10am")
got_office("thursday","10am")
print("after reached to the office i started my work")
got_office("n","h")
# example of positional argument
def add(x,y):
    z=x+y
    print(f"add to argument {z}")
add(10,20)
# example of default argument
def user(name,city,country="india"):
    print(name,city,country)
user("chandu","east govardi")
user("pavan","hyd")
user("bunny","vbfjjd","usa")
#example of keyword argument
def findbig(x,y):
    if(x>y):
        print("x is big")
    else:
        print("y is big")
findbig(y=int(input("enter y values is ")),x=int(input("enter x value is ")))
findbig(y=int(input("enter y values is ")),x=int(input("enter x value is ")))
findbig(y=int(input("enter y values is ")),x=int(input("enter x value is ")))
# example of arbitrary argument is
def saywelcome(*x):
    for i in x:
        print("welcome",i)
saywelcome("chandu","ravi","siva","ramesh")
# example of arbitrary keyword argument
def printaddres(**x):
    for k,v in x.items():
     print(k,"-",v)
printaddres(stree="kudupuru",city="east-gordvari",country="india",dlno="1-136/1")