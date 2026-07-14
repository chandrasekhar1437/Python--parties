# x={10,20,30,40,{1,2,3}}
# print(x)
# set in set not working
#set in list not working
# tuple in set it working
#set in tuple it working
#list in set it working

x={10,20,(1,2,3),50}
print(x,type(x),next(iter(x)))
x=[10,20,30,{20,10},10]
print(x,type(x))
y=(20,30,{10,2},20)
print(y,type(y))
            # frozenset
#frozenset:immutable version of set
#it is immutable
"""
      #built-in/predefined functions
      isdisjoint(),issuperset(),issubset()'union(),intersection(),difference(),symmertic_difference()
synax
s={10,20,30}
to contert frozenset
"""
s={10,20,30,40}
s.add(50)
print(s,type(s))
y=frozenset(s)
print(y,type(y))
y1=frozenset({10,20,30,40,50})
z1=frozenset({1,2,3})
x1=frozenset({40,50,60})
print(x1,type(x1),id(x1))
print(z1,type(z1),id(z1))
print(y1,type(y1),id(y1),len(y1))
print(x1.isdisjoint(y1))
print(z1.issubset(y1))
print(y1.issuperset(z1))
print(y1.union(x1))
print(z1.difference(x1))
print(x1.difference(y1))
print(x1.intersection(y1))
print(y1.symmetric_difference(x1))