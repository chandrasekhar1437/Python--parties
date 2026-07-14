#program print stars in increase
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
print("")
#print hollow right angle triangle
for i in range(1,6):
    for j in range(1,6):
        if( i==j or i==5 or j==1 ):
            print("*",end=" ")
        else:
            print(" ",end="")
    print(" ")
print()
#print  right angle triangle in while
i=1
while  (i<6):
    j=1
    while (j<=i):
        print("*",end="")
        j=j+1
    print()
    i=i+1