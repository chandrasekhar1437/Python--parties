# program to chek whether given number is prime or not
#read in
n=int(input("enter number is "))
# check whether n is division by any number in the range 2 to n-1
# if divisible then declare it as not prime

for i in range(2,n):
    if n%i==0:
        print(f"not a prime {n}")
        break
else:
        print(f"it is prime number is {n}")
