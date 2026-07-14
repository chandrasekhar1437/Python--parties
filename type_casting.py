int()
float()
complex()
str()
bool()
x=3.2
print(x)
print(type(x))
y=int(x)
print(y)
print(y,type(y))
x=False
print(x,type(x))
y=int(x)
print(y,type(y))
a=2+3j
 #b=int(a)
print(a,type(a))
#print(b,type(b))
#int:float,bool,string with 'int' type value only
"""float converting type """
x=12
y=float(x)
print(x,type(x))
print(y,type(y))
a=True
b=float(a)
print(a,type(a))
print(b,type(b))
x=False
y=float(x)
print(y,type(y))
#float:int,bool,string with 'int' and 'float' type value only
"""bool converting type"""
x=123
y=bool(x)
print(x,type(x))
# bool:- non zero======>True,Zero======>False
#bool: int,float,complex,str
"""complex converting type """
x=135
y=complex(x)
print(x,type(x))
print(y,type(y))
#complex:int,float,bool,all string value except text & bool
"""string converting type """
x=12
y=str(x)
print(x,type(x))
print(y,type(y))
#str:all types