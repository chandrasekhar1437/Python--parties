# program to demonstrate file
with open("abc.txt","a") as f:
    print(f, type(f))
    print(f.mode)
    print(f.readable())
    print(f.writable())
    print(f.closed)
    f.write("\npython")
print(f.closed)