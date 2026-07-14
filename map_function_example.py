# program to demonstrate to find squares from input list using map function
inlist=[1,2,3,4,5,6,7,8,9]
def squares(n):
    return n**2
outlist=map(squares,inlist)
print(list(outlist))
# program tto demonstrate to add values 10 using map function
inputlist=[10,20,30,40,50,60,70]
def add(n):
    return n+10
outlist=list(map(add,inputlist))
print(outlist)
#program to convert words in input list into uppercase words using map
name=["hello","wElcome","hi","Time"]
def uppercase(n):
    return n.upper()
uname=list(map(uppercase,name))
print(uname)