          #Nested lists:
#Nested lists= A list inside another list is called nested list
x=[10,20,30,[1.2,3.5],50,60]
user=["chandu",27,["kudupuru","kota",[10,20,30]],"7989578182"]
print(user,id(user),type(user))
print(user[2][2][2])
del user[2][2][1]
print(user)
user.remove("chandu")
print(user)
print(user[1][2].insert(1,20))
print(user)
print(user[1][2].pop(1))