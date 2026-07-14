from sys import exception


class MyError(Exception):
    pass


m=int(input("enter a mark "))

try:
    if (m<10):
        raise MyError("you entered wrong literal.un accepted value error")
except MyError:
    print("hello...i want to apply for revaluation as my marks is less than 10 ")