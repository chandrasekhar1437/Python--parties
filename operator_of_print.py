a=10
b=20
print(a)
print('a/`')
print("a")
print(a,b)
a="chandu"
b="nunna"
print(a,b)
exp=18
print("my experience is",exp)
""""

    same line using "end="
         #format specifiers
         %d,%f,%s
         #"{}".format---->less than 3.5 version
         #f"{}"---- fstring format great than 3.6 version
"""
r=range(0,6)
for s in r:
    print(s, end=",")

a=10
b=2.52
c="chandu"
print("value of a is %d" %a)
print("value of b is %0.2f" %b)
print("my name is %s" %c)
print("a value is {}".format(a))#------>version less than 3.6
print(f"a value is {a}") # --------> version minimum 3.6
print(f"b value is {b}") # --------> version minimum 3.6
l=(20,30,40,50)
print(f"l value is {l}")

