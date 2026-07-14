amount=50000

def amounts():
    global amount
    print("total amount",amount)

def despoit():
    amt=int(input("enter our amount"))
    amt=amount+amt
def with_draw():
    amt=int(input("enter our amount"))
    amount=-amt
