#program to demonstrate match selection control statement
n=int(input("enter the number "))
match(n):
    case 1:
        print("hi")
        print("welcome")
    case 2:
        print("2")
    case 3:
        print("3")
        print("welcome")
    case 4:
        print("4")
        print("india")
    case 5:
        print("chandu")
        print("python")
    case _:#default case
        print("no match found")

# read day number
d=int(input("enter number is "))
match(d):
    case 1:
        print("sunday")
    case 2:
        print("monday")
    case 3:
        print("tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("thursday")
    case 6:
        print("friday")
    case 7:
        print("saturday")
    case _:
        print("no found")