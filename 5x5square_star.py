for i in range(1,6):
    for l in range(1,6):
        print("*",end=" ")
    print("")
print("completed program")
print("")
# print the box 5*5 in star
for o in range(1,6):
    for i in range(1,6):
        if(o==1 or o==5 or i==1 or i==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print("")