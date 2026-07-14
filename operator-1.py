#write a program to add two number
"""
program to add two numbers
step-1 take two number
a=10,b=20
step-2 add two number
c=a+b

"""
a=10
b=20
c=a+b
print(f"result of a+b is {c}")
print("result of a+b is {}".format(c))
print(f"result of a+b is",c)
print(f"result of a+b is %d " %c)
a=int(input("enter value a "))      #typecasting-convert this str into int
b=int(input("enter value b "))      #typecasting-convert this str into int
c=(a+b)
print(f"result of a+b is",c)
#average of three number
# step 1 take a 3 varbiles (3 values)
a=int(input("enter you number"))
b=int(input("enter you number"))
c=int(input("enter of number"))
#average of formulu
d=(a+b+c)
avr=d/3
#print result
print("average of result",avr)