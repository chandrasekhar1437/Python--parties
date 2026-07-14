"""""# program to demonstrate recursion in function
def sayhello(n):
    print("hello",n)
    n=n+1
    if(n==100):
        return
    sayhello(n)
sayhello(10)
print("end")"""
# program find the factorial in recursion function
n=int(input("enter the number "))
f=1
def fact(n):
    global f
    f=f*n
    n=n-1
    if n==1:
        return
    fact(n)

fact(n)
print(f)
