#control statement / control flow statement / flow control statement
"""
  They are 3 different types of statement
  1.selection statement
  2.iterative statement
  3.jump/ transfer flow statement


  1.selection statement
  -if(simple if, if-else,if-elif-else)
  -match
  2.iterative statement
  -for
  -while
  3jump / transfer flow statement
  -break
  -continue
  -pass
  -return

"""


'''
    # selection statement:
    simple if statement:
     syntax:-
              if(condition):
               .. ..statement
               a=10
               b=5
               if(a>b):
                  print("a is big)
                  print("hi")
                  print("welcome")
               print("program ends")
    if_else:
     syntax:-
     
     
     
     
     if-elif-else:
      syntax:-
                if(condition1)
                   statement
                elif(condition2)
                   statement
                elif(condition....)
                   statement
                else:
                   statement
        match case:
         syntax:-
                  n=5
                  match(3):
                     case:1
                        print("hello")
              
'''
#program to demonstrate simple if
a = 10
b = 5
if a<b :
   print("a is big")
   print("hi")
   print("welcome ")
if a>b :
   print("b is big")
   print("hi")
   print("welcome ")
print("program ends")
#program to demonstrate if-else
a=15
b=15
if a==b :
    print("a is big")
    print("welcome")
else:
    print("b is big")
    print("hello")
print("end of program")
#program to check whether given number is positive or negative or zero program in if-elif-else
#take number
a=int(input("enter number"))
#check
if a>0:
    print("it is positive number",a)
elif a<0:
    print("it is negative number",a)
else:
    print("it is zero")

