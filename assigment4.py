# program to find 100 below fibonacci series
a=0
b=1
c=a+b
print(a,b,end=" ")
while(c<=100):
    print(c,end=" ")
    a=b
    b=c
    c=a+b

