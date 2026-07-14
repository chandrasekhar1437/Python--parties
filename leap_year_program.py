# given year is leap year or not
# step1 take a number
y=int(input("enter you year "))
# second step division 4 find reminder
if (y%4==0) and y%100!=0 or y%400==0 :
    print("it is a leap year is",y)
else:
    print("it is not a leap year is ",y)