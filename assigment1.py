# even or odd program in python
# step1 take input
a=int(input("enter number"))
#second step division with 2 find remainder
if a%2==0:
    print("it is even number ",a)
else:
    print("it is odd number",a)
print("even and odd program End ")

# program to check whether given number is division by 3& 11 or not
# step1 take number
a=int(input("enter tne number"))
# step division with 11 and 3 find remainder
if a%3==0 and a%11==0:
    print("to division 3 & 11 is ",a)
else:
    print("not division 3&11 is ",a)
print("the end")
#program to check given string is vowel or consonant
# step 1 take a character
c=input("enter a character")
# check whether given character is a/e/i/o/u or not
if(len(c)>1):
    print("input must be single character")
else:
    if (c == 'a' or c == 'e' or c == 'i' or c == 'u'):
        print("given character is vowel ", c)
    else:
        print("given characteris consonant", c)

