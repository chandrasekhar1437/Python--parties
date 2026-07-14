#this is bank module
class AmountError(Exception):
    pass
class SendpaymentError(Exception):
    pass

balance=10000.0

def deposit():
    global balance
    try:
        amt=float(input("enter amount to be deposited:"))
        if amt<=0:
            raise AmountError("wrong Amount literal entered")
        balance = balance + amt
    except ValueError:
        print("please enter amount properly")
    except AmountError:
        print("please enter amount greater than zero value ")
    except AmountError:
        print("wrong Amount literal entered")
def showbalance():
    print(f"Total balance in your account is: ", balance)
def sendpayment():
    global balance
    try:
        amt=float(input("enter amount to sent:"))
        if amt<=0:
            raise AmountError("wrong Amount literal entered")
        if amt>balance:
            raise SendpaymentError("operation unable to completed")
        balance-=amt
    except ValueError:
        print("please enter balance in numbers")
    except AmountError:
        print("please enter amount greater than zero value ")
    except SendpaymentError:
        print("sending amount must be less than available")