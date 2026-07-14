             #Tuple
#tuple:immutable
"""
empty Tuple
synax
     x=()
     x=tuple()
Non-empty tuple
synax
      x=(10,20,30,50,True,"chandu")

"""
x=(10,20,30,40,55,10,20,)
print(x,type(x),id(x))
print(x[2])
print(x.count(10))
print(x.index(55))
#tuple to list: & list to tuple

x=(10,20,30,40,55,10,20,)
y=list(x)
print(y,id(y,),type(y))
y.sort()
print(y,id(y))
z=tuple(y)
print(z,id(z),type(z))
x=(10,20,30,40,[3.2,4.2],40)
print(x,id(x),type(x))
x[4][1]=1.5
print(x,id(x),type(x))
x1=[10,20,30,(1,2,3),40,50]
print(x1,type(x1),id(x1),len(x1))
s="chandrasekhar"
x=list(s)
print(x,type(x),id(x),len(x))
y=tuple(s)
print(y,type(y),id(y),len(y))
z=str(y)
print(z,type(z),id(z),len(z),z[2])
