import bank as b
while(True):
    print("*******welcome to our bank **********")
    print("1.deposit amount\n2.show balance\n3.send payment\n40 exit")
    c=6
    try:
        c=int(input("choice please(1-4) option:"))
    except ValueError:
        print("please only enter 1-4 digits number only")

    match c:
        case 1:
            b.deposit()
        case 2:
            b.showbalance()
        case 3:
            b.sendpayment()
        case 4:
            print("thank you using our services .welcome again")
            break
        case _:
            print("your choice is wrong. please try again with number between 1 to 4")
