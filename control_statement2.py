""""
iteration / loop :
          1 for loop:
           for
           for-else
          2 while loop:
          2.0
           2.1 while-else:
while(condition):
initialization
condition
updation
         statement:1
         statement:2
 else:



"""
#program to print 1 to number using while
i=1
n=int(input("enter number is"))
while i<=n:
    # if(i==15):
    #     break
    print(i)
    i=1+i
else:
    print("i am else part")
    r = range(1, 11)
    for i in r:
        print(i, end=" ,")
#program multiplication table
n=int(input("enter number"))
i=1
while i<=10:
    print(f"{n}x{i}={n*i}")
    i=1+i
else:
    print("multiplication printed succes")
# print sum of frist n numbers using while loop
# read number
n=int(input("enter number "))
i=1
sum=0
while i<=n:
    print(i)
    i=i+1
    sum = sum + i
else:
    print(f"result of frist {n} numbers sum is {sum}")
