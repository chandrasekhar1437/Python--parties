# program to add
from functools import reduce
num=[1,2,3,4,5]
def add(a,b):
    return a+b
res=reduce(add,num)
print(res)
# program to product
numb=[1,2,3,4,5]
resu=reduce(lambda x,y:x*y,numb)
print(resu)
#program to find max number in list using reduce
list=[10,25,85,23,52]
def max(a,b):
    if a>b:
        return a
    else:
        return b
result=reduce(max,list)
print(result)
#program to find max number in list using reduce
lists=[18,98,89,78,56,89,99,]
re=reduce(lambda x,y:x if x>y else y,lists)
print(re)
