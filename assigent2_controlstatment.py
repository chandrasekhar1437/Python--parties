# print reverse of a number using string concept
n=input("enter number ")
print(n[::-1])
# print reverse of a number without string
n=int(input("enter number "))
n1=n
rev=0
ld=0
while(n>0):
    ld=n%10
    rev=(rev*10)+ld
    n=n//10
else:
    print(f"reverse of given number {n1} is {rev}")

