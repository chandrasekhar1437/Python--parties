def decor(f):
    def upper():
        n=f()
        print(n.upper())
    return upper

@decor
def myfunction():
    return "python"
myfunction()
print()
def decor1(x):
    def upper1():
        n=x()
        print(n.capitalize())
        print(n.upper())
        print(n.lower())
        print(n.split())
        print(n.swapcase())
    return upper1

@decor1
def myfunction1():
    return "python is best\t a,A,B,b"
myfunction1()