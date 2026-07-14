"""list and Tuples"""
#lists&tuples=to store collection of similar or different types values
#list=mutable
"""" 
list---->[]----->mutable to change data
tulpes----()---->immutable unchange data
"""
            #list[] mutable
"""     #empty list
#syntax:
        name=[]
        name=list()
       #non-empty list 
#syntax:
       name=[item1,item2,item3]
       example: marks=[95,89,25,79]
"""
marks=[]
marks1=list()
print(marks,type(marks))
print(marks1,type(marks1))
marks2=[20,30,45,50]
print(marks2,type(marks2))
s="python coures"
l=list(s)
print(l,len(l))
print(len(marks2))
marks2=[20,30,45,50,20,30,45]
print(marks2)
print(marks2[:5])
print(marks2[::-1])
marks3=[20,30,40,20]
'''     #predefined/built in functions
 append(): to add element at the end of the list
 clear():Removes all items from the list
 copy():to create a duplicate copy of original
 count():to retrieve the number of occurrences of an item in the list
 extend():to add list of elements into another list
 index(): to get the index of particular item in the given list
 insert():to insert an element at given index
 pop():removes last element from the list
 pop(index):removes element at particular index from the list
 remove(item):removes first occurrence of that particular item from the list
 reverse():it reverse the original list and update it
 sort():sorts the elements in ascending order
        for descending order we need to give reverse attribute
             object.sort(reverse=True)
del----> operator item & multiple items entire list
 '''
print(marks,id(marks))
marks.append(90)
print(marks,id(marks),len(marks),marks[:])
print(marks2,type(marks2),id(marks2))
marks2.clear()
print(marks2,type(marks2),id(marks2))
print(marks1,id(marks1),len(marks1))
marks1.append(30)
marks1.append(marks3)
print(marks2)
print(marks1,id(marks1),len(marks1))
print(marks1[1][::-1])
m1=marks1.copy()
m2=marks1
print(marks1,id(marks1))
print(m1,id(m1))
print(m2,id(m2))
print(marks3.count(30))
marks4=[20,30,40]
marks5=[50,60,70]
marks4.append(marks5)
print(marks4,len(marks4))
marks4=[20,30,40]
marks5=[50,60,70]
print(marks4,len(marks4))
marks4.insert(0,10)
print(marks4,len(marks4))
marks4.extend(marks5)
print(marks4,len(marks4))
print(marks4.index(30))
marks4.insert(3,45)
print(marks4,len(marks4))
print(marks4.pop())
print(marks4)
marks4.pop(2)
print(marks4)
print(marks4.remove(50))
print(marks4)
marks4.reverse()
print(marks4)
marks6=[20,30,78,25,56,78,96,56,22,78,46,23]
print(marks6,len(marks6))
marks6.sort()
print(marks6)
marks6.sort(reverse=True)
print(marks6)
del marks6[3]
print(marks6)
del marks6[2:4]
print(marks6)
del marks6
#print(marks6)
print(marks5)
marks5.sort(reverse=True)
print(marks5)
marks5[0]=55
print(marks5)
print(marks5.pop())
