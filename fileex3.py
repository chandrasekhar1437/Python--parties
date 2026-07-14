# program to demonstrate read operation on file in python
with open("abc1.txt","r") as n:
    s=n.readline()
    s1=n.readlines()
    print(type(s))
    print("file contents of def.txt:\n")
    print(s)
    print(s1)
