# program to print a number in words
n=input("enter number ")

for i in n:
    if(i=="0"):
        print("zero")
    elif(i=="1"):
        print("one",end=" ")
    elif(i=="2"):
        print("two",end=" ")
    elif(i=="3"):
        print("three",end=" ")
    elif(i=="4"):
        print("four",end=" ")
    elif(i=="5"""):
        print("five",end=" ")
    elif(i=="6"):
        print("six",end=" ")
    elif(i=="7"):
        print("seven",end=" ")
    elif(i=="8"):
        print("eight",end=" ")
    elif(i=="9"):
        print("nine",end=" ")




# program to find factors of a given number
n=int(input("enter number is "))

for i in range(1,n+1):
    if(n%i==0):
        print(i,end=" ")








#pxrogram to find exponent to base number without using exponent operator(**)
b=int(input("enter a base value is "))
e=int(input("enter a exponent value is"))
p=1
for i in range(1,e+1):
    p=p*b
print(f"{b} ** is: {p}")
