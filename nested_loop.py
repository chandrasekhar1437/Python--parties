#  print 10 to 100 below prime number(#programe to check
for n in range(10,100):
    p=0
    for i in range(2, n):
        if n % i == 0:
            print(f"not a prime {n}")
            break
    else:
        print(f"it is prime number is {n}")
print("")
#program print stars in increase
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")

