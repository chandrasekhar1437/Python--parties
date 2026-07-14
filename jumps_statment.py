"""    #jump statment
1. break
2.continue
3.returns
4.pass

 """
# example of break in program
for i in range(1,11):
    if(i==5):
        break
    print(i)
else:
    print("i am else")
print("for after ")
i=1
while(i<11):
     if i==5:
         break

     print(i)
     i=1+i
else:
    print("i am while else")
print("while after ")


#example of continue in program
for i in range(1,11):
    if(i==5):
        continue
    print(i)
else:
    print("i am else")
print("for after ")
