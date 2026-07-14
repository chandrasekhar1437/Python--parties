#program demonstrate function
#function definition
def add():
    a=int(input("enter value a is "))
    b=int(input("enter value b is "))

    c=a+b
    return a,b,c
    print(f"add of a and b is {c}")
#function calling
a,b,n=add()
a1,b1,n1=add()
print(f"addition of {a} and {b} is {n}")
print(f"addition of {a1} and {b1} is {n1}")

