# software that calculate division of two number
print("--------------welcome to division two number software-----------")
try:
    a= int(input("enter a value is "))#value error chance
    b= int(input("enter b value is "))# value error
    c=a/b #zero division error
    print(f"division of {a}/{b} is:{c}")
except ValueError:
    print("please  enter proper integer values for a,b")
except ZeroDivisionError:
    print("please enter greater than 0 value for b ")
else:
    print("i am else ")
finally:
    print("thank you")
print("--------thank you... welcome again-----------")