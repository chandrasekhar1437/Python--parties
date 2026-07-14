      #SET
'''sets: to store collection of unique element
          it maintain  unordered collection.it does not follow insertion order.
        # predefined function  
          add():
          clear():
          copy():
          difference(): Returns a set containing the element that are in first set and not in second set
          difference_update(): Removes the items in this set that are also included in another
          dicard():
          remove():
          intersection():Returns common elements
          isdisjoint():
          issubset():
          issuperset():
          pop():
          union():
          update():
          
          
          
'''
"""#set-"{}"----> sysmbol is mutable
#empty set
#x=set()
#print(x,type(x))
#non-set
#x={10,20,30,40,55,66,40,20}
x1={10,20,30,55,60,40}
print(x1,type(x1))"""
x={"python","java","html"}
y={"c","dotnet","ruby","python"}
print(y,type(y))
print(x,type(x))
x.add("django")
print(x)
x.clear()
print(x,type(x))
x={"python","java","html"}
z=x.copy()
print(x)
print(y)
print(z)
z.clear()
print(z)
print(x.difference(y))
x.difference_update(y)
print(x)
x={"python","java","html"}
y.difference_update(x)
print(x)
print(y)
x={"python","java","html","c"}
y={"c","dotnet","ruby","python"}
print(y.intersection(x))
x={"python","java","html","c"}
y={"c","dotnet","ruby","python"}
print(x.intersection_update(y),id(x))
print(y)
print(x)
x={"python","java","html","c"}
y={"c","dotnet","ruby","python"}
x.remove("python")
print(x)
y.discard("python")
x.discard("c")
y.remove("c")
print(y)
print(x.isdisjoint(y))
x={10,20,30,50,60,70}
y={30,60}
print(x.issubset(y))
print(y.issubset(x))
print(x.issuperset(y))
print(y.issuperset(x))