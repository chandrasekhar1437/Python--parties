""""
symmertric_difference():returns a set with symmertic difference of two sets
,symmertric_difference_update():
pop():its removes arbitrary element or (hash values)
,union():returns all unique element of both the set
,update():

"""
x={10,20,30,40,45}
y={20,30,35,45}
print(x,type(x),id(x))
print(y,type(y),id(y))
x.add(25)
print(x,id(x))
x.remove(20)
print(x,id(x))
x={10,20,30,40,45}
y={20,30,35,45}
print(x.symmetric_difference(y))
print(y.symmetric_difference(x))
x={10,20,30,40,45}
y={20,30,45}
print(x,id(x))
print(y,id(y))
x.symmetric_difference_update(y)
print(x,id(x))
x={10,20,30,40,45}
y={20,30,45}
y.symmetric_difference_update(x)
print(x,id(x))
print(y,id(y))
x={10,20,30,40,45}
y={20,30,45,55}
print(x.union(y))
x={10,20,30,40,45}
y={20,30,45,55,65}
x.update(y)
print(x)
x={10,20,30,40,45}
y={20,30,45,55,65}
print(x,x.pop())
print(x,x.pop())
print(x,x.pop())
print(x,x.pop())
print(next(iter(y)))



