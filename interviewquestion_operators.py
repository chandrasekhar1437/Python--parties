#promble1
l1=[10,20,30]
l2=[10,20,30]
print(l1,id(l1))
print(l2,id(l2))
print(l1 is l2)
print(l1 is not l2)
l1=[10,20,30]
l2=l1
print(l1 is l2)
""""
#caching only integers values upto 0 to 256 and -5 to -1 same loction in registers
"""
a=10
b=10
print(a is b)


