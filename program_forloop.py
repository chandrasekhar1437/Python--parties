# program to print 1 to n number using for
n=int(input("enter number is "))
for i in range(1,n+1):
    print(i)

#prograg sum of digits n=3456 in change
n=3456
s=0
s1=str(n)
for i in s1:
    s=s+int(i)
print(f"sum of digit {s}")

#prograg sum of digits n=? in while
n=int(input("enter number "))
s=0
l=0
while (n>0):
    l=n%10
    s=s+l
    n=n//10
print(s)

