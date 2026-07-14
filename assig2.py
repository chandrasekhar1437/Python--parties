#print sum of frist and last digits of a number using str
n=input("enter number ")
ld=n[-1]
fd=n[0]
sum=int(ld)+int(fd)
print(sum)
#print sum of frist and last digits of a number not using str
n=int(input("enter number"))
n1=n
fd=0
ld=n%10
while(n>=10):
    n=n//10
fd=n
sum=fd+ld
print(sum)
# program to check whether given number is palidrome or not using string
n=input("enter number")
n1=n
rev=n[::-1]
if n1==rev:
    print("it is palidrome",n1)
else:
    print("it not palidrome",n1)

# program to find factorial of a given number
n=int(input("enter number"))
n1=n
p=1
for i in range(1,n+1):
    p=i*p
print(f"{n1}!is factorial of {p}")